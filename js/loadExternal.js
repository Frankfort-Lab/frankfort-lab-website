// Function to load external html table

document.addEventListener("DOMContentLoaded", () => {
    fetch('./lab_meeting/lab_meeting_calendar.html')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            const container = document.getElementById('external-content');
            container.innerHTML = data;

            // Replace literal \n strings in all table cells with actual line breaks
            const cells = container.querySelectorAll('.dataframe td');
            cells.forEach(cell => {
                cell.innerText = cell.innerText.replace(/\\n/g, '\n');
            });
        })
        .catch(error => {
            console.error('Error loading content:', error);
        });
});