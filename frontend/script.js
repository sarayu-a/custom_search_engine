const API_URL = "http://127.0.0.1:8000";


async function search() {
    const query = document.getElementById("query").value.trim();

    if (!query) {
        return;
    }

    const response = await fetch(
        `${API_URL}/search?q=${encodeURIComponent(query)}`
    );

    const data = await response.json();

    displayResults(data.results);
}


function displayResults(results) {
    const list = document.getElementById("results");

    list.innerHTML = "";

    if (results.length === 0) {
        list.innerHTML = "<li>No results found.</li>";
        return;
    }

    for (const result of results) {
        const li = document.createElement("li");

        li.innerHTML = `
            <a href="${result.url}" target="_blank">
                ${result.title}
            </a>
            <br>
            <small>${result.url}</small>
        `;

        list.appendChild(li);
    }
}