$(function idCheck(){
	$('#idBtn').click(function() {
		var username = $('#idBox').val()
		if(username == ''){
			alert('아이디 좀 입력해라. 개씨발새키야.')
			return;
		}
		$.ajax({
			url:'/idcheck',
			type:'get',
			dataType:'json',
			success:function(response){
				if(response.result == "exist"){
					alert("아 씨발 이미 있는 아이디라고 병신새킨야");
					$('#idBox').val('').focus();
					return;
				}else{
				    alert("써라 병신아" + username);
					$('#idBtn').hide();
					return;
				}
			},
               error : function(xhr, error){
				alert("서버와의 통신에서 문제가 발생했습니다.");
				console.error("error : " + error);
			}
		})
	})
})
