# FinPilot - Implementation Guide
**Complete roadmap for finishing the remaining 40% of the project**

---

## Phase 1: Frontend-Backend Integration (2-3 hours)

### Step 1.1: Create API Client Utility
**File**: `finpilot-frontend/lib/api.ts`

```typescript
import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle token refresh
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      const refreshToken = localStorage.getItem('refresh_token');
      if (refreshToken) {
        try {
          const { data } = await axios.post(`${API_URL}/auth/refresh`, {
            refresh_token: refreshToken,
          });
          localStorage.setItem('access_token', data.access_token);
          return api(error.config);
        } catch {
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
          window.location.href = '/login';
        }
      }
    }
    return Promise.reject(error);
  }
);

export default api;
```

### Step 1.2: Create Custom Hooks for Data Fetching
**File**: `finpilot-frontend/hooks/useTransactions.ts`

```typescript
import { useQuery, useMutation } from '@tanstack/react-query';
import api from '@/lib/api';

export const useTransactions = () => {
  return useQuery({
    queryKey: ['transactions'],
    queryFn: async () => {
      const { data } = await api.get('/transactions');
      return data;
    },
  });
};

export const useCreateTransaction = () => {
  return useMutation({
    mutationFn: async (transaction) => {
      const { data } = await api.post('/transactions', transaction);
      return data;
    },
  });
};
```

### Step 1.3: Implement Authentication Pages
**File**: `finpilot-frontend/app/login/page.tsx`

```typescript
'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import api from '@/lib/api';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const { data } = await api.post('/auth/login', { email, password });
      localStorage.setItem('access_token', data.access_token);
      localStorage.setItem('refresh_token', data.refresh_token);
      router.push('/');
    } catch (error) {
      console.error('Login failed:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
        <h1 className="text-2xl font-bold mb-6">FinPilot</h1>
        <form onSubmit={handleLogin} className="space-y-4">
          <Input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <Input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <Button type="submit" disabled={loading} className="w-full">
            {loading ? 'Logging in...' : 'Login'}
          </Button>
        </form>
      </div>
    </div>
  );
}
```

### Step 1.4: Connect Dashboard to Real Data
**File**: `finpilot-frontend/app/page.tsx` (Update)

```typescript
'use client';

import { useEffect, useState } from 'react';
import api from '@/lib/api';
import { useRouter } from 'next/navigation';

export default function Dashboard() {
  const [dashboardData, setDashboardData] = useState(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          router.push('/login');
          return;
        }
        const { data } = await api.get('/dashboard');
        setDashboardData(data);
      } catch (error) {
        console.error('Failed to fetch dashboard:', error);
        router.push('/login');
      } finally {
        setLoading(false);
      }
    };

    fetchDashboard();
  }, [router]);

  if (loading) return <div>Loading...</div>;
  if (!dashboardData) return <div>No data</div>;

  return (
    <div className="space-y-6">
      {/* Balance Card */}
      <div className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-6 rounded-lg">
        <p className="text-sm opacity-90">Current Balance</p>
        <h2 className="text-3xl font-bold">₹{dashboardData.balance}</h2>
        <p className="text-sm mt-2">Safe to spend: ₹{dashboardData.safe_to_spend}</p>
      </div>

      {/* Rest of dashboard components */}
    </div>
  );
}
```

---

## Phase 2: AI Coach & Advanced Features (2-3 hours)

