// 出仓id
var storefromid = -1;
// 入仓id
var storeinrid = -1;
// 当前选择商品的按钮的index
var currentLineIndex = -1;

// 商品行数
var lineIndex = 0;



// 默认获取所有的仓库
getAllStore();

// 获取所有的仓库
function getAllStore() {
    var url = 'http://localhost:8085/api/store/list';
    // 获取数据列表
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            pageIndex: 0,
            pageSize: 10,
            key: ''
        },
        // datatype: "json",
        // contentType: "application/json",
        success: function (data) {
            if (data.success) {
                // data = JSON.parse(data);
                showStoreList(data);
            } else {
                // 显示失败
                showError('出错了', '获取仓库列表失败,请稍后重试');
            }
        },
        error: function (data) {
            // 显示失败
            iziToast.error({
                title: '出错了',
                position: 'topRight',
                message: '获取仓库列表失败,请刷新重试'
            });
        }
    });
}

// 显示仓库列表
function showStoreList(data) {
    $(".option_line").remove();
    var line = "<option class=\"option_line\" value=\"-1\" >请选择仓库</option>";
    $("#store_from_select").append(line);
    $("#store_in_select").append(line);
    // 显示列表
    for (var i = 0; i < data.data.length; i++) {
        var bean = data.data[i];
        var line = "<option class=\"option_line\" value=\"" + bean.id + "\" >" + bean.name + " </option>";
        $("#store_from_select").append(line);
        $("#store_in_select").append(line);
    }
}

// 获取出仓库的id
function getStoreFromId() {
    storefromid = $("#store_from_select").val();
    console.log("出仓库id:" + storefromid);
}

// 获取入仓库的id
function getStoreInId() {
    storeinrid = $("#store_in_select").val();
    console.log("入仓库id:" + storeinrid);
}

// 添加一行商品
function addLine() {
    var allLine = "<tr class=\"tr_add\" id='line_index_" + lineIndex + "'>\n" +
        "        <td>\n" +
        "            <div class=\"form-inline\">\n" +
        "                <input type=\"tel\" placeholder=\"选择商品\" class=\"form-control line_et_name\"\n" +
        "                       id='line_et_name_" + lineIndex + "'>\n" +
        "                <input type=\"hidden\" class='line_et_id' id='line_et_id_" + lineIndex + "'>\n" +
        "                <button style=\"margin: 5px\" class=\"btn btn-success table_btn_choose\" attr_index='" + lineIndex + "'>选择</button>\n" +
        "            </div>\n" +
        "\n" +
        "        </td>\n" +
        "\n" +
        "        <td><input type=\"number\" placeholder=\"选择数量\" min=\"1\" class=\"form-control line_et_size\" id='line_et_num_" + lineIndex + "'>\n" +
        "        </td>\n" +
        "\n" +
        "        <td><select class=\"form-control line_et_unit\">\n" +
        "            <option>选择单位</option>\n" +
        "\n" +
        "            <option>件</option>\n" +
        "\n" +
        "            <option>件</option>\n" +
        "\n" +
        "            <option>件</option>\n" +
        "\n" +
        "            <option>件</option>\n" +
        "\n" +
        "        </select>\n" +
        "        </td>\n" +
        "\n" +
        "        <td><input type=\"text\" placeholder=\"输入备注\" class=\"form-control line_et_desc\"></td>\n" +
        "\n" +
        "        <td>\n" +
        "            <button style=\"margin: 5px\" class=\"btn btn-danger table_btn_del\" attr_index='" + lineIndex + "'>删除</button>\n" +
        "        </td>\n" +
        "\n" +
        "    </tr>";
    $("#tbody").append(allLine);
    lineIndex++;
    // 点击删除的时候的响应时间
    $(".table_btn_del").click(function () {
        var trueIndex = $(this).attr("attr_index");
        $("#line_index_" + trueIndex).remove();
        // 刷新
        if ($(".table_btn_del").length==0){
            resetData();
        }
    });
    // 点击选择的时候
    $(".table_btn_choose").click(function () {
        currentLineIndex = $(this).attr("attr_index");
        // 获取商品列表
        $('#add_edit_modal').modal('show')
        // 获取商品列表
        getProById();
    });
    // 显示删除全部
    $("#change_all_btn_clear").show();
    $("#change_all_btn_save").show();


}

