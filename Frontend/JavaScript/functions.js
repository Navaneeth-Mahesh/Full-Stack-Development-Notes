function welcome(name) {
    console.log(`Welcome ${name}!`);
}

welcome("Navaneeth");
welcome("Rajiv");
welcome("Manohar");
welcome("Saranya");



function add(a, b){
    return a + b; // a-b, a*b, a/b, a%b 
}

console.log(add(100, 200));
console.log(add(500, 300));
console.log(add(800, 900));


function details(name, age, gender){
    console.log("Person Details");
    console.log("name:" + name);
    console.log("Age :" + age);
    console.log("Gender:" + gender);
}

details("Ram", 19, "Male");

function createUser(name, age) {
    return {
        name: name,
        age: age,
    };
}

console.log(createUser("Navaneeth", 19));

function getNumbers() {
    return ["siva", "kumar", 23];
//  return [10, 20, 30];
}
console.log(getNumbers());


function calculate(a, b) {
    return {
        sum: a + b,
        diff: a - b,
        product: a * b,
        quotient: a / b, 
    };
}

let result = calculate(25, 5);
console.log(result.sum);
console.log(result.quotient);

function introduce(name = "Unknown", age = 20) {
    console.log(`Name : ${name}`);
    console.log(`Age : ${age}`);
}
introduce();
introduce("Navaneeth", 20)

function add(...numbers){
    let sum = 0;
    for(let number of numbers){
        sum += number;
    }
    return sum;
}
console.log(add(10,20));
console.log(add(10,20,30,40));

//arrow function 
const greet = (name) => {
    return `Hello ${name}`;
};

setTimeout(function(){
    console.log("2.5 Sec completed");
}, 3000);

const numbers = [1,2,3,4];
numbers.forEach(function(number){
    console.log(number);
});

let count = 0;
function increment(){
    count++;
}

(function(){
    console.log("Testing Started !");
})();

function test(){
    test();
}

test();