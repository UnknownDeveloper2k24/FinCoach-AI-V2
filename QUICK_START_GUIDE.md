# FinPilot - Quick Start Guide

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.9+
- PostgreSQL (running on localhost:5432)

### Installation

#### 1. Backend Setup
```bash
cd /home/code/finpilot/backend
pip install -r requirements.txt
python run.py
```
Backend runs on: **http://localhost:8000**
API Docs: **http://localhost:8000/docs**

#### 2. Frontend Setup
```bash
cd /home/code/finpilot-frontend
npm install
npm run dev
```
Frontend runs on: **http://localhost:3001**
Public URL: **https://finpilot-app.lindy.site**

---

## 🔐 Demo Credentials

**Email:** demo@finpilot.com
**Password:** demo123

---

## 📱 Application Features

### 1. Dashboard
- Real-time balance display
- Monthly income/expense tracking
- Income predictions with confidence scores
- Smart Jars overview
- Active alerts
- Quick action buttons

### 2. Transactions
- Add income/expense transactions
- 12 predefined categories
- Transaction history
- Delete transactions
- Real-time updates

### 3. Smart Jars
- Create savings jars with targets
- Set priorities and deadlines
- 6 color options
- Allocate money to jars
- AI recommendations
- Progress tracking

### 4. Financial Goals
- Set financial goals
- Track progress
- Monthly target calculations
- Deadline countdowns
- Goal status indicators

### 5. AI Coach
- Chat with AI financial advisor
- Get personalized recommendations
- Suggested questions
- Chat history

---

## 🏗️ Project Structure

```
/home/code/
├── finpilot/
│   └── backend/
│       ├── app/
│       │   ├── models/
│       │   ├── routes/
│       │   ├── services/
│       │   └── ml_models/
│       ├── database/
│       └── run.py
├── finpilot-frontend/
│   ├── app/
│   │   ├── page.tsx (Dashboard)
│   │   ├── login/
│   │   ├── register/
│   │   ├── transactions/
│   │   ├── jars/
│   │   ├── goals/
│   │   └── coach/
│   ├── lib/
│   │   ├── api.ts
│   │   ├── hooks.ts
│   │   ├── auth-context.tsx
│   │   └── protected-route.tsx
│   └── components/
└── Documentation/
    ├── PHASE_1_COMPLETION_REPORT.md
    └── QUICK_START_GUIDE.md
```

---

## 🔄 API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `POST /auth/refresh` - Refresh token
- `GET /auth/me` - Get current user

### Transactions
- `GET /transactions` - List all transactions
- `POST /transactions` - Create transaction
- `DELETE /transactions/{id}` - Delete transaction

### Jars
- `GET /jars` - List all jars
- `POST /jars` - Create jar
- `POST /jars/{id}/allocate` - Allocate money
- `GET /jars/recommendations` - Get AI recommendations

### Goals
- `GET /goals` - List all goals
- `POST /goals` - Create goal
- `DELETE /goals/{id}` - Delete goal

### Predictions
- `GET /predictions/income` - Income prediction
- `GET /predictions/expense` - Expense prediction
- `GET /predictions/cashflow` - Cashflow prediction

### AI Coach
- `POST /coach/query` - Ask question
- `GET /coach/history` - Get chat history

### Dashboard
- `GET /dashboard` - Get dashboard summary

---

## 🎨 UI/UX Features

### Design
- CRED-like premium mobile-first design
- Gradient backgrounds (blue to indigo)
- Bottom navigation bar
- Card-based layout
- Smooth animations

### Components
- shadcn/ui components
- Lucide React icons
- Tailwind CSS styling
- Responsive design

### User Experience
- Loading states on all operations
- Error messages with feedback
- Form validation
- Empty states with suggestions
- Auto-scroll in chat
- Quick action buttons

---

## 🔐 Security

### Authentication
- JWT token-based auth
- Token stored in localStorage
- Automatic token refresh
- Protected routes
- Secure logout

### Data Protection
- API endpoints require auth
- Request interceptors
- Error handling
- Session management

---

## 📊 Technology Stack

### Backend
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Auth:** JWT
- **ML:** scikit-learn, pandas, numpy
- **API:** RESTful with 30+ endpoints

### Frontend
- **Framework:** Next.js 15.5.6
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **Components:** shadcn/ui
- **Icons:** Lucide React
- **State:** React Context + Custom Hooks

---

## 🧪 Testing

### Manual Testing
1. Open http://localhost:3001
2. Click "Sign up" to create account
3. Or use demo credentials to login
4. Navigate through all pages
5. Test all features

### API Testing
1. Open http://localhost:8000/docs
2. Use Swagger UI to test endpoints
3. All endpoints require authentication

---

## 🐛 Troubleshooting

### Frontend not loading
```bash
# Kill existing process
lsof -ti:3001 | xargs kill -9

# Restart
cd /home/code/finpilot-frontend
npm run dev
```

### Backend not responding
```bash
# Check if running
curl http://localhost:8000/docs

# Restart
cd /home/code/finpilot/backend
python run.py
```

### Database connection error
```bash
# Check PostgreSQL
psql -h localhost -U $PGUSER -d finpilot

# Create database if needed
createdb -h localhost finpilot
```

---

## 📈 Performance Tips

### Frontend
- Use Chrome DevTools for profiling
- Check Network tab for API calls
- Monitor React component renders

### Backend
- Check API response times in logs
- Monitor database queries
- Use Swagger UI for endpoint testing

---

## 🚀 Deployment

### Production Build
```bash
cd /home/code/finpilot-frontend
npm run build
npm run start
```

### Environment Variables
```
NEXT_PUBLIC_API_URL=https://api.finpilot.com
```

---

## 📞 Support

### Documentation
- API Docs: http://localhost:8000/docs
- Frontend Code: Well-commented components
- Backend Code: Type hints throughout

### Common Issues
- Check browser console for errors
- Check terminal for backend logs
- Verify API is running
- Check authentication token

---

## 🎯 Next Steps

### Phase 2: Advanced Features
- Enhanced AI Coach
- Advanced analytics
- Budget recommendations
- Spending patterns
- Goal predictions

### Phase 3: Polish
- Error handling
- Performance optimization
- Mobile testing
- Accessibility

### Phase 4: Deployment
- Production setup
- Demo data
- Documentation
- Launch

---

## 📝 Notes

- All pages are protected with authentication
- Demo credentials work immediately
- API requires valid JWT token
- Frontend auto-refreshes on code changes
- Backend requires manual restart

---

**Last Updated:** November 26, 2025
**Status:** Phase 1 Complete ✅
**Ready for:** Phase 2 Implementation
