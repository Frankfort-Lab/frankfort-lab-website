// Function to toggle between current and past lab members

function showLabMembers(type) {
    const currentDiv = document.getElementById("current-members");
    const pastDiv = document.getElementById("past-members");
    const buttons = document.querySelectorAll(".curr-prev-button");

    if (type === "current") {
        currentDiv.style.display = "flex";
        pastDiv.style.display = "none";
    } else {
        currentDiv.style.display = "none";
        pastDiv.style.display = "flex";
    }

    buttons.forEach(btn => btn.classList.remove("active"));
    document.querySelector(`.curr-prev-button[onclick*='${type}']`).classList.add("active");
}

