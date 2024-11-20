const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function calculate(expression) {
    try {
        const result = eval(expression);
        return result;
    } catch (error) {
        return 'Error: Invalid expression';
    }
}

function main() {
    rl.question('Enter a mathematical expression: ', (expression) => {
        const result = calculate(expression);
        console.log(`Result: ${result}`);
        rl.close();
    });
}

main();