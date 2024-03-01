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