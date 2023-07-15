function fetchTimelinePosts() {
  console.log("Start fetching api")
  fetch('/api/timeline_post', { method: 'GET' })
    .then(response => response.json())
    .then(data => {
      const timelinePosts = data.timeline_posts;
      const timelinePostsContainer = document.getElementById('timelinePosts');
      timelinePostsContainer.innerHTML = '';

      // Display timeline posts in descending order
      timelinePosts.forEach(post => {
        const postElement = document.createElement('div');
        postElement.innerHTML = `
          <h3>${post.name}</h3>
          <p>${post.content}</p>
          <p><em>${post.created_at}</em></p>
          <hr>
        `;
        timelinePostsContainer.appendChild(postElement);
      });
    })
    .catch(error => console.error('Error:', error));
}

// Function to handle form submission and create a timeline post
function submitForm(event) {
event.preventDefault();
const form = document.getElementById('postForm');
const formData = new FormData(form);

fetch('/api/timeline_post', {
    method: 'POST',
    body: formData
})
  .then(response => response.json())
  .then(data => {
      console.log('Success:', data);
      fetchTimelinePosts(); // Refresh timeline posts after successful submission
      form.reset(); // Clear the form fields
  })
  .catch(error => console.error('Error:', error));
}

// Fetch timeline posts when the page loads
document.addEventListener('DOMContentLoaded', () => {
fetchTimelinePosts();
});

// Add event listener to the form for form submission
const form = document.getElementById('postForm');
form.addEventListener('submit', submitForm);
