async function analyzeText() {

    const text = document.getElementById("message").value;

    if (!text.trim()) {
        alert("Please enter a message.");
        return;
    }

    const response = await fetch("/analyze-text", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            text: text
        })

    });

    const data = await response.json();

    showResult(data);
}


async function analyzeURL() {

    const url = document.getElementById("url").value;

    if (!url.trim()) {
        alert("Please enter a URL.");
        return;
    }

    const response = await fetch("/analyze-url", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            url: url
        })

    });

    const data = await response.json();

    showResult(data);
}


async function analyzeImage() {

    const file = document.getElementById("image").files[0];

    if (!file) {
        alert("Please select an image or video.");
        return;
    }

    const response = await fetch("/analyze-image", {
        method: "POST"
    });

    const data = await response.json();

    showResult(data);
}


function showResult(data) {

    let color = "";

    if (data.risk >= 70) {
        color = "🔴";
    }
    else if (data.risk >= 30) {
        color = "🟡";
    }
    else {
        color = "🟢";
    }


    let reasons = "";

    data.detected.forEach(item => {
        reasons += `<li>✓ ${item}</li>`;
    });


    document.getElementById("resultContent").innerHTML = `

        <h1>${color} ${data.level}</h1>

        <h2>Risk Score: ${data.risk}%</h2>

        <br>

        <h3>Why?</h3>

        <ul>
            ${reasons}
        </ul>

        <br>

        <p>
            ⚠️ Always verify suspicious content
            through official sources.
        </p>
    `;
}