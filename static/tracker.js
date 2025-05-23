fetch("https://web-croud.onrender.com/collect", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    url: window.location.href,
    userAgent: navigator.userAgent,
    referrer: document.referrer
  })
})
.then(response => {
  if (!response.ok) {
    console.error("Tracking failed:", response.statusText);
  } else {
    console.log("Visit tracked successfully");
  }
})
.catch(error => {
  console.error("Tracking error:", error);
});
