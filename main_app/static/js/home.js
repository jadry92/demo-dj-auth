
const form = document.getElementById('login-form');
form.addEventListener('submit', function (e) {
    e.preventDefault()
    const data = {
      username: e.target.username.value,
      password: e.target.password.value
    }
    console.log(data)
    fetch('/users/auth/login/', {
        headers: {
          'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(data)
    }).then(function (response) {
        if (response.status === 200) {
          const res_data = response.json();
          res_data.then((data) => AddResponseToDOM(data))
        } else {
          response.json().then((data) => AddResponseToDOM(data))
        }
    })
});

function AddResponseToDOM(data) {
  const p = document.getElementById('response');
  const card = `<div class="mb-3 row">
  <div class="offset-md-3 col-md-6 col-12">
      <card class="card">
          <div class="card-body">
              <h5 class="card-title">Response</h5>
              <p class="card-text">${JSON.stringify(data)}</p>
          <div>
      </card>
    </div>
  </div>`
  p.innerHTML = card;
}