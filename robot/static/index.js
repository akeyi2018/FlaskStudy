window.onload = () => {
    var $front_elem = document.getElementById("front");
    $front_elem.onmousedown = () => { 
        $front_elem.innerHTML = 'MOVE';
        output_info('move to front', 1);
    };

    $front_elem.onmouseup = () => {
        $front_elem.innerHTML = '前進';
        output_info('stop to move front!', 0);
    };
    var $back_elem = document.getElementById("back");
    $back_elem.onmousedown = () => { 
        $back_elem.innerHTML = 'MOVE';
        output_info('move to back', 2);
    };

    $back_elem.onmouseup = () => {
        $back_elem.innerHTML = '後退';
        output_info('stop to move back', 0);
    };
    var $left_elem = document.getElementById("left");
    $left_elem.onmousedown = () => { 
        $left_elem.innerHTML = 'MOVE';
        output_info('move to left', 3);
    };

    $left_elem.onmouseup = () => {
        $left_elem.innerHTML = '後退';
        output_info('stop to move back', 0);
    };
    var $right_elem = document.getElementById("right");
    $right_elem.onmousedown = () => { 
        $right_elem.innerHTML = 'MOVE';
        output_info('move to right', 4);
    };

    $right_elem.onmouseup = () => {
        $right_elem.innerHTML = '後退';
        output_info('stop to move back', 0);
    };
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