// 保存数据
function saveAllData() {
    // 检查是否有内容
    var size = $(".tr_add").length;
    if (size == 0) {
        showError("出错了", "请先添加商品");
        return;
    }
    // 检查数据
    var result = [];
    for (var i = 0; i < $(".tr_add").length; i++) {
        var id = $(".line_et_id").eq(i).val();
        var size = $(".line_et_size").eq(i).val();
        var unit = $(".line_et_unit").eq(i).val();
        var desc = $(".line_et_desc").eq(i).val();

        console.log(id);
        console.log(size);
        console.log(unit);
        console.log(desc);
        if (id == null || id == '') {
            showError("出错了", "未选择商品");
            return;
        }
        if (size == null || size == '') {
            showError("出错了", "请输入商品数量");
            return;
        }
        if (unit == null || unit == '') {
            showError("出错了", "请选择商品单位");
            return;
        }

        var bean = {
            name: name,
            size: size,
            unit: unit,
            desc: desc
        };
        result.push(bean);
    }
    if (result == null || result.length == 0) {
        showError("出错了", "请输入商品信息");
        return;
    }
    // 显示正在保存
    showInfo("请稍等", "正在保存数据,请稍等");
    console.log(result);
    // 获取所有供应商
    var url = 'http://localhost:8085/api/store/save';
    // 获取数据列表
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            name: result
        },
        // datatype: "json",
        // contentType: "application/json",
        success: function (data) {
            if (data.success) {
                // data = JSON.parse(data);
                // 清空数据
                resetData();
                showSuccess("成功", "保存数据成功!");
            } else {
                // 显示失败
                showError("出错了", "保存数据失败,请稍后重试");
            }
        },
        error: function (data) {
            // 显示失败
            showError("出错了", "保存数据失败,请稍后重试");
        }
    });

}

// 重置数据
function resetData() {
    lineIndex = 0;
    $(".tr_add").remove();
    $("#change_all_btn_clear").hide();
    $("#change_all_btn_save").hide();
}

// 根据出仓id获取商品列表
function getProById() {
    // 检查出仓id
    if (storefromid == -1) {
        showError("出错了", "请先选择出货的仓库");
        return;
    }
    var key = $("#et_keyword").val();
    // 获取所有供应商
    var url = 'http://localhost:8085/api/pro/list';
    // 获取数据列表
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            pageIndex: 0,
            storeid: storefromid,
            pageSize: 10,
            key: key
        },
        // datatype: "json",
        // contentType: "application/json",
        success: function (data) {
            if (data.success) {
                // data = JSON.parse(data);
                showProductList(data);
            } else {
                // 显示失败
                showError('出错了', '获取商品列表失败,请稍后重试');

            }
        },
        error: function (data) {
            // 显示失败
            showError('出错了', '获取商品列表失败,请稍后重试');
        }
    });
}

// 显示商品列表
function showProductList(data) {
    // 删除其他内容
    $(".pro_tr_add").remove();
    var length = data.data.length;
    for (var i = 0; i < length; i++) {
        var bean = data.data[i];
        var allLine = "<tr class=\"pro_tr_add\">\n" +
            "                        <td>" + bean.id + "</td>\n" +
            "                        <td>" + bean.name + "</td>\n" +
            "                        <td>" + bean.num + "</td>\n" +
            "                        <td>" + bean.price + "</td>\n" +
            "                        <td>" + bean.unit + "</td>\n" +
            "                        <td>" + bean.classify + "</td>\n" +
            "                        <td>" + bean.time + "</td>\n" +
            "                        <td>\n" +
            "                            <button style=\"margin: 0px;padding:2px 5px\" class=\"btn btn-success pro_table_btn_done\" attr_id='" + bean.id + "' attr_name='" + bean.name + "' attr_num='" + bean.num + "'>选择\n" +
            "                            </button>\n" +
            "                        </td>\n" +
            "                    </tr>";
        $("#pro_tbody").append(allLine);
    }
    // 点击选择的时候的事件
    $(".pro_table_btn_done").click(function () {
        // id
        var id = $(this).attr("attr_id");
        // name
        var name = $(this).attr("attr_name");
        // num
        var num = $(this).attr("attr_num");
        console.log(id);
        console.log(name);
        console.log(num);
        // 隐藏modal
        $('#add_edit_modal').modal('hide');
        // 显示数据
        $("#line_et_id_" + currentLineIndex).val(id);
        $("#line_et_name_" + currentLineIndex).val(name);
        $("#line_et_num_" + currentLineIndex).attr("max", num);
        $("#line_et_num_" + currentLineIndex).attr("placeholder", "最大值 " + num);
    });
    // 点击选择的时候
    $(".table_btn_choose").click(function () {
        currentLineIndex = $(this).attr("attr_index");
        // 获取商品列表
        $('#add_edit_modal').modal('show')
    });
    // 显示删除全部
    $("#all_btn_clear").show();
    $("#all_btn_save").show();
}