"use strict";
(function() {
    $(document).ready(function(){
        var $pModal = $('#project-modal');

        $('.project').on('click', function(event) {
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
    });
})();
