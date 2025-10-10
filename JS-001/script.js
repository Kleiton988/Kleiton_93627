// funçao para validar formulario 
function validateform(){
    // obtem os valores dos campos de input pelo id

let nome = document.getElementById('nome').value;
let email = document.getElementById('email').value;
let senha = document.getElementById('senha').value;
let confirmsenha = document.getElementById('confirmsenha').value;
let errormessage = document.getElementById('error-message').value;

errormessage.textContent = '';

if(nome === ''){
    errormessage.textContent = 'Por favor , insira seu nome';
    return false;

}
if(email === ''){
    errormessage.textContent = 'Por favor , insira seu email corretamente';
    return false;

}
if( senha !== confirmsenha){
    errormessage.textContent = 'Por favor , insira sua senha corretamente';
    return false;

}
if(confirmsenha ===  senha){
    errormessage.textContent = 'Por favor , corrija a senha corretamnmte';
    return false;

}
return true;
}