const API_BASE = "http://127.0.0.1:8000";

function analyzeStress() {
  const fileInput = document.getElementById("stressImage");
  const resultDiv = document.getElementById("stressResult");

  if (!fileInput.files.length) {
    resultDiv.innerText = "Please upload an image";
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  fetch(`${API_BASE}/stress/analyze`, {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      resultDiv.innerHTML = `
        <p><b>Emotion:</b> ${data.emotion}</p>
        <p><b>Stress Level:</b> ${data.stress_level}</p>
      `;
    })
    .catch(err => {
      resultDiv.innerText = "Error analyzing stress";
      console.error(err);
    });
}

