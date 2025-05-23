fetch("https://web-croud.onrender.com/collect", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    url: window.location.href,
    userAgent: navigator.userAgent,
    referrer: document.referrer,
  })
});
