alert( null || 2 || undefined );

alert( alert(1) || 2 || alert(3) );

alert( 1 && null && 2 );

alert( alert(1) && alert(2) );

alert( null || 2 && 3 || 4 );

if(age >= 14 && age <= 90)

if(!(age >= 14 && age <= 90))
if(age < 14 || age > 90)

if (-1 || 0) alert( 'first' ); 
if (-1 && 0) alert( 'second' ); 
if (null || -1 && 1) alert( 'third' ); 

let login = prompt("Who is there", '');
if(login == "Admin") {
  let password = prompt("Password?", '');
  if(password === "TheMaster"){
    alert("Welcome!");
  } else if(password === '' || password === null) {
    alert("Caneled");
  } else {
    alert("Wrong password");
  }
} else if(login === '' || password === null){
  alert("Canceled");
} else {
  alert("I don't know u");
}