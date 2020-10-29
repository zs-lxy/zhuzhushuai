// JavScript Document

$(function () {
    // alert(11)
    $('#open_login').click(function () {

        /////需要检查是否已经登录过了
        showLoginBox("imgBox");
        LI0(0);
        checkLogin("login")
    });
    $('#open_reg').click(function () {
        showLoginBox("imgBox");
        LI0(1);
        checkLogin("reg")
    });

})


function open_login() {
    alert(2)
    /////需要检查是否已经登录过了
    // showLoginBox("imgBox");
    // LI0(0);
    // checkLogin("login")
}

function checkLogin(text) {
    $.ajax({
        url: "/index/order_form_ooo",
        type: 'post',
        dataType: 'json',
        data: {},
        success: function (data) {
            if (data.error == 1) {
                if (text == "reg") {
                    showLoginBox("imgBox");
                    LI0(1);
                } else {
                    showLoginBox("imgBox");
                    LI0(0);
                }
            } else {
                if (text == "checkout") {
                    ///获取优惠券的号
                    var param = "";
                    var coupon_no = $("#coupon_card").val();
                    if (coupon_no) {
                        param = "&N=" + coupon_no;
                    }
                    window.location.href = "/" ;
                } else {
                    window.location.href = "/";
                }
            }
        }
    });
}

function LI0(i) {
    $(".log_box li").each(function (index) {
        var class_value = $(this).attr("class");
        var j = "";
        switch (i) {
            case 1:
                j = 0;
                break;
            default:
                j = 1;
                break;
        }
        if (index == i) {
            if (class_value.indexOf("selected")) {//
                $(this).addClass("selected" + i);
            }
        } else {
            if (class_value.indexOf("selected")) {
                $(this).removeClass("selected" + j);
            }
        }
        ////
    });
    $(".login .tab_block").each(function (ids, obj) {
        if (ids == i) {
            $(obj).show();
        } else {
            $(obj).hide();
        }
    });

}

function showLoginBox(obj) {
    easyDialog.open({
        container: obj,
        autoClose: 0,
        fixed: true
    });
};
//
// function reg_submit() {
//     var flag = 0;
//     var forware = window.location.href
//     var email = $("#email").val();
//     var password = $("#password").val();
//     var confirm_password = $("#confirm_password").val();
//     var captcha = $("#captcha").val();
//     var agreement = $("#agreement").val();
//
//     var rephone = /^(13[0-9]|14[0-9]|15[0-9]|17[0-9]|18[0-9])[0-9]{8}$/;  // /^(1(([35][0-9])|(47)|[8][0126789]))\d{8}$/;
//     var remail = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/;
//     //过滤表单
//     //提交表单
//     if (!email) {
//         alert("账号不能为空");
//         return false;
//     } else if (!rephone.test(email) && !remail.test(email)) {
//         alert("请输入格式正确的手机号码或邮箱地址！");
//
//         return false;
//     } else if (!password) {
//         alert("密码不能为空");
//         return false;
//     } else if (!confirm_password) {
//         alert("确认密码不能为空");
//         return false;
//     } else if (confirm_password != password) {
//         alert("两次密码输入不一致");
//         return false;
//     }/*else if(!captcha){
// 				 alert("验证码不能为空");
// 				 return false;
// 			 }else if(!agreement){
// 				 alert("请查阅并勾选用户协议");
// 				 return false;
// 			 }*/
//     var url = 'user.php';
//     $.ajax({
//         url: url,
//         type: 'post',
//         dataType: 'json',
//         data: {act: "sregister", agreement: agreement, username: email, password: password},
//         success: function (data) {
//
//             if (data.error == 0) {
//               alert("登陆成功")
//             } else {
//                 confirm("对不起，您输入的用户名或密码不正确！");
//             }
//         },
//         error: function () {
//
//             confirm("对不起，您输入的用户名或密码不正确！");
//         }
//     });
//
// }


