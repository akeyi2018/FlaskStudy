window.onload = () => {
    var $front_elem = document.getElementById("front");
    $front_elem.onclick = () => { 
        // $front_elem.innerHTML = 'MOVE';
        move_front('move to front');
    };

    // $front_elem.onmouseup = () => {
    //     $front_elem.innerHTML = '前進';
    //     output_info('stop to move front!', 0);
    // };
    var $back_elem = document.getElementById("back");
    $back_elem.onclick = () => { 
        // $back_elem.innerHTML = 'MOVE';
        output_info('move to back', 2);
    };

    var $left_elem = document.getElementById("left");
    $left_elem.onmousedown = () => { 
        output_info('move to left', 3);
    };

    // $left_elem.onmouseup = () => {
    //     $left_elem.innerHTML = '後退';
    //     output_info('stop to move back', 0);
    // };
    var $right_elem = document.getElementById("right");
    $right_elem.onmousedown = () => { 
        // $right_elem.innerHTML = 'MOVE';
        output_info('move to right', 4);
    };

    var $right_elem = document.getElementById("stop");
    $right_elem.onmousedown = () => { 
        // $right_elem.innerHTML = 'MOVE';
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

function move_front($text_info) {
    var res = JSON.stringify( { "d": 1 } );
    var $info = document.getElementById('info');
    $info.innerHTML = $text_info;
    $.ajax(
      {
        type:'POST',
        url: '/move_front',
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
    $.ajax(
      {
        type:'POST',
        url: '/move',
        data: res,
        contentType: 'application/json'
      });
}
