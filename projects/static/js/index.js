"use strict";
(function() {
    $(document).ready(function(){
        var $pModal = $('#project-modal');

        $('.project > figure').on('click', function(event) {
            // don't open the modal if we're going somewhere else
            if (event.target.tagName.toLowerCase() === 'a') {
                return;
            }

           // fill the modal
            event.preventDefault();
            $pModal.html(this.innerHTML);
            $pModal.append('<a class="close-reveal-modal">&#215;</a>');
            $pModal.foundation('reveal', 'open');
        });

        // subnav
        var $employerSelect = $('#employer-select');
        var $comProjectsContainer = $('#paid-projects');
        var $comProjects = $comProjectsContainer.find('.project');

        // subnav selection events
        $employerSelect.on('click', 'a', function (event){
            event.preventDefault();
        });
        $employerSelect.on('click', 'dd', function (event){
            // todo: more flexible implementation. maybe data-?
            var classList = event.currentTarget.classList;

            // ignore clicks on active selection
            if (event.currentTarget.className.indexOf('active') !== -1) {
                return;
            }
            if (classList.length > 0) {
                var slug = event.currentTarget.classList[0];
                // show everything
                if (slug === 'all') {
                    $comProjects.fadeIn('fast');
                }

                // only show matching slug
                else {
                    $comProjects.hide().promise().done(function() {
                        $comProjectsContainer.find('.' + slug).fadeIn('fast');
                    });
                }
            }

            // visual cue
            $employerSelect.find('.active').removeClass('active');
            $(event.currentTarget).addClass('active');
        });

    });
})();
