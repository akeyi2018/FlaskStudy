// import {jsPDF} from "jspdf";
//メイン関数
function main_function(num, val)
{
    let button_elem = document.querySelectorAll('#btn')[num];
    // メールアドレス取得
    let mail_add = document.querySelector('.user-level').textContent;

    let select_date = document.getElementById("Select1").value;
    // console.log(select_date);
    let dt_now = getFirstOfPreviousMonth(new Date());
    console.log(dt_now);

    if (select_date == dt_now){
        console.log('OK');
    }else{
        console.log('NG');
    }


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
                    const mail_add = data.mail;
                    //フラグが1の場合
                    if(flg == 1)
                    {
                        alert('[' + mail_add + ']が編集しているため、編集できません。')
                    }
                    else
                    //フラグが0の場合
                    {
                        //コメント欄を最新にする
                        get_latest_comment(num);
                        //サーバー側にフラグ1をセットする
                        post_write_flg(num, mail_add, 1);
                        sessionStorage.setItem("write_flg", 1)
                        alert('編集が可能となりました。');
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
        let data = document.querySelectorAll('textarea')[num].value;
        
        // 全角文字チェック
        if (containsFullWidth(data)) {    
        //全角文字
            alert('全角文字があります。');
        } else {

            post_comment_to_server(num, data, mail_add);
            alert('編集したデータの送信が完了しました。');
            sessionStorage.setItem("write_flg", 0)
            //ボタン名を変更
            button_elem.value="編集開始";
        }
    }
}

function containsFullWidth(str) {
    var fullWidthRegex = /[^\x01-\x7E\xA1-\xFF]/; // 全角文字の正規表現
    return fullWidthRegex.test(str);
}

function getFirstOfPreviousMonth(date) {
    let result = new Date(date.getFullYear() - (date.getMonth() ? 0 : 1), (date.getMonth() + 11) % 12, 1);
    let dt = new Date(result.getTime() - result.getTimezoneOffset() * 60000);
    let dt_y = dt.getFullYear();
    let dt_m = 1 + dt.getMonth();
    let dt_m_str = dt_y + '-' + ('0' + dt_m).slice(-2);
    return dt_m_str;
}

//コメント欄を最新にする
function get_latest_comment(num){
    fetch('/get_comment/' + num)
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
                    const flg = data.data;
                    console.log(flg);
                    document.querySelectorAll('textarea')[num].value = flg;
                }
                )
            }
        )    
}

//サーバー側に書き込みフラグ1をセットする
function post_write_flg(flag, mail_add, value){
    fetch('/write_flg/' + flag, 
    {
        method: 'POST',
        headers: 
        {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(
            {
                param: value,
                mail: mail_add 
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

function post_comment_to_server(num, data, mail_add){
    fetch('/save_comment/' + num,
    {
        method: 'POST',
        headers:
        {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(
            {
                comment: data,
                mail: mail_add
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

function save_pdf_main(){
    const num = [0, 1];
    const id = ['myChart_1','myChart_2']
    let pdf = new jsPDF('landscape');
    for (let i = 0; i < id.length; i++ ){
        save_pdf(pdf, num[i], id[i], id.length);
    }
    pdf.save('result.pdf');
}

function save_pdf(pdf, num, id, max_n){
    let data = document.querySelectorAll('textarea')[num].value;
    const pdfchart = document.getElementById(id);
    const ctx = pdfchart.getContext('2D');
    const pdfImage = pdfchart.toDataURL('image/png', 1.0);
    const wd = pdf.internal.pageSize.width-10;
    const h = pdf.internal.pageSize.height-50;
    pdf.setFontSize(12);
    pdf.setPage(num + 1);
    pdf.addImage(pdfImage, 'PNG', 5, 5, wd, 0);
    pdf.text(5,h,data);
    if (num < max_n-1){
        pdf.addPage();
    }
}

// window.addEventListener('beforeunload', (e) => {
//     e.returnValue = '保存忘れはありませんか？';
//     });


// TESTER = document.getElementById('tester');

// Plotly.plot(TESTER, [{
//     x: [1, 2, 3, 4, 5],
//     y: [1, 2, 4, 8, 16] }], { 
//     margin: { t: 0 } }, {showSendToCloud:true} );