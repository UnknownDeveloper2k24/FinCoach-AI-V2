'use client';

import { useState } from 'react';
import { useAuth } from '@/lib/auth-context';
import { ProtectedRoute } from '@/lib/protected-route';
import { useJars, useCreateJar, useAllocateToJar, useJarRecommendations } from '@/lib/hooks';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Plus, Lightbulb } from 'lucide-react';

const JAR_COLORS = [
  { name: 'Blue', value: 'bg-blue-600' },
  { name: 'Green', value: 'bg-green-600' },
  { name: 'Purple', value: 'bg-purple-600' },
  { name: 'Pink', value: 'bg-pink-600' },
  { name: 'Orange', value: 'bg-orange-600' },
  { name: 'Red', value: 'bg-red-600' },
];

function JarsContent() {
  const { user } = useAuth();
  const { data: jars, loading, refetch } = useJars();
  const { data: recommendations } = useJarRecommendations();
  const { mutate: createJar, loading: creating } = useCreateJar({
    onSuccess: () => {
      setFormData({ name: '', target_amount: '', priority: '1', deadline: '', color: 'bg-blue-600' });
      refetch();
    },
  });
  const { mutate: allocateToJar } = useAllocateToJar(0, {
    onSuccess: () => refetch(),
  });

  const [formData, setFormData] = useState({
    name: '',
    target_amount: '',
    priority: '1',
    deadline: '',
    color: 'bg-blue-600',
  });

  const [allocateData, setAllocateData] = useState<{ [key: number]: string }>({});

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.name || !formData.target_amount) {
      alert('Please fill in all required fields');
      return;
    }
    await createJar({
      ...formData,
      target_amount: parseFloat(formData.target_amount),
      priority: parseInt(formData.priority),
    });
  };

  const handleAllocate = async (jarId: number) => {
    const amount = allocateData[jarId];
    if (!amount) {
      alert('Please enter an amount');
      return;
    }
    await allocateToJar({ amount: parseFloat(amount) });
    setAllocateData({ ...allocateData, [jarId]: '' });
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
          <h1 className="text-2xl font-bold">Smart Jars</h1>
          <p className="text-gray-600 text-sm">Allocate money to priorities</p>
        </div>
      </div>

      <div className="max-w-md mx-auto px-4 py-6 space-y-6">
        {/* Create Jar Form */}
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Create New Jar</CardTitle>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="text-sm font-medium">Jar Name</label>
                <Input
                  placeholder="e.g., Emergency Fund"
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
                  <label className="text-sm font-medium">Priority</label>
                  <select
                    value={formData.priority}
                    onChange={(e) => setFormData({ ...formData, priority: e.target.value })}
                    className="mt-1 w-full px-3 py-2 border rounded-md"
                  >
                    {[1, 2, 3, 4, 5].map((p) => (
                      <option key={p} value={p}>
                        {p === 1 ? 'High' : p === 2 ? 'Medium-High' : p === 3 ? 'Medium' : p === 4 ? 'Medium-Low' : 'Low'}
                      </option>
                    ))}
                  </select>
                </div>
              </div>

              <div>
                <label className="text-sm font-medium">Deadline (optional)</label>
                <Input
                  type="date"
                  value={formData.deadline}
                  onChange={(e) => setFormData({ ...formData, deadline: e.target.value })}
                  className="mt-1"
                />
              </div>

              <div>
                <label className="text-sm font-medium">Color</label>
                <div className="grid grid-cols-6 gap-2 mt-2">
                  {JAR_COLORS.map((color) => (
                    <button
                      key={color.value}
                      type="button"
                      onClick={() => setFormData({ ...formData, color: color.value })}
                      className={`w-full h-10 rounded-lg ${color.value} ${
                        formData.color === color.value ? 'ring-2 ring-offset-2 ring-gray-400' : ''
                      }`}
                      title={color.name}
                    />
                  ))}
                </div>
              </div>

              <Button type="submit" className="w-full" disabled={creating}>
                <Plus size={18} className="mr-2" />
                {creating ? 'Creating...' : 'Create Jar'}
              </Button>
            </form>
          </CardContent>
        </Card>

        {/* Recommendations */}
        {recommendations && recommendations.length > 0 && (
          <Card className="border-blue-200 bg-blue-50">
            <CardHeader>
              <CardTitle className="text-lg flex items-center gap-2">
                <Lightbulb size={20} className="text-blue-600" />
                Recommendations
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-2">
              {recommendations.map((rec: any, idx: number) => (
                <p key={idx} className="text-sm text-blue-900">
                  💡 {rec}
                </p>
              ))}
            </CardContent>
          </Card>
        )}

        {/* Jars List */}
        <div>
          <h2 className="text-lg font-bold mb-4">Your Jars</h2>
          {jars && jars.length > 0 ? (
            <div className="space-y-4">
              {jars.map((jar: any) => {
                const progress = (jar.current_amount / jar.target_amount) * 100;
                return (
                  <Card key={jar.id}>
                    <CardContent className="pt-6 space-y-4">
                      <div>
                        <div className="flex justify-between items-center mb-2">
                          <h3 className="font-bold">{jar.name}</h3>
                          <span className="text-sm text-gray-600">Priority: {jar.priority}</span>
                        </div>
                        <div className="flex justify-between text-sm mb-2">
                          <span>₹{jar.current_amount?.toLocaleString('en-IN') || '0'}</span>
                          <span className="text-gray-600">₹{jar.target_amount?.toLocaleString('en-IN') || '0'}</span>
                        </div>
                        <div className="w-full bg-gray-200 rounded-full h-3">
                          <div
                            className={`h-3 rounded-full ${jar.color || 'bg-blue-600'}`}
                            style={{ width: `${Math.min(progress, 100)}%` }}
                          ></div>
                        </div>
                        <p className="text-xs text-gray-600 mt-1">{Math.round(progress)}% complete</p>
                      </div>

                      {/* Allocate Section */}
                      <div className="flex gap-2">
                        <Input
                          type="number"
                          placeholder="Amount to add"
                          value={allocateData[jar.id] || ''}
                          onChange={(e) => setAllocateData({ ...allocateData, [jar.id]: e.target.value })}
                          className="flex-1"
                        />
                        <Button
                          onClick={() => handleAllocate(jar.id)}
                          size="sm"
                          className="px-4"
                        >
                          Add
                        </Button>
                      </div>

                      {jar.deadline && (
                        <p className="text-xs text-gray-600">
                          Deadline: {new Date(jar.deadline).toLocaleDateString()}
                        </p>
                      )}
                    </CardContent>
                  </Card>
                );
              })}
            </div>
          ) : (
            <Card>
              <CardContent className="pt-6 text-center">
                <p className="text-gray-600">No jars yet. Create one to start saving!</p>
              </CardContent>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
}

export default function JarsPage() {
  return (
    <ProtectedRoute>
      <JarsContent />
    </ProtectedRoute>
  );
}
