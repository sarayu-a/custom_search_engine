async function search() {

    const query = document.getElementById("query").value;

    const response = await fetch(
        "http://127.0.0.1:8000/search?q=" + encodeURIComponent(query)
    );

    const data = await response.json();

    const list = document.getElementById("results");

    list.innerHTML = "";

    data.results.forEach(result => {

        const li = document.createElement("li");

        li.innerHTML = `
            <a href="${result.url}" target="_blank">
                ${result.title}
            </a>
            <br>
            <small>${result.url}</small>
        `;

        list.appendChild(li);

    });

}