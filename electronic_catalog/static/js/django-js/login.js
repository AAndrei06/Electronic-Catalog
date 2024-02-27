$(document).ready(function(){
	let errorMessages = document.querySelector(".text-error");
	var csrf = $("input[name=csrfmiddlewaretoken]").val();
	let formObject = document.getElementsByTagName("form")[0];
	formObject.addEventListener("submit",(event) => {
		event.preventDefault();
		let name = $("input[name=name]").val();
		let password = $("input[name=password]").val();
		$.ajax({
			url:'',
			type:'post',
			data:{
				name:name,
				password:password,
				csrfmiddlewaretoken:csrf
			},
			success: function(response){
				if (response.text != 'valid'){
					errorMessages.style.display = "block";
					errorMessages.innerHTML = response.text;
					setTimeout(() => {
						errorMessages.style.display = "none";
					},5000);
				}else{
					window.location.href = '/';
				}
			}
		})
	})
})
