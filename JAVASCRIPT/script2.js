const details = {
    name: "Rajiva",
    age: 20,
    course: "BBA"
};

console.table(details);

//   Output :

//  ┌─────────┬──────────┐
//  │ (index) │ Values   │
//  ├─────────┼──────────┤
//  │ name    │ 'Rajiva' │
//  │ age     │ 20       │
//  │ course  │ 'BBA'    │
//  └─────────┴──────────┘

console.time("Timer");

for (let i = 0; i < 1000000; i++) {}

console.timeEnd("Timer");