// const count = document.querySelector('span');
// const button = document.querySelector('button');
// button.addEventListener('click', function () {
//   count.textContent = parseInt(count.textContent) + 1;
// });

fetch('http://127.0.0.1:8001', {mode: 'no-cors'})
.then((response) => console.log(response));