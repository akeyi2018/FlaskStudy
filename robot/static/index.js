window.onload = () => {
    var $front_elem = document.getElementById("front");
    $front_elem.onclick = () => { 
        output_info('move to front', 1);
    };

    var $back_elem = document.getElementById("back");
    $back_elem.onclick = () => { 
        output_info('move to back', 2);
    };

    var $left_elem = document.getElementById("left");
    $left_elem.onmousedown = () => { 
        output_info('move to left', 3);
    };

    var $right_elem = document.getElementById("right");
    $right_elem.onmousedown = () => { 
        output_info('move to right', 4);
    };

    var $right_elem = document.getElementById("stop");
    $right_elem.onmousedown = () => { 
        stop(0);
    };
}
 
function stop(direction) {
    var res = JSON.stringify(
        {
            "d": direction
        }
        );
    $.ajax(
      {
        type:'POST',
        url: '/stop',
        data: res,
        contentType: 'application/json'
      });
}

function output_info($text_info, direction) {
    var res = JSON.stringify(
        {
            "d": direction
        }
        );
    var $info = document.getElementById('info');
    $info.innerHTML = $text_info;
    $.ajax(
      {
        type:'POST',
        url: '/move',
        data: res,
        contentType: 'application/json'
      });
}
