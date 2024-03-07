let addReport = document.getElementById("add-report-btn-submit");
let reportTitle = document.getElementById("title-of-post");
let reportDescription = document.getElementById("text-desc-rep");
let imageReport = document.getElementById("report-file-input");

const web_socket = new WebSocket('ws://'+window.location.host+'/');
console.log('ws://'+window.location.host+'/');

web_socket.onmessage = function(event){
	const data = JSON.parse(event.data);
	if (data.message == "Add Mark"){
		console.log(data)
		let markRow = document.querySelectorAll(`[title="${data.student_id}"]`);
		if (data.month == document.getElementById("month-marks-obj").innerHTML){
			for (col of markRow){
				if (col.classList.contains(data.day)){
					if (data.mark == "99999"){
						col.innerHTML = `<p></p>`;
						continue;
					}
					if (data.present == true){
						col.innerHTML = `<p>${data.mark}</p>`;
					}
					else{
						col.innerHTML = `<p>Ab</p>`;
					}
				}
			}
		}
	}
}

web_socket.onclose = function(event){
	console.log("Error with websocket");
}

addReport.onclick = function(event){
	if(imageReport.value != "") {
		const file = imageReport.files[0];
		const reader = new FileReader();
		reader.addEventListener("load",() => {
			console.log(reader.result)
			web_socket.send(JSON.stringify({
				'message':"Article Create",
				'title':reportTitle.value,
				'description':reportDescription.value,
				'image':reader.result
			}))
		})
		reader.readAsDataURL(file); 
	}
}


// HomeWork Create
$(document).ready(function(){
	let addHomeworkForm = document.getElementById("add-home-form");
	addHomeworkForm.addEventListener("submit",(event) => {
		event.preventDefault();
		let title = document.getElementsByName("title-of-homework")[0].value;
		let description = document.getElementsByName("description-of-homework")[0].value;
		let grade = document.getElementsByName("class-option-name-home")[0].value;
		let files = document.getElementsByName("file-input-homework")[0].files;
		var csrf = $("input[name=csrfmiddlewaretoken]").val();
		let data = new FormData();
		data.append("title",title);
		data.append("description",description);
		data.append("grade",grade);
		for (let i = 0;i < files.length;i++){
			data.append("files",files[i]);
		}
		data.append("csrfmiddlewaretoken",csrf);
		data.append("purpose","add_homework")
		$.ajax({
			method:'POST',
			url:'',
			processData:false,
			contentType:false,
			mimeType:'multipart/form-data',
			data:data
		});
	})
})

// Add Student

let addStudent = document.getElementsByName("add-student-btn-class")[0];

addStudent.addEventListener("click",() => {
	let classOfStudent = document.querySelector('input[name="radio1"]:checked').value;
	let studentID = document.getElementsByName('student-id-add-to-class')[0].value;
	web_socket.send(JSON.stringify({
		'message':"Student Add",
		'ID':studentID,
		'classroom':classOfStudent
	}))
})

// Remove Student

let removeStd = document.getElementsByName("remove-student-from-classroom")[0];

removeStd.addEventListener("click",() => {
	let studentID = document.getElementsByName('student-id-remove')[0].value;
	web_socket.send(JSON.stringify({
		'message':"Student Remove",
		'ID':studentID,
	}))
})

// Add Mark

let submitMarkBtn = document.getElementById("submit-mark-to-std");
let monthToGo = "";
let dayToGo = "";
let student_id_mark = ""
for (mark of marks){
	mark.addEventListener("click",(event) => {
		event.stopPropagation();
		dayToGo = event.srcElement.getAttribute('value');
		student_id_mark = event.srcElement.getAttribute('title');
		monthToGo = document.getElementById("month-marks-obj").innerHTML;
		markPanel.style.display = "block";
	})
}

submitMarkBtn.onclick = function (){
	console.log(dayToGo)
	console.log(monthToGo)
	console.log(student_id_mark)
	console.log(document.querySelector('input[name="radio"]:checked').value)

	web_socket.send(JSON.stringify({
		"message":"Add Mark",
		"mark":document.querySelector('input[name="radio"]:checked').value,
		"day":dayToGo,
		"month":monthToGo,
		"student_id":student_id_mark
	}))
	document.getElementById("not").checked = true;
}

// Add Homework

$(document).ready(function(){
	let submitHomeworkForms = document.querySelectorAll("#form-submit-homework");
	for (form of submitHomeworkForms){
		form.addEventListener("submit",(event) => {
			event.preventDefault();
			let thatForm = event.srcElement;
			console.log(thatForm)
			let filesToUpload = document.getElementsByName(thatForm.getAttribute('value')+"-file-for-homework")[0].files;
			let data = new FormData();
			console.log(filesToUpload)
			for (let i = 0;i < filesToUpload.length;i++){
				data.append("files",filesToUpload[i]);
			}
			data.append("csrfmiddlewaretoken",document.getElementsByName("csrfmiddlewaretoken")[0].value);
			data.append("purpose","send_homework_to_teacher");
			$.ajax({
				method:'POST',
				url:'',
				processData:false,
				contentType:false,
				mimeType:'multipart/form-data',
				data:data
				});
		});
	}
})