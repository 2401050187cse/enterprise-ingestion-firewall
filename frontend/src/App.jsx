import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';

function App() {
  const [message, setMessage] = useState('');
  const [summary, setSummary] = useState('');
  const [priority, setPriority] = useState('medium');
  const [response, setResponse] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResponse('');

    try {
      const res = await fetch('http://127.0.0.1:8000/api/respond', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message, summary, priority })
      });

      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.detail || 'An error occurred');
      }

      setResponse(data.response);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '650px', margin: '40px auto', fontFamily: 'Arial, sans-serif', padding: '20px' }}>
      <h2>Enterprise Ingestion Firewall — Week 2 UI</h2>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
        <div>
          <label style={{ display: 'block', fontWeight: 'bold', marginBottom: '5px' }}>User Support Message:</label>
          <input 
            type="text" 
            value={message} 
            onChange={(e) => setMessage(e.target.value)} 
            placeholder="Enter issue description..."
            required 
            style={{ width: '100%', padding: '10px', boxSizing: 'border-box' }}
          />
        </div>
        <div>
          <label style={{ display: 'block', fontWeight: 'bold', marginBottom: '5px' }}>Summary:</label>
          <input 
            type="text" 
            value={summary} 
            onChange={(e) => setSummary(e.target.value)} 
            placeholder="Brief summary..."
            style={{ width: '100%', padding: '10px', boxSizing: 'border-box' }}
          />
        </div>
        <div>
          <label style={{ display: 'block', fontWeight: 'bold', marginBottom: '5px' }}>Priority Level:</label>
          <select value={priority} onChange={(e) => setPriority(e.target.value)} style={{ width: '100%', padding: '10px' }}>
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
          </select>
        </div>
        <button type="submit" disabled={loading} style={{ padding: '12px', backgroundColor: '#007bff', color: '#fff', border: 'none', cursor: 'pointer', fontSize: '16px' }}>
          {loading ? 'Validating & Processing...' : 'Submit Payload'}
        </button>
      </form>

      {error && (
        <div style={{ color: 'red', marginTop: '20px', padding: '12px', border: '1px solid red', backgroundColor: '#ffe6e6' }}>
          <strong>Firewall / System Alert:</strong> {error}
        </div>
      )}

      {response && (
        <div style={{ marginTop: '20px', padding: '15px', border: '1px solid #ddd', backgroundColor: '#f8f9fa' }}>
          <h3>AI Response (Rendered Markdown):</h3>
          <ReactMarkdown>{response}</ReactMarkdown>
        </div>
      )}
    </div>
  );
}

export default App;