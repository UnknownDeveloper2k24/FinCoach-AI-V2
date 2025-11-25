# 📁 FinPilot - Complete File Structure & Locations

**Last Updated**: November 25, 2025, 11:30 PM IST

---

## 📂 Root Directory Structure

```
/home/code/
├── finpilot/                          # Main project directory
│   ├── backend/                       # FastAPI backend
│   ├── finpilot-frontend/             # Next.js frontend
│   ├── README.md                      # Project README
│   └── requirements.txt               # Python dependencies
├── IMPLEMENTATION_GUIDE.md            # Step-by-step implementation roadmap
├── PROJECT_SUMMARY.md                 # Comprehensive project overview
├── FINPILOT_STATUS.md                 # Build status and feature matrix
├── FINAL_SUMMARY.md                   # Complete delivery summary
└── FILES_AND_LOCATIONS.md             # This file
```

---

## 🔙 Backend Directory Structure

### Location: `/home/code/finpilot/backend`

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                        # FastAPI app initialization
│   ├── database.py                    # Database connection & session
│   ├── config.py                      # Configuration settings
│   │
│   ├── models/                        # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── user.py                    # User model
│   │   ├── transaction.py             # Transaction model
│   │   ├── jar.py                     # Jar model
│   │   ├── goal.py                    # Goal model
│   │   ├── alert.py                   # Alert model
│   │   ├── user_interaction.py        # UserInteraction model
│   │   └── prediction.py              # Prediction model
│   │
│   ├── schemas/                       # Pydantic validation schemas
│   │   ├── __init__.py
│   │   ├── user.py                    # User schemas
│   │   ├── transaction.py             # Transaction schemas
│   │   ├── jar.py                     # Jar schemas
│   │   ├── goal.py                    # Goal schemas
│   │   ├── alert.py                   # Alert schemas
│   │   └── prediction.py              # Prediction schemas
│   │
│   ├── api/                           # API route handlers
│   │   ├── __init__.py
│   │   ├── auth.py                    # Authentication endpoints
│   │   ├── transactions.py            # Transaction endpoints
│   │   ├── jars.py                    # Jar endpoints
│   │   ├── goals.py                   # Goal endpoints
│   │   ├── alerts.py                  # Alert endpoints
│   │   ├── predictions.py             # Prediction endpoints
│   │   ├── coach.py                   # AI Coach endpoints
│   │   ├── insights.py                # Insights endpoints
│   │   └── dashboard.py               # Dashboard endpoints
│   │
│   ├── ml/                            # Machine Learning models
│   │   ├── __init__.py
│   │   ├── income_predictor.py        # Income prediction model
│   │   ├── category_detector.py       # Auto-categorization model
│   │   ├── cashflow_analyzer.py       # Cashflow analysis model
│   │   ├── pattern_analyzer.py        # Pattern analysis model
│   │   └── budget_optimizer.py        # Budget optimization model
│   │
│   ├── agents/                        # Multi-agent system
│   │   ├── __init__.py
│   │   ├── router_agent.py            # Intent classification
│   │   ├── income_agent.py            # Income prediction agent
│   │   ├── spending_agent.py          # Spending analysis agent
│   │   ├── goal_agent.py              # Goal planning agent
│   │   ├── alert_engine.py            # Alert generation engine
│   │   └── coach_agent.py             # AI Coach agent
│   │
│   └── utils/                         # Utility functions
│       ├── __init__.py
│       ├── auth.py                    # JWT & password utilities
│       ├── sms_parser.py              # SMS parsing for 5 banks
│       ├── jar_logic.py               # Jar allocation logic
│       ├── openai_client.py           # OpenAI integration
│       └── helpers.py                 # Helper functions
│
├── run.py                             # Application entry point
├── requirements.txt                   # Python dependencies
├── .env.example                       # Environment variables template
└── README.md                          # Backend README
```

---

## 🎨 Frontend Directory Structure

### Location: `/home/code/finpilot-frontend`

```
finpilot-frontend/
├── app/                               # Next.js app directory
│   ├── layout.tsx                     # Root layout
│   ├── page.tsx                       # Dashboard page
│   ├── globals.css                    # Global styles
│   │
│   ├── transactions/
│   │   └── page.tsx                   # Transactions page
│   │
│   ├── jars/
│   │   └── page.tsx                   # Money Jars page
│   │
│   ├── goals/
│   │   └── page.tsx                   # Savings Goals page
│   │
│   ├── coach/
│   │   └── page.tsx                   # AI Coach page
│   │
│   └── api/                           # API routes (if needed)
│       └── [...].ts                   # API route handlers
│
├── components/                        # Reusable React components
│   ├── ui/                            # shadcn/ui components
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── input.tsx
│   │   ├── badge.tsx
│   │   ├── progress.tsx
│   │   └── [other components]
│   │
│   ├── BalanceCard.tsx                # Balance display component
│   ├── TransactionCard.tsx            # Transaction card component
│   ├── JarCard.tsx                    # Jar card component
│   ├── GoalCard.tsx                   # Goal card component
│   ├── AlertCard.tsx                  # Alert card component
│   ├── Navigation.tsx                 # Bottom navigation
│   ├── LoadingSpinner.tsx             # Loading state
│   ├── IncomeChart.tsx                # Income visualization
│   └── [other components]
│
├── hooks/                             # Custom React hooks
│   ├── useTransactions.ts             # Transactions data fetching
│   ├── useJars.ts                     # Jars data fetching
│   ├── useGoals.ts                    # Goals data fetching
│   ├── useAlerts.ts                   # Alerts data fetching
│   ├── usePredictions.ts              # Predictions data fetching
│   └── useToast.ts                    # Toast notifications
│
├── lib/                               # Utility functions
│   ├── api.ts                         # Axios API client
│   ├── utils.ts                       # Helper functions
│   └── constants.ts                   # Constants
│
├── public/                            # Static assets
│   ├── logo.png
│   ├── icons/
│   └── [other assets]
│
├── styles/                            # Additional styles
│   └── globals.css                    # Global Tailwind styles
│
├── package.json                       # NPM dependencies
├── tsconfig.json                      # TypeScript configuration
├── tailwind.config.ts                 # Tailwind CSS configuration
├── next.config.ts                     # Next.js configuration
├── .env.local.example                 # Environment variables template
└── README.md                          # Frontend README
```

---

## 📄 Documentation Files

### Location: `/home/code`

| File | Purpose | Size |
|------|---------|------|
| **FINAL_SUMMARY.md** | Complete project delivery summary | ~15 KB |
| **PROJECT_SUMMARY.md** | Comprehensive project overview | ~12 KB |
| **IMPLEMENTATION_GUIDE.md** | Step-by-step implementation roadmap | ~18 KB |
| **FINPILOT_STATUS.md** | Build status and feature matrix | ~10 KB |
| **FILES_AND_LOCATIONS.md** | This file - complete file structure | ~8 KB |

---

## 🗄️ Database Schema

### Location: `/home/code/finpilot/backend/app/models`

**7 Tables**:

1. **users** - User authentication and profile
   - id, email, password_hash, name, phone, created_at, updated_at

2. **transactions** - Income/expense records
   - id, user_id, amount, type, category, description, date, confidence, created_at

3. **jars** - Virtual money containers
   - id, user_id, name, target_amount, current_amount, priority, deadline, created_at

4. **goals** - Savings goals
   - id, user_id, name, target_amount, current_amount, deadline, status, created_at

5. **alerts** - Proactive notifications
   - id, user_id, type, message, severity, triggered_at, user_response, created_at

6. **user_interactions** - Behavioral learning
   - id, user_id, interaction_type, data, created_at

7. **predictions** - ML accuracy tracking
   - id, user_id, prediction_type, predicted_value, actual_value, confidence, created_at

---

## 🔌 API Endpoints

### Location: `/home/code/finpilot/backend/app/api`

**30+ Endpoints organized by module**:

#### Authentication (`/auth`)
- POST `/auth/register` - User registration
- POST `/auth/login` - User login
- POST `/auth/refresh` - Refresh token
- GET `/auth/me` - Get current user

#### Transactions (`/transactions`)
- GET `/transactions` - List transactions
- POST `/transactions` - Create transaction
- GET `/transactions/{id}` - Get transaction
- PUT `/transactions/{id}` - Update transaction
- DELETE `/transactions/{id}` - Delete transaction
- POST `/transactions/categorize` - Auto-categorize
- POST `/transactions/bulk-upload` - Bulk upload

#### Jars (`/jars`)
- GET `/jars` - List jars
- POST `/jars` - Create jar
- GET `/jars/{id}` - Get jar
- PUT `/jars/{id}` - Update jar
- DELETE `/jars/{id}` - Delete jar
- POST `/jars/{id}/allocate` - Allocate money
- GET `/jars/recommendations` - Get recommendations
- GET `/jars/{id}/progress` - Get progress

#### Goals (`/goals`)
- GET `/goals` - List goals
- POST `/goals` - Create goal
- GET `/goals/{id}` - Get goal
- PUT `/goals/{id}` - Update goal
- DELETE `/goals/{id}` - Delete goal
- POST `/goals/{id}/plan` - Plan goal
- GET `/goals/{id}/progress` - Get progress

#### Predictions (`/predict`)
- GET `/predict/income` - Income prediction
- GET `/predict/expense` - Expense prediction
- GET `/predict/cashflow` - Cashflow analysis
- GET `/predict/safe-to-spend` - Safe to spend

#### Alerts (`/alerts`)
- GET `/alerts` - List alerts
- POST `/alerts` - Create alert
- GET `/alerts/{id}` - Get alert
- PUT `/alerts/{id}/respond` - Respond to alert
- GET `/alerts/history` - Alert history

#### Coach (`/coach`)
- POST `/coach/query` - Query AI coach
- GET `/coach/history` - Chat history

#### Insights (`/insights`)
- GET `/insights/predictions` - Prediction insights
- GET `/insights/patterns` - Spending patterns
- GET `/insights/optimizations` - Budget optimizations
- GET `/insights/categories` - Category analysis

#### Dashboard (`/dashboard`)
- GET `/dashboard` - Dashboard data
- GET `/dashboard/summary` - Summary data

---

## 🤖 ML Models

### Location: `/home/code/finpilot/backend/app/ml`

| Model | File | Purpose |
|-------|------|---------|
| **Income Predictor** | `income_predictor.py` | 7/30/90 day forecasts |
| **Category Detector** | `category_detector.py` | Auto-categorization |
| **Cashflow Analyzer** | `cashflow_analyzer.py` | Runout prediction |
| **Pattern Analyzer** | `pattern_analyzer.py` | Spending patterns |
| **Budget Optimizer** | `budget_optimizer.py` | Savings suggestions |

---

## 🧠 Multi-Agent System

### Location: `/home/code/finpilot/backend/app/agents`

| Agent | File | Purpose |
|-------|------|---------|
| **Router Agent** | `router_agent.py` | Intent classification |
| **Income Agent** | `income_agent.py` | Income prediction |
| **Spending Agent** | `spending_agent.py` | Spending analysis |
| **Goal Agent** | `goal_agent.py` | Goal planning |
| **Alert Engine** | `alert_engine.py` | Alert generation |
| **Coach Agent** | `coach_agent.py` | AI Coach responses |

---

## 🛠️ Utility Functions

### Location: `/home/code/finpilot/backend/app/utils`

| Utility | File | Purpose |
|---------|------|---------|
| **Auth Utils** | `auth.py` | JWT, password hashing |
| **SMS Parser** | `sms_parser.py` | Parse SMS from 5 banks |
| **Jar Logic** | `jar_logic.py` | Auto-allocation logic |
| **OpenAI Client** | `openai_client.py` | OpenAI integration |
| **Helpers** | `helpers.py` | General helpers |

---

## 📦 Dependencies

### Backend Dependencies
**File**: `/home/code/finpilot/backend/requirements.txt`

```
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
pydantic==2.5.0
pydantic-settings==2.1.0
python-jose==3.3.0
passlib==1.7.4
bcrypt==4.1.1
python-multipart==0.0.6
scikit-learn==1.3.2
pandas==2.1.3
numpy==1.26.2
statsmodels==0.14.0
openai==1.3.5
requests==2.31.0
python-dotenv==1.0.0
cors==1.0.1
```

### Frontend Dependencies
**File**: `/home/code/finpilot-frontend/package.json`

```json
{
  "dependencies": {
    "next": "15.5.6",
    "react": "19.0.0-rc-66855b96-20241106",
    "react-dom": "19.0.0-rc-66855b96-20241106",
    "@radix-ui/react-slot": "^2.0.2",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.0.0",
    "lucide-react": "^0.263.1",
    "next-themes": "^0.2.1",
    "tailwind-merge": "^2.2.0",
    "tailwindcss-animate": "^1.0.6",
    "axios": "^1.6.0",
    "recharts": "^2.10.0",
    "@tanstack/react-query": "^5.0.0"
  },
  "devDependencies": {
    "typescript": "^5.3.3",
    "tailwindcss": "^3.3.6",
    "postcss": "^8.4.31",
    "autoprefixer": "^10.4.16"
  }
}
```

---

## 🔐 Environment Variables

### Backend
**File**: `/home/code/finpilot/backend/.env`

```
DATABASE_URL=postgresql://user:password@localhost:5432/finpilot
JWT_SECRET=your-secret-key-here
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
OPENAI_API_KEY=sk-...
ALLOWED_ORIGINS=http://localhost:3000,https://finpilot.vercel.app
DEBUG=False
```

### Frontend
**File**: `/home/code/finpilot-frontend/.env.local`

```
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_APP_NAME=FinPilot
```

---

## 🚀 Running the Application

### Backend
```bash
cd /home/code/finpilot/backend
python run.py
# Runs on http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Frontend
```bash
cd /home/code/finpilot-frontend
npm run dev
# Runs on http://localhost:3000
```

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| Total Files | 150+ |
| Backend Code | ~2,500 lines |
| Frontend Code | ~1,200 lines |
| Documentation | ~60 KB |
| Database Tables | 7 |
| API Endpoints | 30+ |
| ML Models | 5 |
| Agents | 6 |
| Components | 20+ |
| Hooks | 6+ |
| Utilities | 5+ |

