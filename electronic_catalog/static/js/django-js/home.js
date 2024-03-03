let addReport = document.getElementById("add-report-btn-submit");
let reportTitle = document.getElementById("title-of-post");
let reportDescription = document.getElementById("text-desc-rep");
let imageReport = document.getElementById("report-file-input");
const web_socket = new WebSocket('ws://'+window.location.host+'/');
console.log('ws://'+window.location.host+'/');

web_socket.onmessage = function(event){
	const data = JSON.parse(event.data);
	console.log(data);
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
console.log("Here");
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
		$.ajax({
			method:'POST',
			url:'',
			processData:false,
			contentType:false,
			mimeType:'multipart/form-data',
			data:data,
			success: function (res){
				console.log(res);
			}
		});
	})
})