//グルーピング
function save_pdf_main_p1(pdf_file_name){
    //コメントIDの設定情報
    const comment_num = [
        ['btn_001'],
        ['btn_002']
    ];
    //グラフのグルーピングの設定情報
    const graph_gr_id = [
        ['ScatterChart','myChart_1','myChart_2'],
        ['myChart_3','myChart_4']
    ];

    //pdfの変数宣言
    let pdf = new jsPDF('landscape');
    pdf.setTextColor(255, 255, 255);
    let title_ct = 0;
    //pdf作成ループ
    for (let i = 0; i < comment_num.length; i++){
        //セットするグラフIDを取得
        graph_id = graph_gr_id[i];
        max_page = comment_num.length;
        //グラフチャートの個数で分岐
        switch(graph_id.length){
            case 3:
                save_pdf_03(pdf,comment_num[i],graph_id,i,max_page,title_ct);
                break;
            case 2:
                save_pdf_02(pdf,comment_num[i],graph_id,i,max_page,title_ct);
                break;
            default:
                console.log("nothing");
                break;
        }
        //タイトルカウント
        title_ct = title_ct +  (graph_id.length);
        console.log(title_ct);
    }
    pdf.save(pdf_file_name);
}

//差し替え

function save_pdf_test(pdf_file_name){
    //グラフの数とコメントの数が異なる為、工夫が必要
    const comment_num = [0, 1];
    const graph_id = ['ScatterChart','myChart_1','myChart_2']
    let pdf = new jsPDF('landscape');
    // for (let i = 0; i < id.length; i++ ){
    //     save_pdf(pdf, num[i], id[i], id.length);
    // }
    // save_pdf_06(pdf, 0, graph_id);
    save_pdf_with_table(pdf, 0, graph_id);
    pdf.save(pdf_file_name);
}

function save_pdf_with_table(pdf, num, id){
    //コメントデータの取得
    let data = document.querySelectorAll('textarea')[num].value;
    const wd = pdf.internal.pageSize.width;
    const h = pdf.internal.pageSize.height-50;
    
    //背景を作成する
    pdf.setPage(1);
    // pdf.setFillColor(52, 58, 64);
    pdf.setFillColor(240,240,240);
    pdf.rect(0, 0, wd, h, "FD");
    
    //1個目のグラフのイメージを作成する
    //タイトル文字列の取得
    let title_01 = document.getElementsByClassName('card-title')[0].innerHTML;
    pdf.text(5, 5, title_01);
    const pdfchart_01 = document.getElementById(id[0]);
    const pdfImage_01 = pdfchart_01.toDataURL('image/png', 1.0);
    pdf.addImage(pdfImage_01, 'PNG', 5, 15, wd/3-5, 0);

    //テーブルデータ取得
    let table_data = document.getElementsByClassName('table table-hover')[0];
    var headers = get_table_header(table_data);
    // var headers = createHeaders([
    //     "id",
    //     "coin",
    //     "game_group",
    //     "game_name",
    //     "game_version",
    //     "machine",
    //     "vlt"
    //   ]);
    console.log(headers);

    pdf.table(1, h-20, generateData(table_data, headers), headers);

}

function get_table_header(table){
    // ヘッダー取得
    var table_th = [];
    for (let cell of table.rows[0].cells){
        table_th.push(cell.innerText);   
    }
    var table_header = createHeaders(table_th);
    return table_header;

}

function generateData(table, header){
    var result = [];
    //テーブルの列数を取得する
    var col = table.rows[0].cells.length;
    // console.log(table.rows[1].cells[1].innerHTML);
    // console.log(header[]);
    for (let i = 0; i < table.rows.length; i++){
        for (let j = 0; j < col-1; j ++){
            // console.log(table.rows[i+1].cells[j].innerHTML);
            // console.log(header[i].id);
            str_01 = table.rows[i].cells[j].innerHTML.toString();
            header[i].id = str_01;
            // result.push(Object.assign({}, header));
            // data[table.rows[0].cells[j].innerHTML.toString()] = table.rows[i].cells[j].innerHTML;
        }
        result.push(Object.assign({}, header));
        // result.push(Object.assign({}, data));
    }
    console.log(result); 
    return result;
}

var generateData_ori = function(amount) {
    var result = [];
    var data = {
      no: "100",
      game_group: "GameGroup",
      game_name: "XPTO2",
      game_version: "25",
      machine: "20485861",
      vlt: "0"
    };
    for (var i = 0; i < amount; i += 1) {
      data.no = (i + 1).toString();
      result.push(Object.assign({}, data));
    }
    console.log(result);
    return result;
  };
  
  function createHeaders(keys) {
    var result = [];
    for (var i = 0; i < keys.length; i += 1) {
      result.push({
        id: keys[i],
        name: keys[i],
        prompt: keys[i],
        width: 50,
        height: 5,
        align: "center",
        padding: 0
      });
    }
    return result;
  }
  
  
  
