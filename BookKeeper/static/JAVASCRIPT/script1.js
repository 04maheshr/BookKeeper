// Initialize an empty object to store books
var books = {};

 async function addBook(event) {
  event.preventDefault(); 
 
  var key = 'book_' + Date.now();
  // Get form values
  var pathivuEn = document.getElementById('pathivu-en').value;
  var pagupuEn = document.getElementById('pagupu-en').value;
  var title = document.getElementById('title').value;
  var author = document.getElementById('author').value;
  var rate = document.getElementById('rate').value;
  var year = document.getElementById('year').value;
  var rackNo = document.getElementById('rack-no').value;
  var rackSide = document.querySelector('input[name="rack_side"]:checked').value;
  var rowNo = document.getElementById('row-no').value;
  var formdata = new FormData();
  formdata.append("pathivuEn",pathivuEn);
  formdata.append("pagupuEn",pagupuEn);
  formdata.append("title",title);
  formdata.append("author",author);
  formdata.append("rate",rate);
  formdata.append("year",year);
  formdata.append("rackNo",rackNo);
  formdata.append("rackSide",rackSide);
  formdata.append("rowNo",rowNo);
  // to checjk the values are getting stored

  for (const [key,values] of formdata.entries()) {
    console.log(key,values);
  }
  try{
    const response =await fetch("/values",{
        method:"POST",
        body:formdata
    });
    if(response.ok){
        let data= await response.json();
        alert(data.message);
    }
  }
  finally{
    console.log("good bye");
  }

}
