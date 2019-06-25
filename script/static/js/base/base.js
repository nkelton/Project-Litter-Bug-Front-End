$(document).ready(function () {
    var calendar = {};
    navbarListener();

    $(function(){
        $('#cal').datepicker({
                dateFormat: 'mm-dd-yyyy',
                todayHighlight: true,
                autoclose: true})
        .on("changeDate", function (e) {
                calendar["day"] = e.date.getDate();
                calendar["month"] = e.date.getMonth() + 1;
                calendar["year"] = e.date.getFullYear();
        });
    });

    $(function(){
        $("#litter-date-search-btn").click(function(e){
            if ("month" in calendar && "day" in calendar && "year" in calendar) {
                window.location.href =  results + "?month=" + calendar["month"] +
                                        "&day=" + calendar["day"] + "&year=" + calendar["year"];
            }
        });
    });
});

function navbarListener() {
    var links = $('.navbar ul li a');
    $.each(links, function (key, va) {
        if (va.href == document.URL) {
            $(this).addClass('active');
        }
    });
}





