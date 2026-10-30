// Example of your frontend fetching from your FastAPI backend
document.getElementById("submitBtn").addEventListener("click", async () => {
    const userMessage = document.getElementById("messageInput").value;
    const outputElem = document.getElementById("output");

    const response = await fetch("http://127.0.0.1:8000/api/respond", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        message: userMessage,
        summary: "Web frontend user inquiry",
        priority: "medium"
    })
});

    const data = await response.json();
    
    // This line renders the Markdown response cleanly on your webpage!
    outputElem.innerHTML = marked.parse(data.response);
});