'use client';

import { useState, useEffect, useRef } from 'react';
import { useAuth } from '@/lib/auth-context';
import { ProtectedRoute } from '@/lib/protected-route';
import { useAskCoach, useCoachHistory } from '@/lib/hooks';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Send, Lightbulb } from 'lucide-react';

function CoachContent() {
  const { user } = useAuth();
  const { data: history, refetch: refetchHistory } = useCoachHistory();
  const { mutate: askCoach, loading: asking } = useAskCoach({
    onSuccess: () => {
      setQuery('');
      refetchHistory();
    },
  });

  const [query, setQuery] = useState('');
  const [messages, setMessages] = useState<any[]>([]);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Load history on mount
  useEffect(() => {
    if (history) {
      setMessages(history);
    }
  }, [history]);

  // Auto-scroll to bottom
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    // Add user message to UI immediately
    const userMessage = { role: 'user', content: query };
    setMessages((prev) => [...prev, userMessage]);

    // Send to API
    await askCoach({ query });
  };

  const suggestedQuestions = [
    'How can I save more money?',
    'What should my emergency fund be?',
    'How to budget my income?',
    'Tips for reducing expenses?',
    'How to invest wisely?',
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 pb-24 flex flex-col">
      {/* Header */}
      <div className="bg-white border-b sticky top-0 z-10">
        <div className="max-w-md mx-auto px-4 py-4">
          <h1 className="text-2xl font-bold">AI Coach 🤖</h1>
          <p className="text-gray-600 text-sm">Your personal financial advisor</p>
        </div>
      </div>

      <div className="max-w-md mx-auto w-full px-4 py-6 flex-1 flex flex-col">
        {/* Messages */}
        <div className="flex-1 space-y-4 mb-6 overflow-y-auto">
          {messages.length === 0 ? (
            <div className="space-y-4">
              <Card>
                <CardContent className="pt-6 text-center">
                  <Lightbulb size={32} className="mx-auto text-blue-600 mb-3" />
                  <p className="font-semibold mb-2">Welcome to FinPilot Coach!</p>
                  <p className="text-sm text-gray-600 mb-4">
                    Ask me anything about your finances. I'm here to help you make smarter financial decisions.
                  </p>
                </CardContent>
              </Card>

              <div>
                <p className="text-sm font-semibold text-gray-700 mb-3">Suggested questions:</p>
                <div className="space-y-2">
                  {suggestedQuestions.map((q, idx) => (
                    <button
                      key={idx}
                      onClick={() => {
                        setQuery(q);
                      }}
                      className="w-full text-left p-3 bg-white rounded-lg border border-gray-200 hover:border-blue-400 hover:bg-blue-50 transition text-sm"
                    >
                      {q}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          ) : (
            messages.map((msg, idx) => (
              <div
                key={idx}
                className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                <div
                  className={`max-w-xs px-4 py-3 rounded-lg ${
                    msg.role === 'user'
                      ? 'bg-blue-600 text-white rounded-br-none'
                      : 'bg-white text-gray-900 border border-gray-200 rounded-bl-none'
                  }`}
                >
                  <p className="text-sm">{msg.content}</p>
                </div>
              </div>
            ))
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Form */}
        <form onSubmit={handleSubmit} className="flex gap-2">
          <Input
            placeholder="Ask me anything..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            disabled={asking}
            className="flex-1"
          />
          <Button
            type="submit"
            disabled={asking || !query.trim()}
            size="icon"
          >
            <Send size={18} />
          </Button>
        </form>
      </div>
    </div>
  );
}

export default function CoachPage() {
  return (
    <ProtectedRoute>
      <CoachContent />
    </ProtectedRoute>
  );
}
