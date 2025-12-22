const API_BASE = "http://127.0.0.1:8000";

function markAttendance() {
  const fileInput = document.getElementById("imageInput");
  const resultDiv = document.getElementById("result");

  if (!fileInput.files.length) {
    resultDiv.innerText = "Please upload an image";
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  fetch(`${API_BASE}/attendance/mark`, {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      resultDiv.innerHTML = `
        <p><b>Status:</b> ${data.status}</p>
        <p><b>Student:</b> ${data.student_name}</p>
      `;
    })
    .catch(err => {
      resultDiv.innerText = "Error marking attendance";
      console.error(err);
    });
}

