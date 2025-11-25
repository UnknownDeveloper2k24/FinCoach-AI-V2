# FinPilot - AI-Powered Financial OS

A premium CRED-like financial operating system for gig workers and freelancers, powered by multi-agent AI architecture.

## 🎯 Overview

FinPilot is a complete financial management platform that combines:
- **Real-time Income & Expense Tracking** with auto-categorization
- **AI-Powered Predictions** for income forecasting and spending patterns
- **Smart Money Jars** for automated savings allocation
- **Intelligent Alerts** with adaptive learning
- **AI Coach** for personalized financial guidance
- **CRED-like UI** with minimal, premium design

## 🏗️ Architecture

### Backend (FastAPI + Python)
- **Framework**: FastAPI with async support
- **Database**: PostgreSQL with SQLAlchemy ORM
- **ML Models**: scikit-learn, pandas, statsmodels
- **Authentication**: JWT-based with refresh tokens
- **Multi-Agent System**: 10 specialized financial agents

### Frontend (Next.js 15 + React)
- **Framework**: Next.js 15.5.6 with TypeScript
- **UI Components**: shadcn/ui + Tailwind CSS
- **Design**: Mobile-first, CRED-inspired
- **State Management**: React hooks + Context API

## 📁 Project Structure

```
finpilot/
├── backend/
│   ├── app/
│   │   ├── models/          # SQLAlchemy models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── api/             # API routes
│   │   ├── ml/              # ML models & algorithms
│   │   ├── agents/          # Multi-agent system
│   │   ├── utils/           # Utilities (auth, SMS parsing, etc)
│   │   ├── config.py        # Configuration
│   │   ├── database.py      # Database setup
│   │   └── main.py          # FastAPI app
│   ├── venv/                # Python virtual environment
│   ├── requirements.txt     # Python dependencies
│   └── run.py              # Entry point
│
└── finpilot-frontend/
    ├── app/
    │   ├── page.tsx         # Dashboard
    │   ├── transactions/    # Transactions page
    │   ├── jars/           # Money jars page
    │   ├── goals/          # Savings goals page
    │   ├── coach/          # AI coach page
    │   └── layout.tsx      # Root layout
    ├── components/
    │   └── navigation.tsx   # Bottom navigation
    ├── public/             # Static assets
    └── package.json        # Node dependencies
```

## 🚀 Getting Started

### Backend Setup

```bash
cd finpilot/backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start server
python run.py
```

Backend runs on `http://localhost:8000`
API docs available at `http://localhost:8000/docs`

### Frontend Setup

```bash
cd finpilot-frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

Frontend runs on `http://localhost:3000`

## 📊 Core Features

### 1. **Income Prediction Agent**
- 7/30/90 day forecasts
- Confidence scoring (0-100%)
- Trend detection (increasing/decreasing/stable)
- Daily breakdown

### 2. **Cashflow Agent**
- Daily safe-to-spend calculation
- Runout prediction with risk levels
- Emergency fund recommendations

### 3. **Jar System Agent**
- Auto-allocation based on priority
- 4 default jars: Rent, Bills, Emergency, Savings
- Custom jar creation
- Progress tracking

### 4. **UPI/Bank SMS Parsing Agent**
- Supports 5+ Indian banks (HDFC, ICICI, SBI, etc)
- Auto-categorization from merchant names
- Confidence scoring

### 5. **Spending Pattern Agent**
- Category-wise analysis
- Peak day detection
- Anomaly detection
- Trend analysis

### 6. **Budget Optimization Agent**
- Category-wise reduction suggestions
- Savings potential calculation
- Priority-based recommendations

### 7. **Goal Planning Agent**
- Feasibility checks
- Monthly savings calculation
- Milestone tracking
- On-track status

### 8. **Alert Engine**
- 6 alert types with adaptive triggers
- User response tracking
- Learning from interactions

### 9. **AI Coach Agent**
- Intent classification
- Context-aware responses
- Financial reasoning
- Action recommendations

### 10. **Asset Management Agent**
- Investment tracking
- Portfolio analysis
- Market forecasting

