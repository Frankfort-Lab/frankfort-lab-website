// Function to generate the header for each page

function loadHeader() {
    fetch("header.html")
        .then(res => {
            if (!res.ok) throw new Error("Failed to load header");
            return res.text();
        })
        .then(data => {
            document.querySelector("#header-placeholder").innerHTML = data;
        })
        .catch(err => console.error(err));
}

loadHeader();

