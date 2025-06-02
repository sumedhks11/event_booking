document.addEventListener('DOMContentLoaded', function () {
  fetch('/events')  // Flask route rendering events.html
    .then(response => response.text())
    .then(html => {
      document.getElementById('main-content').innerHTML = html;
    });
});
