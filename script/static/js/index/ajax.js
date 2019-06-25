function aggregateDataQuery() {
    $.ajax({
        type: "GET",
        url: "/ajax/aggregateData/",
        success: function(data) {
            contentData["life_stats"] = data;
            updateIFrame(contentData["life_stats"].embedded_url);
            updateLifeStats(contentData["life_stats"]);
        }
    });
}