## 🗄️ Database Schema

### Users
- id, email, name, phone, occupation
- hashed_password, created_at

### Transactions
- id, user_id, date, amount, type (income/expense)
- category, description, auto_categorized, confidence

### Jars
- id, user_id, name, target_amount, current_amount
- priority, deadline, color, created_at

### Goals
- id, user_id, name, target_amount, current_amount
- deadline, monthly_savings_needed, status

### Alerts
- id, user_id, type, severity, message, suggestion
- active, dismissed_at, user_action, created_at

### UserInteractions
- id, user_id, alert_id, action, timestamp

### Predictions
- id, user_id, prediction_type, period
- predicted_value, confidence, actual_value, created_at

## 🔌 API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `GET /auth/me` - Get current user

### Transactions
- `POST /transactions` - Create transaction
- `GET /transactions` - List transactions
- `GET /transactions/{id}` - Get transaction
- `PUT /transactions/{id}` - Update transaction
- `DELETE /transactions/{id}` - Delete transaction

### Jars
- `POST /jars` - Create jar
- `GET /jars` - List jars
- `GET /jars/{id}` - Get jar
- `PUT /jars/{id}` - Update jar
- `POST /jars/{id}/allocate` - Allocate money

### Goals
- `POST /goals` - Create goal
- `GET /goals` - List goals
- `GET /goals/{id}` - Get goal
- `PUT /goals/{id}` - Update goal
- `DELETE /goals/{id}` - Delete goal

### Predictions
- `GET /predict/income/weekly` - Weekly income prediction
- `GET /predict/income/monthly` - Monthly income prediction
- `GET /predict/cashflow/runout` - Runout prediction
- `GET /predict/safe-to-spend` - Safe to spend calculation

### Insights
- `GET /insights/patterns` - Spending patterns
- `GET /insights/optimizations` - Budget optimizations
- `GET /insights/dashboard` - Dashboard data

### Alerts
- `POST /alerts` - Create alert
- `GET /alerts` - List alerts
- `PUT /alerts/{id}` - Update alert
- `DELETE /alerts/{id}` - Delete alert

## 🎨 UI/UX Design Principles

### CRED-like Aesthetics
- Minimal, premium design
- Mobile-first approach
- Cards and tiles layout
- Clear typography hierarchy
- Intentional whitespace

### No AI Tone
- No apologies or filler text
- No "As an AI" language
- Direct, actionable insights
- Professional tone

### Silent Intelligence
- High-signal insights only
- Time-critical alerts
- Confidence scoring on all predictions
- Range and impact indicators

### Action-First
- Always 2-4 clear, tappable actions
- Primary and secondary actions
- Contextual recommendations

## 🔐 Security

- JWT authentication with refresh tokens
- Password hashing with bcrypt
- CORS protection
- SQL injection prevention via SQLAlchemy ORM
- Environment-based configuration

## 📈 ML Models

### Income Prediction
- Time-series analysis with trend detection
- Confidence scoring based on data consistency
- 7/30/90 day forecasts

### Category Detection
- Keyword-based merchant matching
- Confidence scoring
- Alternative suggestions

### Spending Pattern Analysis
- Frequency analysis
- Peak day detection
- Anomaly detection (3-sigma rule)
- Trend analysis

### Budget Optimization
- Category-wise spending analysis
- Reduction suggestions (30% for discretionary)
- Savings potential calculation

## 🚀 Deployment

### Backend
```bash
# Using Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app.main:app
```

### Frontend
```bash
# Build for production
npm run build
npm start
```

## 📝 Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql://user:password@localhost:5432/finpilot
JWT_SECRET=your-secret-key
OPENAI_API_KEY=your-api-key
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

MIT License - see LICENSE file for details

## 👨‍💻 Author

Built with ❤️ for gig workers and freelancers

## 🔗 Links

- **GitHub**: https://github.com/UnknownDeveloper2k24/FinCoach-AI-V2
- **Live Demo**: https://finpilot.lindy.site
- **API Docs**: http://localhost:8000/docs

---

**FinPilot** - Your AI-powered financial operating system