### Step 2.1: Integrate OpenAI API
**File**: `finpilot/backend/app/utils/openai_client.py`

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_coach_response(query: str, user_context: dict) -> str:
    """Get AI coach response using OpenAI GPT-4o-mini"""
    
    prompt = f"""
    You are FinPilot, a friendly financial coach for gig workers in India.
    
    User Context:
    - Current Balance: ₹{user_context.get('balance', 0)}
    - Safe to Spend Today: ₹{user_context.get('safe_to_spend', 0)}
    - Predicted Income (7 days): ₹{user_context.get('predicted_income', 0)}
    - Active Jars: {user_context.get('jars', [])}
    - Active Goals: {user_context.get('goals', [])}
    
    User Query: {query}
    
    Provide a helpful, actionable response in 2-3 sentences.
    Always explain WHY, not just WHAT.
    Use Indian currency (₹) and relatable examples.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=200
    )
    
    return response.choices[0].message.content
```

### Step 2.2: Implement Chat Endpoint
**File**: `finpilot/backend/app/api/coach.py` (Update)

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils.openai_client import get_coach_response
from app.models.user import User
from app.utils.auth import get_current_user

router = APIRouter(prefix="/coach", tags=["coach"])

@router.post("/query")
async def query_coach(
    query: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get AI coach response"""
    
    # Build user context
    user_context = {
        'balance': get_user_balance(current_user.id, db),
        'safe_to_spend': calculate_safe_to_spend(current_user.id, db),
        'predicted_income': get_predicted_income(current_user.id, db),
        'jars': get_user_jars(current_user.id, db),
        'goals': get_user_goals(current_user.id, db),
    }
    
    # Get AI response
    response = get_coach_response(query, user_context)
    
    # Save to chat history
    save_chat_message(current_user.id, query, response, db)
    
    return {
        "query": query,
        "response": response,
        "context": user_context
    }
```

### Step 2.3: Create Chat UI Component
**File**: `finpilot-frontend/app/coach/page.tsx` (Update)

```typescript
'use client';

import { useState, useRef, useEffect } from 'react';
import api from '@/lib/api';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

interface Message {
  id: string;
  type: 'user' | 'coach';
  content: string;
  timestamp: Date;
}

export default function CoachPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    // Add user message
    const userMessage: Message = {
      id: Date.now().toString(),
      type: 'user',
      content: input,
      timestamp: new Date(),
    };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const { data } = await api.post('/coach/query', { query: input });
      const coachMessage: Message = {
        id: (Date.now() + 1).toString(),
        type: 'coach',
        content: data.response,
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, coachMessage]);
    } catch (error) {
      console.error('Failed to get coach response:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-white">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((msg) => (
          <div
            key={msg.id}
            className={`flex ${msg.type === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-xs px-4 py-2 rounded-lg ${
                msg.type === 'user'
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-100 text-gray-900'
              }`}
            >
              {msg.content}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <form onSubmit={handleSendMessage} className="p-4 border-t">
        <div className="flex gap-2">
          <Input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask me anything about your finances..."
            disabled={loading}
          />
          <Button type="submit" disabled={loading}>
            Send
          </Button>
        </div>
      </form>
    </div>
  );
}
```

---

## Phase 3: Data Visualization & Polish (1-2 hours)

### Step 3.1: Add Recharts Visualization
**File**: `finpilot-frontend/components/IncomeChart.tsx`

```typescript
'use client';

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

interface IncomeChartProps {
  data: Array<{ date: string; amount: number }>;
}

export function IncomeChart({ data }: IncomeChartProps) {
  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip formatter={(value) => `₹${value}`} />
        <Line type="monotone" dataKey="amount" stroke="#3b82f6" strokeWidth={2} />
      </LineChart>
    </ResponsiveContainer>
  );
}
```

### Step 3.2: Add Loading States & Error Handling
**File**: `finpilot-frontend/components/LoadingSpinner.tsx`

```typescript
export function LoadingSpinner() {
  return (
    <div className="flex items-center justify-center p-4">
      <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
    </div>
  );
}
```

### Step 3.3: Add Toast Notifications
**File**: `finpilot-frontend/components/Toast.tsx`

```typescript
'use client';

import { useState, useCallback } from 'react';

