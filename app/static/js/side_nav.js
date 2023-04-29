// when user click on any nav link on the sidebar the color will be active and previous nav color may also change
$(document).ready(function() {
    $('.nav-link').click(function() {
        $('.nav-link').removeClass("active");
        $(this).addClass("active");
    });
});

$(function() {
    $('#sidebarCollapse').on('click', function() {
        $('#sidebar, #content').toggleClass('active');
    });
})
