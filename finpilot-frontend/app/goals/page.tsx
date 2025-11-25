'use client';

import { useState } from 'react';
import { useAuth } from '@/lib/auth-context';
import { ProtectedRoute } from '@/lib/protected-route';
import { useGoals, useCreateGoal, useGoalProgress, useDeleteGoal } from '@/lib/hooks';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Plus, Trash2, Target } from 'lucide-react';

function GoalsContent() {
  const { user } = useAuth();
  const { data: goals, loading, refetch } = useGoals();
  const { mutate: createGoal, loading: creating } = useCreateGoal({
    onSuccess: () => {
      setFormData({ name: '', target_amount: '', deadline: '' });
      refetch();
    },
  });
  const { mutate: deleteGoal } = useDeleteGoal(0, {
    onSuccess: () => refetch(),
  });

  const [formData, setFormData] = useState({
    name: '',
    target_amount: '',
    deadline: '',
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.name || !formData.target_amount || !formData.deadline) {
      alert('Please fill in all fields');
      return;
    }
    await createGoal({
      ...formData,
      target_amount: parseFloat(formData.target_amount),
    });
  };

  const handleDelete = async (id: number) => {
    if (confirm('Are you sure you want to delete this goal?')) {
      await deleteGoal();
    }
  };

  if (loading) {
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
          <h1 className="text-2xl font-bold">Financial Goals</h1>
          <p className="text-gray-600 text-sm">Plan and track your goals</p>
        </div>
      </div>

      <div className="max-w-md mx-auto px-4 py-6 space-y-6">
        {/* Create Goal Form */}
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Set New Goal</CardTitle>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="text-sm font-medium">Goal Name</label>
                <Input
                  placeholder="e.g., Buy a Laptop"
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  className="mt-1"
                />
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="text-sm font-medium">Target Amount</label>
                  <Input
                    type="number"
                    placeholder="0"
                    value={formData.target_amount}
                    onChange={(e) => setFormData({ ...formData, target_amount: e.target.value })}
                    className="mt-1"
                  />
                </div>
                <div>
                  <label className="text-sm font-medium">Deadline</label>
                  <Input
                    type="date"
                    value={formData.deadline}
                    onChange={(e) => setFormData({ ...formData, deadline: e.target.value })}
                    className="mt-1"
                  />
                </div>
              </div>

              <Button type="submit" className="w-full" disabled={creating}>
                <Plus size={18} className="mr-2" />
                {creating ? 'Creating...' : 'Create Goal'}
              </Button>
            </form>
          </CardContent>
        </Card>

        {/* Goals List */}
        <div>
          <h2 className="text-lg font-bold mb-4">Your Goals</h2>
          {goals && goals.length > 0 ? (
            <div className="space-y-4">
              {goals.map((goal: any) => {
                const daysLeft = Math.ceil(
                  (new Date(goal.deadline).getTime() - new Date().getTime()) / (1000 * 60 * 60 * 24)
                );
                const progress = (goal.current_amount / goal.target_amount) * 100;
                const monthlyRequired = goal.target_amount / Math.max(daysLeft / 30, 1);

                return (
                  <Card key={goal.id}>
                    <CardContent className="pt-6 space-y-4">
                      <div className="flex items-start justify-between">
                        <div className="flex-1">
                          <div className="flex items-center gap-2 mb-1">
                            <Target size={18} className="text-blue-600" />
                            <h3 className="font-bold">{goal.name}</h3>
                          </div>
                          <p className="text-xs text-gray-600">
                            {daysLeft > 0 ? `${daysLeft} days left` : 'Deadline passed'}
                          </p>
                        </div>
                        <Button
                          variant="ghost"
                          size="sm"
                          onClick={() => handleDelete(goal.id)}
                        >
                          <Trash2 size={16} className="text-red-600" />
                        </Button>
                      </div>

                      {/* Progress */}
                      <div>
                        <div className="flex justify-between text-sm mb-2">
                          <span>₹{goal.current_amount?.toLocaleString('en-IN') || '0'}</span>
                          <span className="text-gray-600">₹{goal.target_amount?.toLocaleString('en-IN') || '0'}</span>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-3">
                          <div
                            className="h-3 rounded-full bg-blue-600"
                            style={{ width: `${Math.min(progress, 100)}%` }}
                          ></div>
                        </div>
                        <p className="text-xs text-gray-600 mt-1">{Math.round(progress)}% complete</p>
                      </div>

                      {/* Monthly Target */}
                      <div className="bg-blue-50 p-3 rounded border border-blue-200">
                        <p className="text-xs text-gray-600">Monthly target to reach goal</p>
                        <p className="text-lg font-bold text-blue-600">
                          ₹{monthlyRequired.toLocaleString('en-IN', { maximumFractionDigits: 0 })}
                        </p>
                      </div>

                      {/* Status */}
                      {progress >= 100 ? (
                        <div className="bg-green-50 p-3 rounded border border-green-200">
                          <p className="text-sm font-semibold text-green-700">✅ Goal Achieved!</p>
                        </div>
                      ) : daysLeft <= 0 ? (
                        <div className="bg-red-50 p-3 rounded border border-red-200">
                          <p className="text-sm font-semibold text-red-700">⚠️ Deadline Passed</p>
                        </div>
                      ) : (
                        <div className="bg-yellow-50 p-3 rounded border border-yellow-200">
                          <p className="text-sm text-yellow-700">
                            On track: {((progress / (100 * (daysLeft / 30))) * 100).toFixed(0)}% of monthly target
                          </p>
                        </div>
                      )}
                    </CardContent>
                  </Card>
                );
              })}
            </div>
          ) : (
            <Card>
              <CardContent className="pt-6 text-center">
                <p className="text-gray-600">No goals yet. Set one to start planning!</p>
              </CardContent>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
}

export default function GoalsPage() {
  return (
    <ProtectedRoute>
      <GoalsContent />
    </ProtectedRoute>
  );
}
