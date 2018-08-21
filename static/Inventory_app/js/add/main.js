var storeid = -1;

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
                iziToast.error({
                    title: '出错了',
                    position: 'topRight',
                    message: '获取仓库列表失败,请稍后重试'
                });
                // 重新获取数据
                getData();
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
    $("#store_select").append(line);
    // 显示列表
    for (var i = 0; i < data.data.length; i++) {
        var bean = data.data[i];
        var line = "<option class=\"option_line\" value=\"" + bean.id + "\" >" + bean.name + " </option>";
        $("#store_select").append(line);
    }
}

// 获取仓库的id
function getStoreId() {
    storeid = $("#store_select").val();
    console.log("仓库id:" + storeid);
}

// 获取供应商列表
function getSupplyList() {
    // 获取所有供应商
    var url = 'http://localhost:8085/api/supply/list';
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
                addLine(data);
            } else {
                // 显示失败
                iziToast.error({
                    title: '出错了',
                    position: 'topRight',
                    message: '获取供应商列表失败,请稍后重试'
                });

            }
        },
        error: function (data) {
            // 显示失败
            iziToast.error({
                title: '出错了',
                position: 'topRight',
                message: '获取供应商列表失败,请刷新重试'
            });
        }
    });
}

// 添加一行商品
function addLine(data) {
    var allLine = "<tr class='tr_add' id='line_index_" + lineIndex + "'>\n" +
        "        <td>\n" +
        "            <div class=\"form-inline\"><input type=\"tel\" placeholder=\"选择商品\" class=\"form-control line_et_name\">\n" +
        "                <button style=\"margin: 5px\" class=\"btn btn-danger table_btn_del\" attr_index='" + lineIndex + "'>删除</button>\n" +
        "            </div>\n" +
        "        </td>\n" +
        "        <td><input type=\"number\" placeholder=\"选择数量\" class=\"form-control line_et_size\"></td>\n" +
        "        <td><input type=\"number\" placeholder=\"输入单价\" class=\"form-control line_et_price\"></td>\n" +
        "        <td>\n" +
        "            <select class=\"form-control line_et_unit\">\n" +
        "                <option>选择单位</option>\n" +
        "                <option>件</option>\n" +
        "                <option>件</option>\n" +
        "                <option>件</option>\n" +
        "                <option>件</option>\n" +
        "                <option>件</option>\n" +
        "            </select>\n" +
        "        </td>\n" +
        "        <td><input type=\"text\" placeholder=\"输入类别\" class=\"form-control line_et_classify\"></td>\n" +
        "        <td>\n" +
        "            <select class=\"form-control select_line_supply\" >\n" +
        "                <option value='-1'>选择供应商</option>\n" +
        "            </select>\n" +
        "        </td>\n" +
        "    </tr>";
    $("#tbody").append(allLine);
    lineIndex++;
    // 删除所有的供应商
    $(".line_select_supply_option").remove();
    // 添加供应商
    for (var i = 0; i < data.data.length; i++) {
        console.log("添加一个供应商");
        var bean = data.data[i];
        var line = "<option class='line_select_supply_option' value='" + bean.id + "'>" + bean.name + "</option>";
        $(".select_line_supply").append(line);
    }
    // 点击删除的时候的响应时间
    $(".table_btn_del").click(function () {
        var trueIndex = $(this).attr("attr_index");
        $("#line_index_" + trueIndex).remove();
        if ($(".table_btn_del").length==0){
            resetData();
        }
    });
    // 显示删除全部
    $("#all_btn_clear").show();
    $("#all_btn_save").show();


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
        var name = $(".line_et_name").eq(i).val();
        var size = $(".line_et_size").eq(i).val();
        var price = $(".line_et_price").eq(i).val();
        var unit = $(".line_et_unit").eq(i).val();
        var classify = $(".line_et_classify").eq(i).val();
        var supplyid = $(".select_line_supply").eq(i).val();

        console.log(name);
        console.log(size);
        console.log(price);
        console.log(unit);
        console.log(classify);
        console.log(supplyid);
        if (name == null || name == '') {
            showError("出错了", "请输入商品名称");
            return;
        }
        if (size == null || size == '') {
            showError("出错了", "请输入商品数量");
            return;
        }
        if (price == null || price == '') {
            showError("出错了", "请输入商品价格");
            return;
        }
        if (unit == null || unit == '') {
            showError("出错了", "请选择商品单位");
            return;
        }
        if (supplyid == null || supplyid == -1) {
            showError("出错了", "请选择供应商");
            return;
        }

        var bean = {
            name: name,
            size: size,
            price: price,
            unit: unit,
            classify: classify,
            supplyid: supplyid
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
            name:result
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
    $(".tr_add").remove();
    $("#all_btn_clear").hide();
    $("#all_btn_save").hide();
}