function save_pdf_06(pdf, num, id){
    //コメントデータの取得
    let data = document.querySelectorAll('textarea')[num].value;
    const wd = pdf.internal.pageSize.width;
    const h = pdf.internal.pageSize.height;
    
    //背景を作成する
    pdf.setPage(1);
    pdf.setFillColor(26, 32, 53);
    // pdf.setFillColor(240,240,240);
    pdf.rect(0, 0, wd, h, "FD");

    let c_h_l = 10;
    let c_h_u = 10;
    let c_h_u_2 = 10;
    let lo_ = h/2 - 30;
    let lo_2 = h/2 - 30;
    //1個目のグラフのイメージを作成する
    //タイトル文字列の取得
    let title_01 = document.getElementsByClassName('card-title')[0].innerHTML;
    pdf.text(5, 5, title_01);
    const pdfchart_01 = document.getElementById(id[0]);
    const pdfImage_01 = pdfchart_01.toDataURL('image/png', 1.0);
    pdf.addImage(pdfImage_01, 'PNG', 5, c_h_u, wd/3-5, lo_);
    
    //2個目のグラフのイメージを作成する
    //タイトル文字列の取得
    let title_02 = document.getElementsByClassName('card-title')[1].innerHTML;
    pdf.text(5+wd/3, 5, title_02);
    const pdfchart_02 = document.getElementById(id[1]);
    const pdfImage_02 = pdfchart_02.toDataURL('image/png', 1.0);
    pdf.addImage(pdfImage_02, 'PNG', 5+wd/3, c_h_u, wd/3-5, lo_);

    //3個目のグラフのイメージを作成する
    //タイトル文字列の取得
    let title_03 = document.getElementsByClassName('card-title')[2].innerHTML;
    pdf.text(5+(wd/3)*2, 5, title_03);
    const pdfchart_03 = document.getElementById(id[2]);
    const pdfImage_03 = pdfchart_03.toDataURL('image/png', 1.0);
    pdf.addImage(pdfImage_03, 'PNG', 5+(wd/3)*2, c_h_u, (wd/3)-5, lo_);

    //4個目のグラフのイメージを作成する
    //タイトル文字列の取得
    let title_04 = document.getElementsByClassName('card-title')[0].innerHTML;
    pdf.text(5, h/2-c_h_u_2, title_04);
    const pdfchart_04 = document.getElementById(id[0]);
    const pdfImage_04 = pdfchart_04.toDataURL('image/png', 1.0);
    pdf.addImage(pdfImage_04, 'PNG', 5, h/2-c_h_u_2, wd/3-5, lo_2);
    
    //5個目のグラフのイメージを作成する
    //タイトル文字列の取得
    let title_05 = document.getElementsByClassName('card-title')[1].innerHTML;
    pdf.text(5+wd/3, h/2-c_h_u_2, title_05);
    const pdfchart_05 = document.getElementById(id[1]);
    const pdfImage_05 = pdfchart_05.toDataURL('image/png', 1.0);
    pdf.addImage(pdfImage_05, 'PNG', 5+wd/3, h/2-c_h_u_2, wd/3-5, lo_2);

    //6個目のグラフのイメージを作成する
    //タイトル文字列の取得
    let title_06 = document.getElementsByClassName('card-title')[2].innerHTML;
    pdf.text(5+(wd/3)*2, h/2-c_h_u_2, title_06);
    const pdfchart_06 = document.getElementById(id[2]);
    const pdfImage_06 = pdfchart_06.toDataURL('image/png', 1.0);
    pdf.addImage(pdfImage_06, 'PNG', 5+(wd/3)*2, h/2-c_h_u_2, (wd/3)-5, lo_2);
    pdf.setTextColor(255, 255, 255);
    pdf.text(5,h-30,data);

}

function set_page_header(pdf){
    //id_name
    let id = 'start_month';
    //タイトル
    let page_title = document.getElementsByClassName('page-title')[0].innerHTML;
    pdf.text(5, 5, page_title);
    //discription
    let page_dis = document.getElementsByClassName('page-category')[0].innerHTML;
    pdf.text(5, 10, page_dis);
    //select month
    let select_v = document.getElementById(id).options[document.getElementById(id).selectedIndex].text;
    pdf.text(5, 15, select_v);
    // console.log(select_v); 
}

