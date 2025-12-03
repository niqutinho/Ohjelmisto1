'use strict';

const num1Input = document.getElementById('num1');
const num2Input = document.getElementById('num2');
const operationSelect = document.getElementById('operation');
const calculateBtn = document.getElementById('start');
const resultEl = document.getElementById('result');

calculateBtn.addEventListener('click', () => {
    // Convert input values to integers
    const a = parseInt(num1Input.value.trim(), 10);
    const b = parseInt(num2Input.value.trim(), 10);
    const op = operationSelect.value;

    if (isNaN(a) || isNaN(b)) {
        resultEl.textContent = 'Please enter valid integers';
        return;
    }

    let result;

    if (op === 'add') {
        result = a + b;
    } else if (op === 'sub') {
        result = a - b;
    } else if (op === 'multi') {
        result = a * b;
    } else if (op === 'div') {
        if (b === 0) {
            result = 'Error: Division by zero';
        } else {
            result = Math.floor(a / b); // integer division
        }
    } else {
        result = 'Invalid operation';
    }

    resultEl.textContent = result;
});
