async function handleSubmit() {
    console.log("handleSubmit called");
    const output = document.getElementById("output");
    output.value = "Submitting...";

    const relationEls = document.querySelectorAll('.relation');
    const relationList = Array.from(relationEls, el => el.value.trim()).filter(Boolean);
    console.log("relationList", relationList);

    if (relationList.length === 0) {
        output.value = "Please enter rule values.";
        return;
    }

    const seed = document.getElementById("input");
    const BACKEND_URL = "http://127.0.0.1:5000"; // replace with deployed backend URL in production
    const url = `${BACKEND_URL}/process`;
    const payload = { seed: seed.value, relations: relationList };
    console.log("Submitting to Flask:", url, payload);

    try {
        const response = await fetch(url, {
            method: "POST",
            mode: "cors",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        console.log("Fetch response status:", response.status);

        if (!response.ok) {
            const errorText = await response.text();
            console.error("API error", response.status, errorText);
            output.value = `Error ${response.status}: ${errorText}`;
            return;
        }

        const data = await response.json();
        console.log("API response body:", data);
        const sequence = data.sequence || [];
        output.value = Array.isArray(sequence) ? sequence.join(", ") : String(sequence);
    } catch (error) {
        console.error("Fetch failed", error);
        output.value = `Fetch failed: ${error.message}`;
    }
}
