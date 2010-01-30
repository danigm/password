function vote(){
    rate = $(this).parent();
    to_load = $(this).attr("href");
    $.get(to_load+".json", {}, function(data){
        rate.parent().find(".votes").html(data.votes);
        rate.parent().find(".rate_percentage").html(data.rate);
        rate.fadeOut();
        rate.html("thanks");
        rate.fadeIn();
    }, "json");
    return false;
}


$(document).ready(function(){
    $("#search").focus(function(){
        $(this).val("");
    });

    $(".voteyes").click(vote);
    $(".voteno").click(vote);
});
