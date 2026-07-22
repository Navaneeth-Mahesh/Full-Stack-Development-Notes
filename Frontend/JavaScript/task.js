function createProfile(Name, Age, Gender, city, country, profession, dreamjob){
    console.log("======= Profile ==========");
    console.log("Name :" +""+Name);
    console.log("Age : "+""+ Age);
    console.log("Gender :" +""+Gender);
    console.log("city :"+""+city);
    console.log("Country :"+""+country);
    console.log("Profession :"+""+profession);
    console.log("DreamJob :"+""+dreamjob);
}
createProfile("Navaneeth", 19, "Male", "Kakinada", "India", "Student", "Full Stack + AI Developer")

console.log("======================");


function Studentdetails(name, rollno, branch, sem, Cgpa, college){
    console.log("========= StudentDetails ========");
    console.log("Name :" + name);
    console.log("Roll no :" + rollno);
    console.log("Branch :" + branch);
    console.log("Sem :"+sem);
    console.log("cgpa :"+Cgpa);
    console.log("College:"+college);
}

Studentdetails("navaneeth", "5DC", "cse", "5th", 8.1, "PEC");
console.log("===========")



function movieTicket(movieName, theatre, seat, price) {
    let gst = price * 0.18;
    let total = price + gst;
    console.log("====== Movie Ticket ======");
    console.log("Movie :", movieName);
    console.log("Theatre :", theatre);
    console.log("Seat :", seat);
    console.log("Base Price :", price);
    console.log("GST :", gst);
    console.log("Total :", total);
}

movieTicket("Doomsday", "INOX", "A10", 170);
