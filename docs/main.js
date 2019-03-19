"use strict";

// 处理地图
$(function () {
    $(".mapFull").each(function () {
        $(this).wrap($("<div/>").addClass("mapFullBox"));
        $(this).css({
            "background-image": "url(" + this.dataset.image + ")",
            "width": this.dataset.width + "px",
            "height": this.dataset.height + "px"
        });
        if (+this.dataset.display) {
            $(this).css({
                "transform": "scale(" + +this.dataset.display / +this.dataset.width + ")",
                "font-size": +this.dataset.width / +this.dataset.display + "em",
                "line-height": "1.5em",
                "margin": (+this.dataset.display / +this.dataset.width * +this.dataset.height - +this.dataset.height) / 2 + "px " + (+this.dataset.display - +this.dataset.width) / 2 + "px"
            });
            $(this.parentElement).css({
                "width": this.dataset.display + "px",
                "height": +this.dataset.display / +this.dataset.width * +this.dataset.height + "px"
            });
        } else {
            $(this.parentElement).css({
                "width": this.dataset.width + "px",
                "height": this.dataset.height + "px"
            });
        }
        if (this.dataset.highlight) {
            var hl = this.dataset.highlight.split(",").map(x => +x - 1),
                children = this.children;
            for (var i = 0; i < hl.length; i++) {
                if (children[hl[i]]) {
                    $(children[hl[i]]).addClass("mapHighlight");
                }
            }
        }
        if (this.dataset.codeOnly) {
            $(this.parentElement).css({
                "width": +$(this.parentElement).css("width").slice(0, -2) + 150 + "px"
            });
            $("<ol/>").addClass("mapCode").css({
                "height": $(this.parentElement).css("height")
            }).prependTo($(this.parentElement));
        }
    })
    $(".map").each(function (n) {
        $(this).css({
            "left": this.dataset.x + "px",
            "top": this.dataset.y + "px",
            "width": this.dataset.width + "px",
            "height": this.dataset.height + "px"
        }).attr({
            "title": this.dataset.nameChs
        });
        if (!this.parentElement.dataset.highlightOnly || this.classList.contains("mapHighlight")) {
            if (this.parentElement.dataset.codeOnly) {
                $("<span/>").text(n + 1).appendTo($(this).empty());
                $("<li/>").text(this.dataset.nameChs).attr({
                    "value": n + 1
                }).appendTo($(this.parentElement.parentElement).find(".mapCode"));
            } else {
                $("<span/>").text(this.dataset.nameChs).appendTo($(this).empty());
            }
        }
    });
});