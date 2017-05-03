$(function() {
    $("#comments").click(function () {
        $header = $(this).parent();
        //getting the next element
        $content = $header.next();
        //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
        $content.slideToggle(0, function () {
        });
        $(this).toggleClass("right_caret down_caret");
    });
});