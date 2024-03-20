document.write("this is java script");//prints out text
document.body.style.backgroundImage = "url('images/wallpaper1.jpg')";



function myfunction(){

const myElement = document.getElementById("red1");
document.getElementById("red1").style.color ="red";
}


function myfunction1(){
	const values = [1 ,2,3];
	for(let i = 0; i < values.length;i++){
	var x = 5;
	var y = 10;
	var result = x+y*values[i];
}

	document.getElementById("calc").innerHTML = result;
}
