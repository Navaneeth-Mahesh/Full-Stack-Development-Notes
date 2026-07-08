function personProfile() {
    const name = "Navaneeth";
    let age = 19;
    const gender = "Male";
    let profession = "Full Stack Developer";
    let student = "Yes";

    console.log("Name:", name);
    console.log("Age:", age);
    console.log("Gender:", gender);
    console.log("Profession:", profession);
    console.log("Student:", student);
}

function location() {
    let city = "Hyd";
    const country = "India";

    console.log("City:", city);
    console.log("Country:", country);
}

function hobbies() {
    const hobby1 = "Gym";
    const hobby2 = "Coding";
    const hobby3 = "Photography";
    const hobby4 = "Reading";

    console.log("Hobbies:");
    console.log("1.", hobby1);
    console.log("2.", hobby2);
    console.log("3.", hobby3);
    console.log("4.", hobby4);
}

function status() {
    console.log("You are an adult.");
}

// Function calls
personProfile();
location();
hobbies();
status();

