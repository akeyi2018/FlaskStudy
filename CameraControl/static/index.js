function reset(){
    $.post("/reset_json", "", function(data, status, xhr){
        if (status == "success") {
            $("#text_status").html("インターバル撮影が完了しました。")
        }
    });
}

function stop(){
    $.post("/stop", "", function(data, status, xhr){
        if (status == "success") {
            $("#text_status").html("インターバル撮影を停止しました。")
        }else{
            console.log("NG")
        }
    });
}

function getjson(){
    $.getJSON("/get_json", "", function(data){
        const res = data.status;
        $("#interval").val(res);
        if (data.running == 0){
            $("#text_status").html("インターバル撮影が完了しました。");
            $("#interval").val(0);
        }
    });
}

function changeProgress() {
    var id = setInterval(function(){   
        const res = $("#text_status").html();
        if (res == "インターバル撮影実行中"){
            getjson();
        }else{
            clearInterval(id);
        }}, 1000);
}