//
// function login_submit() {
//     var flag = 0;
//     var forware = window.location.href
//
//     var username = $("#user_name").val();
//     var passwd = $("#passwd").val();
//     ////过滤表单
//     //提交表单
//     var url = '/passport/login_btn';
//     $.ajax({
//         url: url,
//         type: 'post',
//         dataType: 'json',
//         data: {act: "signin", username: username, password: passwd, back_act: forware},
//         success: function (data) {
//             if (data.error == 0) {
//                 $("#ucdata").html(data.ucdata);
//                 $("#js-login-info").html('<a class="top-logout" href="user.php?act=logout">退出</a>  <span class="vip" style="display: none;"></span> <p>您好, <a href="user.php">' + username + '</a></p>')
//                 $("#js-coupon").show();
//                 easyDialog.close();
//                 //跳转到某页面
//             } else {
//                 confirm("对不起，您输入的用户名或密码不正确！");
//             }
//         },
//         error: function () {
//             alert(forware);
//             confirm("对不起，您输入的用户名或密码不正确！");
//         }
//     });
//
// }

/******/
function checkCoupon(coupon_sn) {
    $.ajax({
        type: "post",
        dataType: "json",
        url: "check_coupon.php",
        data: "step=check_sn&coupon_sn=" + coupon_sn,
        success: function (msg) {
            if (msg.error == 1) {
                alert(msg.content);
            } else {
                $("#js-order-total").html(msg.content);
                $("#show_tP").html(msg.total_p);
                ///修改优惠和修改价格
                //alert(msg.content);
            }
        }
    })
}


$(function () {
    $("#login_lqy").click(function () {
        var username = $("#user_name").val();
        var passwd = $("#passwd").val();
        par = {
            "username": username,
            "passwd": passwd
        }
        $.ajax({
            type: "post",
            dataType: "json",
            url: "/passport/login_btn",
            data: JSON.stringify(par),
            contentType: "application/json",
            success: function (resp) {
                if (resp.errno == '0') {
                    alert(resp.errmsg);
                    window.location.href = '/'
                } else {
                    alert(resp.errmsg);
                    // window.location.reload()
                }

            }
        })
    })

})

$(function () {
    $("#register_zs").click(function () {
        var mobile = $("#mobile").val();
        var nick_name = $("#nick_name").val();
        var password = $("#password").val();
        var confirm_password = $("#confirm_password").val();
        var captcha = $("#captcha").val();
        var agreement = $("#agreement").val();

        par = {
            "mobile": mobile,
            "password": password,
            "confirm_password": confirm_password,
            "captcha": captcha,
            "agreement": agreement,
            "nick_name": nick_name
        }
        $.ajax({
            type: "post",
            dataType: "json",
            url: "/passport/register_btn",
            data: JSON.stringify(par),
            contentType: "application/json",
            success: function (resp) {
                if (resp.errno == '0') {
                    alert(resp.errmsg);
                    window.location.href = '/'
                } else {
                    alert(resp.errmsg);
                    // window.location.reload()
                }

            }
        })
    })

})





// 生成一个图片验证码的编号，并设置页面中图片验证码img标签的src属性
function generateImageCode() {
    // 1. 生成一个编号
    // 严格一点的使用uuid保证编号唯一， 不是很严谨的情况下，也可以使用时间戳
    imageCodeId = generateUUID();

    // 2. 拼接验证码地址
    var imageCodeUrl = "/passport/image_code?code_id=" + imageCodeId;
    // 3. 设置页面中图片验证码img标签的src属性
    $(".get_pic_code").attr("src", imageCodeUrl)
}

function generateUUID() {
    var d = new Date().getTime();
    if (window.performance && typeof window.performance.now === "function") {
        d += performance.now(); //use high-precision timer if available
    }
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = (d + Math.random() * 16) % 16 | 0;
        d = Math.floor(d / 16);
        return (c == 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
    return uuid;
}

// 一般页面的iframe的高度是660
// 新闻发布页面iframe的高度是900
function fnSetIframeHeight(num){
	var $frame = $('#main_frame');
	$frame.css({'height':num});
}