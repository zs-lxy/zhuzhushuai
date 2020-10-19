// JavaScript Document
$(function () {
    $(window).scroll(function () {
        var sTop = $(window).scrollTop();
        if (sTop >= 60) {
            $(".nav").css('position', 'fixed');
        }
        else {
            $(".nav").css('position', 'relative');
        }
    })
    $(".all").hover(function () {
        $(".expose .item:eq(0)").toggleClass('hover');
        $(".nav-exposed").show();
        var nav_height = $('.nav_new').height();
        $('.nav_new').height(nav_height);
    }, function () {
        $(".expose .item").removeClass('hover');
        $(".nav-exposed").hide();
    })
});