export function useToast() {
  const [toasts, setToasts] = useState<Array<{ id: string; message: string; type: 'success' | 'error' }>>([]);

  const addToast = useCallback((message: string, type: 'success' | 'error' = 'success') => {
    const id = Date.now().toString();
    setToasts((prev) => [...prev, { id, message, type }]);
    setTimeout(() => {
      setToasts((prev) => prev.filter((t) => t.id !== id));
    }, 3000);
  }, []);

  return { toasts, addToast };
}
```

---

## Phase 4: Demo Features & Deployment (1-2 hours)

### Step 4.1: Create "Raju's Week" Demo
**File**: `finpilot-frontend/components/DemoAnimation.tsx`

```typescript
'use client';

import { useState } from 'react';
import { Button } from '@/components/ui/button';

const DEMO_DATA = [
  {
    day: 'Monday',
    transaction: { amount: 600, type: 'income', description: 'Delivery work' },
    narration: 'Raju starts his week with ₹600 from delivery work',
  },
  {
    day: 'Tuesday',
    transaction: { amount: 300, type: 'expense', description: 'Food' },
    narration: 'Spent ₹300 on food. Balance: ₹900',
  },
  // ... more days
];

export function DemoAnimation() {
  const [currentDay, setCurrentDay] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);

  const playDemo = async () => {
    setIsPlaying(true);
    for (let i = 0; i < DEMO_DATA.length; i++) {
      await new Promise((resolve) => setTimeout(resolve, 2000));
      setCurrentDay(i);
    }
    setIsPlaying(false);
  };

  return (
    <div className="space-y-4">
      <Button onClick={playDemo} disabled={isPlaying}>
        {isPlaying ? 'Playing...' : 'Play Raju\'s Week'}
      </Button>
      <div className="p-4 bg-gray-50 rounded-lg">
        <h3 className="font-bold">{DEMO_DATA[currentDay]?.day}</h3>
        <p className="text-sm text-gray-600">{DEMO_DATA[currentDay]?.narration}</p>
      </div>
    </div>
  );
}
```

### Step 4.2: Deployment Configuration

**Railway Backend Deployment**:
1. Push code to GitHub
2. Connect Railway to GitHub repo
3. Set environment variables:
   - `DATABASE_URL`
   - `JWT_SECRET`
   - `OPENAI_API_KEY`
4. Deploy

**Vercel Frontend Deployment**:
1. Connect GitHub repo to Vercel
2. Set environment variables:
   - `NEXT_PUBLIC_API_URL` (Railway backend URL)
3. Deploy

---

## Testing Checklist

- [ ] User can register and login
- [ ] Dashboard displays real data
- [ ] Transactions can be added and viewed
- [ ] Jars auto-allocate correctly
- [ ] Goals track progress
- [ ] AI Coach responds to queries
- [ ] Income predictions display with confidence
- [ ] Alerts trigger correctly
- [ ] Mobile responsive design works
- [ ] All API endpoints return correct data
- [ ] Error handling works properly
- [ ] Loading states display correctly

---

## Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql://user:password@localhost:5432/finpilot
JWT_SECRET=your-secret-key-here
OPENAI_API_KEY=sk-...
ALLOWED_ORIGINS=http://localhost:3000,https://finpilot.vercel.app
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## Quick Start Commands

```bash
# Backend
cd finpilot/backend
python run.py

# Frontend
cd finpilot-frontend
npm run dev

# Both running:
# Backend: http://localhost:8000
# Frontend: http://localhost:3000
# API Docs: http://localhost:8000/docs
```

---

## Success Metrics

✅ All 30+ API endpoints functional
✅ Frontend-backend integration complete
✅ ML predictions accurate (70%+ confidence)
✅ Auto-categorization 80%+ accurate
✅ Zero critical bugs
✅ Response time < 500ms
✅ Mobile responsive
✅ Demo animation works
✅ Deployment successful

---

**Estimated Time to Complete**: 6-8 hours
**Difficulty Level**: Medium
**Priority**: High

