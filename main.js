async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  try {
    const response = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username: username, password: password }),
    });
    const result = await response.json();
    if (result.status === "success") {
      alert("Logged In!");
    } else {
      alert("Failed Login");
    }
  } catch (error) {
    alert(error.message);
  }
}
