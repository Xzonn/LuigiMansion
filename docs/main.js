"use strict";

$(function() {
    // 返回页面顶端
    $("#topLink").click(function(e) {
        $("html").animate({
            scrollTop: 0
        }, 500);
        e.preventDefault();
    });
});