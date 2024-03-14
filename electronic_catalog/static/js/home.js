let menuBtn = document.querySelector('.fa-bars')
let menu_open = true;
let menuSlide = document.querySelector(".menu-slide");
menuSlide.style.transition = "0.5s";
menuBtn.onclick = () => {
	if (menu_open){
		menuSlide.style.left = "0px";
		menu_open = false;
		document.getElementsByTagName("body")[0].style.overflow = "hidden";
	}else{
		menuSlide.style.left = "-270px";
		menu_open = true;
		document.getElementsByTagName("body")[0].style.overflow = "visible";
	}
}	

let closeBTN = document.querySelector(".close-btn");
let closeBTN2 = document.querySelector(".close-btn2");
let closeBTN3 = document.querySelector(".close-btn3");
let closeBTN4 = document.querySelector(".close-btn4");
let closeBTN5 = document.querySelector(".close-btn5");
let settingsTable = document.querySelector(".settings-table");
let setOn = document.querySelector(".set-table-on");
let markPanel = document.querySelector(".mark-panel");
let addStudentBtn = document.getElementById("add-std-btn");
let addStdPanel = document.getElementById("add-student");
let rmStudent = document.getElementById("remove-student");
let setT = false;
let addStd = false;
let rmStdBtn = document.getElementById("remove-std-btn");
let rmStdBool = false;
let reportBool = false;
let reportTable = document.getElementById("report-add-table");
let reportBtn = document.getElementById("add-report");
let addMarkBtnSubmit = document.getElementById("submit-mark-to-std");


function showReportAdd(){
	if (!reportBool){
		reportTable.style.display = "block";
		reportBool = true;
	}else{
		reportTable.style.display = "none";
		reportBool = false;
	}
}


reportBtn.onclick = showReportAdd;
closeBTN5.onclick = showReportAdd;

function rmPlaceStd(){
	if (!rmStdBool){
		rmStudent.style.display = "block";
		rmStdBool = true;
	}else{
		rmStudent.style.display = "none";
		rmStdBool = false;
	}
}

rmStdBtn.onclick = rmPlaceStd;
closeBTN4.onclick = rmPlaceStd

addStudentBtn.onclick = () => {
	if (!addStd){
		addStdPanel.style.display = "block";
		addStd = true;
	}else{
		addStdPanel.style.display = "none";
		addStd = false;
	}
}

setOn.onclick = () => {
	if (!setT){
		settingsTable.style.display = "block";
		setT = true;
	}else{
		settingsTable.style.display = "none";
		setT = false;
	}
}

closeBTN3.onclick = () => {
	if (!addStd){
		addStdPanel.style.display = "block";
		addStd = true;
	}else{
		addStdPanel.style.display = "none";
		addStd = false;
	}
}
	
closeBTN.onclick = () => {
	if (!setT){
		settingsTable.style.display = "block";
		setT = true;
	}else{
		settingsTable.style.display = "none";
		setT = false;
	}
}

closeBTN2.onclick = () => {
	markPanel.style.display = "none";
}


let mainDiv = document.querySelector(".main-div-register");
let marks = document.getElementsByName("mark-object-std");

mainDiv.addEventListener("mouseout",() => {
	for (let m of marks){
		m.style.backgroundColor = "whitesmoke";
	}
})

for (let m of marks){

	m.addEventListener("mouseover",() => {

		for (let x of marks){
			if (x.getAttribute('id') == m.getAttribute('id') || x.getAttribute('value') == m.getAttribute('value')){
				x.style.backgroundColor = "#4287f5";
			}else{
				x.style.backgroundColor = "whitesmoke";
			}
		}
	})
}