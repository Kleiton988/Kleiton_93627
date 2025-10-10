document.getElementById('calculatorForm').addEventListener
('submit',
    function(event) {
                     event.preventDefault();
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);

    if(isNaN(num1) || isNaN(num2)){
    alert('Por favor , insira u numero valido');
    return;

    }
    
    const result = num1 + num2;

    document.getElementById('result').textContent = result;

    }
)