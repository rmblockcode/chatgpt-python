const chatgptResponse = document.getElementById('chatgptResponse');
const btnSubmit = document.getElementById('btnSubmit');
const responseContainer = document.querySelector('.responseContainer');
const originalText = btnSubmit.value;

responseContainer.style.display = 'none';

btnSubmit.addEventListener('click', (event) => {
    event.preventDefault();

    // Obtener los valores de los campos del formulario
    const promptValue = document.getElementById('promptValue').value;
    btnSubmit.value = 'Cargando...';

    // Configuracion de Axios para enviar la peticion POST a nuestra API
    axios.post('/chatgpt', {
        promptValue: promptValue
    })
    .then((response) => {
        btnSubmit.value = originalText;
        responseContainer.style.display = 'block';
        chatgptResponse.innerHTML = response.data.message;
    })
    .catch((error) => {
        chatgptResponse.innerHTML = error; //Manejo de errores
    });
})