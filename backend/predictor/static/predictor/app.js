document.getElementById("predictForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const model = document.getElementById("model").value;

    const data = {
        Age: Number(Age.value),
        Sex: Sex.value,
        ChestPainType: ChestPainType.value,
        RestingBP: Number(RestingBP.value),
        Cholesterol: Number(Cholesterol.value),
        FastingBS: Number(FastingBS.value),
        RestingECG: RestingECG.value,
        MaxHR: Number(MaxHR.value),
        ExerciseAngina: ExerciseAngina.value,
        Oldpeak: Number(Oldpeak.value),
        ST_Slope: ST_Slope.value
    };

    const response = await fetch(`/api/predict/${model}/`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await response.json();
    const resultDiv = document.getElementById("result");

    const risk = result.prediction === 1;
    const probability = (result.probability[1] * 100).toFixed(2);

    resultDiv.classList.remove("hidden");
    resultDiv.className = `result ${risk ? "high" : "low"}`;

    resultDiv.innerHTML = risk
        ? `High Risk Detected<br>Probability: ${probability}%`
        : `Low Risk Detected<br>Probability: ${probability}%`;
});
