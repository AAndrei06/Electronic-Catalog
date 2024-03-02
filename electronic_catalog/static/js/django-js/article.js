const web_socket = new WebSocket('ws://'+window.location.host+'/');
console.log('ws://'+window.location.host+'/');

web_socket.onmessage = function(event){
	const data = JSON.parse(event.data);
	console.log(data);
	if (data["message"] == "Article Edit"){
		document.getElementsByName(data["id"]+"-title")[0].innerHTML = data["title"];
		document.getElementsByName(data["id"]+"-desc")[0].innerHTML = data["description"];
	}else if (data["message"] == "Article Delete"){
		document.getElementsByName(data["id"])[0].remove()
	}
}

web_socket.onclose = function(event){
	console.log("Error with WebSocket");
}

let editBtns = document.querySelectorAll("#edit-btn");
let deleteBtns = document.querySelectorAll("#del-btn");

editBtns.forEach((edit) => {
	edit.onclick = function(event){
		let article_id = edit.getAttribute("name");
		console.log(article_id+"-title");
		let new_title = document.getElementsByName(article_id+"-title")[0].innerHTML;
		let new_desc = document.getElementsByName(article_id+"-desc")[0].innerHTML;
		web_socket.send(JSON.stringify({
			'message':"Article Edit",
			'id':article_id,
			'title':new_title,
			'description':new_desc,
		}))
	}
})

deleteBtns.forEach((btn) => {
	btn.onclick = function(event){
		let article_id = btn.getAttribute("name");
		web_socket.send(JSON.stringify({
			'message':"Article Delete",
			'id':article_id,
		}))
	}
})
