$(document).ready(function(){
	function makeid(length) {
	    let result = '';
	    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
	    const charactersLength = characters.length;
	    let counter = 0;
	    while (counter < length) {
	      result += characters.charAt(Math.floor(Math.random() * charactersLength));
	      counter += 1;
	    }
	    return result;
	}
	let errorMessages = document.querySelector(".text-error");
	var csrf = $("input[name=csrfmiddlewaretoken]").val();
	let formObject = document.getElementsByTagName("form")[0];
	formObject.addEventListener("submit",(event) => {
		event.preventDefault();
		let username = $("input[name=username]").val();
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
				UUID:makeid(32),
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
