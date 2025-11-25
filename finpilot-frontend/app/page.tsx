'use client';

import { useAuth } from '@/lib/auth-context';
import { ProtectedRoute } from '@/lib/protected-route';
import { useDashboard, useJars, useAlerts, useIncomePrediction } from '@/lib/hooks';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { ArrowUpRight, ArrowDownLeft, TrendingUp, AlertCircle } from 'lucide-react';
import Link from 'next/link';

function DashboardContent() {
  const { user } = useAuth();
  const { data: dashboard, loading: dashboardLoading } = useDashboard();
  const { data: jars } = useJars();
  const { data: alerts } = useAlerts();
  const { data: incomePrediction } = useIncomePrediction('weekly');

  if (dashboardLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 pb-24">
      {/* Header */}
      <div className="bg-white border-b sticky top-0 z-10">
        <div className="max-w-md mx-auto px-4 py-4">
          <h1 className="text-2xl font-bold">Welcome, {user?.name || 'User'}! 👋</h1>
          <p className="text-gray-600 text-sm">Your financial overview</p>
        </div>
      </div>

      <div className="max-w-md mx-auto px-4 py-6 space-y-6">
        {/* Balance Card */}
        <Card className="bg-gradient-to-br from-blue-600 to-blue-700 text-white border-0">
          <CardContent className="pt-6">
            <p className="text-sm opacity-90">Current Balance</p>
            <h2 className="text-4xl font-bold mt-2">
              ₹{dashboard?.balance?.toLocaleString('en-IN') || '0'}
            </h2>
            <p className="text-sm opacity-75 mt-4">
              Safe to spend today: ₹{dashboard?.safe_to_spend?.toLocaleString('en-IN') || '0'}
            </p>
          </CardContent>
        </Card>

        {/* Quick Stats */}
        <div className="grid grid-cols-2 gap-4">
          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-xs text-gray-600">This Month Income</p>
                  <p className="text-xl font-bold mt-1">
                    ₹{dashboard?.monthly_income?.toLocaleString('en-IN') || '0'}
                  </p>
                </div>
                <ArrowUpRight className="text-green-600" size={24} />
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-xs text-gray-600">This Month Spent</p>
                  <p className="text-xl font-bold mt-1">
                    ₹{dashboard?.monthly_spent?.toLocaleString('en-IN') || '0'}
                  </p>
                </div>
                <ArrowDownLeft className="text-red-600" size={24} />
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Income Prediction */}
        {incomePrediction && (
          <Card>
            <CardHeader>
              <CardTitle className="text-lg flex items-center gap-2">
                <TrendingUp size={20} />
                Next Week Prediction
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-2">
              <div className="flex justify-between items-center">
                <span className="text-gray-600">Predicted Income</span>
                <span className="font-bold">₹{incomePrediction.predicted_amount?.toLocaleString('en-IN') || '0'}</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-gray-600">Confidence</span>
                <span className="font-bold">{(incomePrediction.confidence * 100).toFixed(0)}%</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2 mt-2">
                <div
                  className="bg-blue-600 h-2 rounded-full"
                  style={{ width: `${(incomePrediction.confidence * 100)}%` }}
                ></div>
              </div>
            </CardContent>
          </Card>
        )}

        {/* Jars Overview */}
        {jars && jars.length > 0 && (
          <Card>
            <CardHeader>
              <CardTitle className="text-lg">Your Jars</CardTitle>
              <CardDescription>Money allocated to priorities</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              {jars.slice(0, 3).map((jar: any) => (
                <div key={jar.id}>
                  <div className="flex justify-between items-center mb-2">
                    <span className="font-medium">{jar.name}</span>
                    <span className="text-sm font-bold">
                      ₹{jar.current_amount?.toLocaleString('en-IN') || '0'} / ₹{jar.target_amount?.toLocaleString('en-IN') || '0'}
                    </span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div
                      className={`h-2 rounded-full ${jar.color || 'bg-blue-600'}`}
                      style={{
                        width: `${Math.min((jar.current_amount / jar.target_amount) * 100, 100)}%`,
                      }}
                    ></div>
                  </div>
                </div>
              ))}
              <Link href="/jars">
                <Button variant="outline" className="w-full mt-4">
                  View All Jars
                </Button>
              </Link>
            </CardContent>
          </Card>
        )}

        {/* Alerts */}
        {alerts && alerts.length > 0 && (
          <Card className="border-orange-200 bg-orange-50">
            <CardHeader>
              <CardTitle className="text-lg flex items-center gap-2 text-orange-900">
                <AlertCircle size={20} />
                Active Alerts
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-3">
              {alerts.slice(0, 2).map((alert: any) => (
                <div key={alert.id} className="p-3 bg-white rounded border border-orange-200">
                  <p className="font-medium text-sm">{alert.message}</p>
                  {alert.suggestion && (
                    <p className="text-xs text-gray-600 mt-1">💡 {alert.suggestion}</p>
                  )}
                </div>
              ))}
            </CardContent>
          </Card>
        )}

        {/* Quick Actions */}
        <div className="grid grid-cols-2 gap-3">
          <Link href="/transactions">
            <Button variant="outline" className="w-full">
              Add Transaction
            </Button>
          </Link>
          <Link href="/coach">
            <Button className="w-full">
              Ask Coach
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default function Home() {
  return (
    <ProtectedRoute>
      <DashboardContent />
    </ProtectedRoute>
  );
}
