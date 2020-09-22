$(document).ready(function () {
    $('#sidenavToggler').click(function () {
        $('.sidenav').toggleClass('showNav');
        $("i").toggleClass("fa-times");
        $(".navToggle").toggleClass("navToggleActive");
    });
    $('#datePicker').datepicker({ dateFormat: 'yy-mm-dd' });
    $('.sidenav a').click(function () {
        $('.sidenav').toggleClass('showNav');
        $("i").toggleClass("fa-times");
        $(".navToggle").toggleClass("navToggleActive");
    });
});