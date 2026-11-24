import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

function App() {
  const [sessionId, setSessionId] = useState('');
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    let storedSession = localStorage.getItem('session_id');

    if (!storedSession) {
      storedSession = 'session_' + crypto.randomUUID();
      localStorage.setItem('session_id', storedSession);
    }

    setSessionId(storedSession);
  }, []);

  const handleSend = async () => {
    if (!input.trim() || loading || !sessionId) return;

    const currentInput = input.trim();

    setMessages((prev) => [
      ...prev,
      { role: 'user', content: currentInput }
    ]);

    setInput('');
    setLoading(true);

    try {
      const res = await axios.post(
        'http://127.0.0.1:8000/api/respond',
        {
          message: currentInput,
          summary: 'General Query',
          priority: 'Medium',
          session_id: sessionId
        }
      );

      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: res.data.response
        }
      ]);

    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: '⚠️ Error: ' + err.message
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleNewChat = async () => {
    if (loading) return;

    setLoading(true);

    try {
      if (sessionId) {
        await axios.post(
          'http://127.0.0.1:8000/api/clear',
          { session_id: sessionId }
        );
      }
    } catch (err) {
      console.warn('Unable to clear old session:', err);
    } finally {
      const newSession = 'session_' + crypto.randomUUID();

      localStorage.setItem('session_id', newSession);
      setSessionId(newSession);
      setMessages([]);
      setInput('');
      setLoading(false);
    }
  };

  return (
    <div style={{
      maxWidth: '800px',
      margin: '20px auto',
      fontFamily: 'sans-serif'
    }}>

      <style>{`
        .markdown-content {
          line-height: 1.6;
          overflow-wrap: anywhere;
        }

        .markdown-content table {
          border-collapse: collapse;
          width: 100%;
          margin: 12px 0;
        }

        .markdown-content th,
        .markdown-content td {
          border: 1px solid #ccc;
          padding: 8px;
          text-align: left;
        }

        .markdown-content th {
          background: #e2e8f0;
        }

        .markdown-content pre {
          background: #1e293b;
          color: white;
          padding: 12px;
          border-radius: 6px;
          overflow-x: auto;
        }

        .markdown-content code {
          font-family: monospace;
        }

        .markdown-content img {
          max-width: 100%;
        }
      `}</style>

      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
      }}>
        <h2>Enterprise Ingestion Firewall — Week 3 Chat</h2>

        <button
          onClick={handleNewChat}
          disabled={loading}
          style={{
            backgroundColor: '#dc3545',
            color: '#fff',
            border: 'none',
            padding: '10px 15px',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          New Chat
        </button>
      </div>

      <p>
        <strong>Current Session ID:</strong> {sessionId}
      </p>

      <div style={{
        border: '1px solid #ccc',
        height: '400px',
        overflowY: 'auto',
        padding: '15px',
        borderRadius: '8px',
        marginBottom: '15px'
      }}>

        {messages.map((m, i) => (
          <div
            key={i}
            style={{
              textAlign: m.role === 'user' ? 'right' : 'left',
              margin: '10px 0'
            }}
          >
            <div style={{
              display: 'inline-block',
              maxWidth: '95%',
              padding: '10px',
              borderRadius: '8px',
              background: m.role === 'user'
                ? '#007bff'
                : '#f1f1f1',
              color: m.role === 'user'
                ? '#fff'
                : '#000',
              overflowX: 'auto'
            }}>

              {m.role === 'assistant' ? (
                <div className="markdown-content">
                  <ReactMarkdown remarkPlugins={[remarkGfm]}>
                    {m.content}
                  </ReactMarkdown>
                </div>
              ) : (
                m.content
              )}

            </div>
          </div>
        ))}

        {loading && (
          <p>Processing request...</p>
        )}

      </div>

      <div style={{
        display: 'flex',
        gap: '10px'
      }}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter') handleSend();
          }}
          placeholder="Type your message..."
          style={{
            flex: 1,
            padding: '10px'
          }}
        />

        <button
          onClick={handleSend}
          disabled={loading || !sessionId}
          style={{
            padding: '10px 20px',
            backgroundColor: '#007bff',
            color: '#fff',
            border: 'none',
            borderRadius: '4px'
          }}
        >
          {loading ? 'Wait...' : 'Send'}
        </button>
      </div>
    </div>
  );
}

export default App;