function save_pdf_03(pdf, comment_num, graph_id, page_num, max_page,title_ct){
    //コメントデータの取得
    let data = document.getElementById(comment_num).value;
    const wd = pdf.internal.pageSize.width;
    const h = pdf.internal.pageSize.height;
    
    //背景を作成する
    // pdf.setPage(1);
    pdf.setFillColor(26, 32, 53);
    pdf.rect(0, 0, wd, h, "FD");
    set_page_header(pdf);
    
    //1個目のグラフのイメージを作成する
    //タイトル文字列の取得
    let title_01 = document.getElementsByClassName('card-title')[title_ct+0].innerHTML;
    pdf.text(5, 20, title_01);
    const pdfchart_01 = document.getElementById(graph_id[0]);
    const pdfImage_01 = pdfchart_01.toDataURL('image/png', 1.0);
    pdf.addImage(pdfImage_01, 'PNG', 5, 30, wd/3-5, 0);
    
    //2個目のグラフのイメージを作成する
    //タイトル文字列の取得
    let title_02 = document.getElementsByClassName('card-title')[title_ct+1].innerHTML;
    pdf.text(5+wd/3, 20, title_02);
    const pdfchart_02 = document.getElementById(graph_id[1]);
    const pdfImage_02 = pdfchart_02.toDataURL('image/png', 1.0);
    pdf.addImage(pdfImage_02, 'PNG', 5+wd/3, 30, wd/3-5, 0);

    //3個目のグラフのイメージを作成する
    //タイトル文字列の取得
    let title_03 = document.getElementsByClassName('card-title')[title_ct+2].innerHTML;
    pdf.text(5+(wd/3)*2, 20, title_03);
    const pdfchart_03 = document.getElementById(graph_id[2]);
    const pdfImage_03 = pdfchart_03.toDataURL('image/png', 1.0);
    pdf.addImage(pdfImage_03, 'PNG', 5+(wd/3)*2, 30, (wd/3)-5, 0);

    //コメント表示
    pdf.text(5,h-50,data);
    //ページ
    pdf.text(wd-15, h-5, 'P'+(page_num+1).toString());
    if (page_num < max_page - 1){
        pdf.addPage();
    }
}

function save_pdf_02(pdf, comment_num, graph_id, page_num, max_page, title_ct){
    //コメントデータの取得
    let data = document.getElementById(comment_num).value;
    const wd = pdf.internal.pageSize.width;
    const h = pdf.internal.pageSize.height;
    
    //背景を作成する
    // pdf.setPage(1);
    pdf.setFillColor(26, 32, 53);
    pdf.rect(0, 0, wd, h, "FD");
    set_page_header(pdf);

    //グラフタイトル文字列の取得
    let title_01 = document.getElementsByClassName('card-title')[title_ct+0].innerHTML;
    pdf.text(5, 20, title_01);
    //1個目のグラフのイメージを作成する
    const pdfchart_01 = document.getElementById(graph_id[0]);
    const pdfImage_01 = pdfchart_01.toDataURL('image/png', 1.0);
    pdf.addImage(pdfImage_01, 'PNG', 5, 30, wd/2, 0);
    let title_02 = document.getElementsByClassName('card-title')[title_ct+1].innerHTML;
    pdf.text(5+wd/2, 20, title_02);
    //2個目のグラフのイメージを作成する
    const pdfchart_02 = document.getElementById(graph_id[1]);
    const pdfImage_02 = pdfchart_02.toDataURL('image/png', 1.0);
    pdf.addImage(pdfImage_02, 'PNG', 5+wd/2, 30, wd/2, 0);

    //コメント表示
    pdf.text(5,h-50,data);
    //ページ
    pdf.text(wd-15, h-5, 'P'+(page_num+1).toString());
    if (page_num < max_page - 1){
        pdf.addPage();
    }

}

function save_pdf(pdf, num, id, max_n){
    let data = document.querySelectorAll('textarea')[num].value;
    const pdfchart = document.getElementById(id);
    const context = pdfchart.getContext('2d');
    const pdfImage = pdfchart.toDataURL('image/png', 1.0);
    const wd = pdf.internal.pageSize.width-10;
    const h = pdf.internal.pageSize.height-50;
    pdf.setFontSize(12);
    pdf.setPage(num + 1);
    pdf.setFillColor(52, 58, 64);
    pdf.rect(0, 0, wd, h, "FD");
    pdf.addImage(pdfImage, 'PNG', 5, 5, wd, 0);
    pdf.text(5,h+10,data);
    if (num < max_n-1){
        pdf.addPage();
    }
}