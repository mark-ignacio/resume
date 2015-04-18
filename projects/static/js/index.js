"use strict";

(function () {

    // cache a bunch of selectors
    var $window = $(window);
    var $index = $('#index');
    var $lpages = $('#other-lpages');

    var pages = [
        [null, 'index', null],
        ['dev', 'security', 'hobby'],
        [null, 'about', null]
    ];
    var currentPage = [0, 1];

    function loadPage(page, direction) {
        var $page = $(page);
        var $oldPage = $('#' + pages[currentPage[0]][currentPage[1]]);
        // animate current page going up

        switch (direction) {
            case 'up':
                $page.css({
                    top: $window.height() * 2,
                    left: 0,
                    right: 0,
                    bottom: $window.height()
                });
                break;
            case 'down':
                $page.css({
                    top: $window.height(),
                    left: 0,
                    right: 0,
                    bottom: $window.height() * 2
                });
                break;
            default:
                break;
        }

        $oldPage.animate(
            {top: $window.height() * -1},
            function () {
                $oldPage.css({top: -9999})
            }
        );
        $page.animate({
            top: 0,
            bottom: 0,
            left: 0,
            right: 0
        });
    }

    // vim keybinds are ok
    $(document.body).keyup(function (e) {
        if ((e.which === 40 || e.which === 74)) {
            loadPage('#security', 'down');
        }
    });

    // on startup and scroll, resize
    var sectionResize = function () {
        var windowHeight = $window.height();
        $index.height(windowHeight);
        $lpages.css({top: windowHeight});
    };

    $window.resize(sectionResize);
    sectionResize();
})();