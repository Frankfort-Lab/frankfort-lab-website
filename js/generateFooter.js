// Function to generate the footer for each page

function loadFooter() {
    fetch("footer.html")
        .then(res => {
            if (!res.ok) throw new Error("Failed to load footer");
            return res.text();
        })
        .then(data => {
            document.querySelector("#footer-placeholder").innerHTML = data;

            // Set current year after footer is loaded
            const yearSpan = document.getElementById("currentYear");
            if (yearSpan) {
                yearSpan.textContent = new Date().getFullYear();
            }
        })
        .catch(err => console.error(err));
}

loadFooter();
