export function uploadImage(endpoint, file) {
  const formData = new FormData();
  formData.append("file", file);

  return fetch(endpoint, {
    method: "POST",
    body: formData
  }).then(res => res.json());
}

