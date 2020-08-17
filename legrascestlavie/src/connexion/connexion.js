const login = (envent) => {
    event.preventDefault()
    const loginInfo = {}
    const form =event.target
    for (input of form) {
        if (input.id !== "") {
            loginInfo[input.id] = input.value
        }
    }

    fetch('http://127.0.0.1:5000/connexion', {
    method:"GET",
    body:JSON.stringify(form),
    headers:{'Content-Type': 'application/json'}

})




document.querySelector('#connexion').addEventListener('submit', login)

}
