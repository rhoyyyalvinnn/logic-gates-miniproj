document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("prediction-form");
    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const bit1 = document.getElementById("bit1").value;
        const bit2 = document.getElementById("bit2").value;
        const gate = document.getElementById("gate").value;

        // Input validation
        if (bit1 === "" || bit2 === "" || gate === "") {
            alert("Please fill in all fields.");
            return;
        }

        const formData = new FormData();
        formData.append("bit1", bit1);
        formData.append("bit2", bit2);
        formData.append("gate", gate);

        // Send the data to the backend
        fetch("/predict", {
            method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            // Display the result in a new page
            document.body.innerHTML = data;
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
