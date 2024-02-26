$(document).ready(function(){
	let errorMessages = document.querySelector(".text-error");
	var csrf = $("input[name=csrfmiddlewaretoken]").val();
	errorMessages.style.color = "#fc2403";
	errorMessages.style.fontWeight = "bold";
	errorMessages.style.display = "block";
	errorMessages.style.margin = "0px";
	errorMessages.style.padding = "0px";
	let formObject = document.getElementsByTagName("form")[0];
	formObject.addEventListener("submit",(event) => {
		event.preventDefault();
		let username = $("input[name=username]").val();
		console.log(username)
		let email = $("input[name=email]").val();
		let password = $("input[name=password]").val();
		let password2 = $("input[name=password2]").val();
		$.ajax({
			url:'',
			type:'post',
			data:{
				name:username,
				email:email,
				password:password,
				password2:password2,
				csrfmiddlewaretoken:csrf
			},
			success: function(response){
				console.log(response.text);
			}
		})
	})
})
