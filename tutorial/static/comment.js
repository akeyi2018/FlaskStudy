//メイン関数
function main_function(num, val)
{
    let button_elem = document.querySelectorAll('#btn')[num];
    // let button_elem = button_elem_all[comment_area_val];
    console.log(button_elem.value);
    // console.log(comment_area_val);
    //ボタンが「編集開始」の場合
    if (val=="編集開始")
    {
        //サーバーの編集フラグをチェックする
        fetch('/write_flg/' + num)
            .then(function(response)
            {
                //レスポンスが200でない場合
                if(response.status!=200)
                {
                    console.log(response.statusText);
                }
                //結果の取得
                response.json().then(function(data)
                {
                    const flg = data.flag;
                    //フラグが1の場合
                    if(flg == 1)
                    {
                        console.log('編集不可');
                    }
                    else
                    //フラグが0の場合
                    {
                        console.log('編集可能');
                        //サーバー側にフラグ1をセットする
                        post_write_flg(num, 1);
                        //ボタン名を変更
                        button_elem.value="編集終了"; 
                    }
                }
                )
            }
        );
    }
    else
    {
        //textareaのデータを取得する
        let data = document.querySelector('textarea').value;
        post_comment_to_server(data);
    }
}

//サーバー側に書き込みフラグ1をセットする
function post_write_flg(flag, value){
    fetch('/write_flg/' + flag, 
    {
        method: 'POST',
        headers: 
        {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(
            {
                param1: value
            }
            )
        }).then(function(response){
            if(response.status!=200)
            {
                console.log(response.statusText);
            }
    }
    )     
}

function post_comment_to_server(data){
    console.log(data);
}

window.addEventListener('beforeunload', function(e) {
    e.returnValue = '保存忘れはありませんか？';
    },
    false 
  );

$(window).on('beforeunload', function(e){
    e.returnValue = '保存忘れはありませんか？';
});