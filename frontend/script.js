document.getElementById('analyzeBtn').addEventListener('click', async () => {
    const message = document.getElementById('messageInput').value.trim();
    const outputElem = document.getElementById('outputResult');

    if (!message) {
        alert('Please enter a message first.');
        return;
    }

    outputElem.textContent = 'Processing through ingestion firewall...';

    try {
        const response = await fetch('http://127.0.0.1:8000/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || 'Validation or Server Error');
        }

        outputElem.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        outputElem.textContent = `[ERROR] ${error.message}`;
    }
});