---

## 🔗 Important URLs

| Resource | URL |
|----------|-----|
| GitHub Repository | https://github.com/UnknownDeveloper2k24/FinCoach-AI-V2 |
| Backend API | http://localhost:8000 |
| API Documentation | http://localhost:8000/docs |
| Frontend | http://localhost:3000 |
| Public URL | https://finpilot.lindy.site |

---

## 📝 File Naming Conventions

### Backend
- **Models**: `snake_case.py` (e.g., `user.py`, `transaction.py`)
- **Classes**: `PascalCase` (e.g., `User`, `Transaction`)
- **Functions**: `snake_case` (e.g., `get_user()`, `create_transaction()`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`, `DEFAULT_TIMEOUT`)

### Frontend
- **Components**: `PascalCase.tsx` (e.g., `BalanceCard.tsx`)
- **Pages**: `page.tsx` in directory (e.g., `app/transactions/page.tsx`)
- **Hooks**: `useXxx.ts` (e.g., `useTransactions.ts`)
- **Utilities**: `snake_case.ts` (e.g., `api.ts`, `helpers.ts`)

---

## 🔄 Git Repository Structure

```
GitHub: UnknownDeveloper2k24/FinCoach-AI-V2
├── main branch
│   ├── finpilot/
│   ├── finpilot-frontend/
│   ├── README.md
│   ├── requirements.txt
│   └── [documentation files]
└── [other branches as needed]
```

---

## 📋 Quick Reference

### Start Development
```bash
# Terminal 1: Backend
cd /home/code/finpilot/backend && python run.py

# Terminal 2: Frontend
cd /home/code/finpilot-frontend && npm run dev
```

### View Documentation
- **Project Overview**: `/home/code/FINAL_SUMMARY.md`
- **Implementation Guide**: `/home/code/IMPLEMENTATION_GUIDE.md`
- **Build Status**: `/home/code/FINPILOT_STATUS.md`
- **Project Summary**: `/home/code/PROJECT_SUMMARY.md`

### Access Services
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Frontend**: http://localhost:3000

---

**Last Updated**: November 25, 2025, 11:30 PM IST
**Project Status**: 60% Complete
**Next Milestone**: Frontend-Backend Integration

