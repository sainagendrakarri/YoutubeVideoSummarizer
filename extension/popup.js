const btn = document.getElementById("summarise");

btn.addEventListener("click", async () => {
    btn.disabled = true;
    btn.textContent = "Summarising...";

    const output = document.getElementById("output");

    try {
        const [tab] = await chrome.tabs.query({
            active: true,
            currentWindow: true
        });

    const url = new URL(tab.url);

    const videoId = url.searchParams.get("v");

    const response = await fetch(
        `http://127.0.0.1:5000/summary?videoId=${videoId}`
    );

        const data = await response.json();

        if (!response.ok) {
            output.textContent = data.error || "Something went wrong.";
        } else {
            output.textContent = data.summary;
        }

    } catch (error) {
        output.textContent = "Unable to connect to the backend server.";
        console.error(error);
    } finally {
        btn.disabled = false;
        btn.textContent = "Summarise";
    }
});
