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

// 房间道具
$(function () {
    $(".roomItem").each(function () {
        var item = this.dataset.item,
            i;
        for (i = 0; i < item.length; i++) {
            var title;
            switch (item[i]) {
                case "奇":
                    title = "奇诺比奥，可以保存。如果使用 amiibo 则可以回复体力。";
                    break;
                case "镜":
                    title = "镜子。用 Game Boy Horror 照射可以返回到大厅。";
                    break;
                case "火":
                case "水":
                case "冰":
                    title = item[i] + "之元素。获得" + item[i] + "之元素奖章后可以吸入并喷出" + item[i] + "之元素。";
                    break;
                case "心":
                    title = "可能会出现回复较多体力的心。"
                    break;
            }
            $("<span/>").addClass("roomItem" + item[i]).text(item[i]).attr({
                "title": title
            }).appendTo($(this));
        }
    });
});