export function uploadImage(endpoint, file) {
  const formData = new FormData();
  formData.append("file", file);

  return fetch(endpoint, {
    method: "POST",
    body: formData
  }).then(res => res.json());
}
import { uploadImage } from "./upload.js";

document.getElementById("imageInput").addEventListener("change", async (event) => {
    const file = event.target.files[0];
    if (file) {
        const response = await uploadImage("http://127.0.0.1:8000/process/upload/", file);
        console.log("Upload Response:", response);
    }
});


