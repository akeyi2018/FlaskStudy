window.onload = () => {
    var $front_elem = document.getElementById("front");
    $front_elem.onmousedown = () => { 
        inter_id = setInterval(
            function(){
                $front_elem.innerHTML = 'MOVE';
                output_info('move to front', 1);
            }, 20); 
    };

    $front_elem.onmouseup = () => {
        clearInterval(inter_id);
        $front_elem.innerHTML = '前進';
        output_info('stop to move front!');
    };
    var $back_elem = document.getElementById("back");
    $back_elem.onmousedown = () => { 
        inter_id_2 = setInterval(
            function(){
                $back_elem.innerHTML = 'MOVE';
                output_info('move to back', 2);
            }, 20); 
    };

    $back_elem.onmouseup = () => {
        clearInterval(inter_id_2);
        $back_elem.innerHTML = '後退';
        output_info('stop to move back');
    };
}
 
function output_info($text_info, direction) {
    var res = JSON.stringify({"d": direction});
    $.ajax(
      {
        type:'POST',
        url: '/move',
        data: res,
        contentType: 'application/json'
      }
    );
    // $.post("/move", $text_info, function(res, status, xhr){
    //     if (status == "success") {
    //       $info_elem = document.getElementById("info");
    //       $info_elem.innerHTML = $text_info + direction;
    //     }
    // });
}
