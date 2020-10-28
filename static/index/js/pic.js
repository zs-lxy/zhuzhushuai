function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$(function () {
    $(".input_sub").click(function (e) {
        var nick_name = $("#nick_name").val();
        var sex = $("radio[name=sex]:checked").val()
        var avatar = $("#avatar").val()
        params = {
            "nick_name": nick_name,
            "sex": sex,
            "avatar": avatar
        }
        //TODO 上传头像
        // 模拟表单的提交
        $.ajax({
            url: '/user/user_avatar',
            type: 'post',
            contentType: "application/json",
            data: JSON.stringify(params),
            success: function (resp) {
                if (resp.errno == '0') {
                    // `上传头像`成功
                    // 获取上传头像的完整的url地址
                    var avatar_url = resp.avatar_url;
                    // 设置页面上用户头像img的src属性
                    // $(".now_user_pic").attr("src", avatar_url);
                    // // 设置父窗口中用户头像img的src属性
                    // $(".user_center_pic>img", parent.document).attr("src", avatar_url);
                    // $(".user_login>img", parent.document).attr("src", avatar_url);
                } else {
                    // `上传头像`失败
                    alert(resp.errmsg);
                }
            }
        })

    })


})
