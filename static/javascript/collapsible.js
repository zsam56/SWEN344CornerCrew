$(function() {
    $(".comments-btn").click(function () {
        $header = $(this).parent().parent();
        //getting the next element
        $content = $header.next();
        //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
        $content.slideToggle(0, function () {
        });
    });
});