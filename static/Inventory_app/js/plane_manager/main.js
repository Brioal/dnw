// 数据定义
var currentPageIndex = 0;

// 默认执行

// 获取回访计划列表
getPlanList();

// 方法
// 客户搜索
// 根据客户姓名搜索客户列表
function peopleSearch() {
    // 获取客户姓名
    var key = $("#add_modal_et_keyword").val();
    console.log("要搜索的客户名称:" + key);
    // 搜索
    var url = 'http://localhost:8085/api/people/list';
    // 获取数据列表
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            key: key
        },
        // datatype: "json",
        // contentType: "application/json",
        success: function (data) {
            if (data.success) {
                // data = JSON.parse(data);
                // 显示
                showPeopleList(data);
            } else {
                // 显示失败
                showError('出错了', '找不到对应的用户');
            }
        },
        error: function (data) {
            // 显示失败
            showError('出错了', '找不到对应的用户');
        }
    });
}

// 显示客户列表
function showPeopleList(data) {
    // 删除所有的客户列表
    $(".add_modal_tr").remove();
    // 循环添加内容
    var length = data.data.length;
    for (var i = 0; i < length; i++) {
        var bean = data.data[i];
        var line = " <tr class=\"add_modal_tr\">\n" +
            "                        <td>" + bean.name + "</td>\n" +
            "                        <td>" + bean.state + "</td>\n" +
            "                        <td >\n" +
            "                            <button attr_id='" + bean.id + "' class=\"btn btn-success add_modal_btn_choose\" type=\"button\" style=\"margin: 0px;padding: 2px 5px\">选择</button>\n" +
            "                        </td>\n" +
            "                    </tr>";
        // 添加
        $("#add_modal_tbody").append(line);
        // 点击选择的时候进行确认
        $(".add_modal_btn_choose").click(function () {
            // 判断是否选择了时间
            var dataVal = $("#add_modal_et_date").val();
            if (dataVal == null || dataVal == '') {
                showError("出错了", "请选择回访日期");
                return;
            }
            // 获取客户的id
            var id = $(this).attr("attr_id");
            console.log(id);
            console.log(dataVal);
            // 隐藏modal
            $("#add_modal").modal('hide');
            // 进行保存
            savePlan(id, dataVal);
        });

    }


}

// 保存回访计划
function savePlan(id, dataVal) {
    // 显示正在保存
    showInfo("请稍等", "正在保存回访计划,请稍等");
    // 保存数据
    // 搜索
    var url = 'http://localhost:8085/api/store/save';
    // 获取数据列表
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            id: id,
            dataVal: dataVal
        },
        // datatype: "json",
        // contentType: "application/json",
        success: function (data) {
            if (data.success) {
                // data = JSON.parse(data);
                // 保存成功,刷新
                showSuccess("成功", "保存计划成功");
                getPlanList();
            } else {
                // 显示失败
                showError('出错了', '保存回访计划失败');
            }
        },
        error: function (data) {
            // 显示失败
            showError('出错了', '保存回访计划失败');
        }
    });

}

// 获取回访计划列表
getPlanList();

// 获取回访计划列表
function getPlanList() {
    var url = 'http://localhost:8085/api/plan/list';
    // 获取每页数量
    var pageSize = 10;
    // 获取关键字
    var key = $("#et_keyword").val();
    // 获取数据列表
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            pageIndex: currentPageIndex,
            pageSize: pageSize,
            key: key
        },
        // datatype: "json",
        // contentType: "application/json",
        success: function (data) {
            if (data.success) {
                // data = JSON.parse(data);
                // 显示计划列表
                showPlanList(data);
            } else {
                // 显示失败
                showError('出错了', '获取回访计划列表失败');
            }
        },
        error: function (data) {
            // 显示失败
            showError('出错了', '获取回访计划列表失败');
        }
    });

}

// 显示仓库列表
function showPlanList(data) {
    // 清空内容
    $(".tr_add").remove();
    // 循环添加
    for (var i = 0; i < data.data.length; i++) {
        var bean = data.data[i];
        var line = "<tr class='tr_add'>\n" +
            "        <td>" + bean.name + "</td>\n" +
            "        <td>" + bean.state + "</td>\n" +
            "        <td>" + bean.date + "</td>\n" +
            "        <td>" + bean.arrive + "</td>\n" +
            "        <td>\n" +
            "            <button class=\"btn btn-primary btn_edit\" type=\"button\" attr_value='" + +bean.id + "'  attr_name='" + bean.name + "' attr_time='" + bean.time + "'>修改</button>\n" +
            "            <button class=\"btn btn-danger btn_del\" type=\"button\" attr_value='" + bean.id + "'>删除</button>\n" +
            "        </td>\n" +
            "\n" +
            "    </tr>";
        // 添加到内容
        $("#tbody").append(line);
        // 点击编辑时候的弹窗
        $(".btn_edit").click(function () {
            console.log("点击了删除");
            // 获取选中的id
            var id = $(this).attr("attr_value");
            // 获取选中的内容
            var content = $(this).attr("attr_name");
            // 是否已启用
            var time = $(this).attr("attr_time");
            console.log(id);
            console.log(content);
            console.log(time);
            // // 设置内容
            $("#edit_modal_et_id").val(id);
            $("#edit_modal_et_name").val(content);
            $("#edit_modal_et_date").val(time);
            // 显示弹窗
            $('#edit_modal').modal('show');
        });
        // 点击删除时候的弹窗
        $(".btn_del").click(function () {
            console.log("删除");
            // 获取选中的id
            var id = $(this).attr("attr_value");
            // 设置内容
            $("#modal_et_id").val(id);
            // 显示弹窗
            $('#del_edit_modal').modal('show');
        });
    }
    // 滚动到顶部
    $('html,body').animate({scrollTop: '0px'}, 600);
    // 显示分页
    $('#page').jqPaginator({
        totalPages: data.allpage,
        visiblePages: 10,
        currentPage: currentPageIndex + 1,
        prev: '<li class="page-item"><a class="page-link" href="#">上一页</a></li>',
        next: '<li class="page-item"><a class="page-link" href="#">下一页</a></li>',
        page: '<li class="page-item"><a class="page-link" href="#">{{page}}</a></li>',
        onPageChange: function (num, type) {
            if (type == 'change') {
                currentPageIndex = num - 1;
                getPlanList();
            }
        }
    });
}

// 删除仓库内容
function delPlan() {
    // 显示正在保存
    showInfo('请稍等', '正在删除回访计划,请稍等!');
    // 获取id
    var id = $("#modal_et_id").val();
    // 隐藏modal
    $('#del_edit_modal').modal('hide');
    // 保存内容
    var url = 'http://localhost:8085/api/store/save';
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            id: id
        },
        // datatype: "json",
        // contentType: "application/json",
        success: function (data) {
            // 隐藏弹窗
            var toast = document.querySelector('.iziToast');
            iziToast.hide({}, toast);
            if (data.success) {
                // 删除成功
                showSuccess('成功', '删除回访计划成功');
                // 刷新数据
                setTimeout(function () {
                    getStoreList();
                }, 1000);
            } else {
                // 显示失败
                showError('出错了', '删除回访计划失败,请稍后重试');
            }
        },
        error: function (data) {
            // 显示失败
            showError('出错了', '删除回访计划失败,请稍后重试');
        }
    });
}