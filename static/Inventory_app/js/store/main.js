var currentPageIndex = 0;

// 获取仓库列表
getStoreList();

// 获取仓库列表
function getStoreList() {
    var url = 'http://localhost:8085/api/store/list';
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
                showData(data);
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
function showData(data) {
    // 清空内容
    $(".tr_add").remove();
    // 循环添加
    for (var i = 0; i < data.data.length; i++) {
        var bean = data.data[i];
        var state = '';
        if (bean.state == 0) {
            state = '未启用';
        } else {
            state = '已启用';
        }
        var line = "<tr class='tr_add'>\n" +
            "        <th scope=\"row\">" + bean.id + "</th>\n" +
            "        <td>" + bean.name + "</td>\n" +
            "        <td>" + state + "</td>\n" +
            "        <td>\n" +
            "            <button class=\"btn btn-primary btn_edit\" type=\"button\" attr_value='" + +bean.id + "'  attr_name='" + bean.name + "' attr_state='"+bean.state+"'>修改</button>\n" +
            "            <button class=\"btn btn-danger btn_del\" type=\"button\" attr_value='" + bean.id + "'>删除</button>\n" +
            "        </td>\n" +
            "\n" +
            "    </tr>";
        // 添加到内容
        $("#tbody").append(line);
        // 点击编辑时候的弹窗
        $(".btn_edit").click(function () {
            console.log("膝盖");
            // 获取选中的id
            var id = $(this).attr("attr_value");
            // 获取选中的内容
            var content = $(this).attr("attr_name");
            // 是否已启用
            var state = $(this).attr("attr_state");
            // 设置内容
            $("#et_id").val(id);
            $("#et_name").val(content);
            $("#select_state").val(state);
            // 显示弹窗
            $('#add_edit_modal').modal('show');
            // 设置标题
            $("#add_edit_modalLabel").val("修改仓库");
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
                getStoreList();
            }
            console.log(num);
            console.log(currentPageIndex);
            // 跳转页面
            // if ((currentPageIndex + 1) != num) {
            //     currentPageIndex = num;
            //     getStoreList();
            // }
        }
    });
}

// 保存仓库内容
function saveStore() {
    // 显示正在保存
    iziToast.info({
        title: '请稍等',
        position: 'topRight',
        message: '正在保存数据,请稍等!'
    });
    // 获取id
    var id = $("#et_id").val();
    // 获取内容
    var content = $("#et_name").val();
    // 获取是否启用
    var state = $("#select_state").val();
    // 检查内容
    if ( content == null||content=="") {
        // 隐藏弹窗
        var toast = document.querySelector('.iziToast');
        iziToast.hide({}, toast);
        iziToast.error({
            title: '出错了',
            position: 'topRight',
            message: '仓库名称不能为空!'
        });
        return;
    }
    // 保存内容
    if (id == null || id == "") {
        id = -1;
    }
    console.log(id);
    console.log(content);
    // 隐藏modal
    $('#add_edit_modal').modal('hide');
    // 保存内容
    var url = 'http://localhost:8085/api/store/save';
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            id: id,
            name: content,
            state: state
        },
        // datatype: "json",
        // contentType: "application/json",
        success: function (data) {
            // 隐藏弹窗
            var toast = document.querySelector('.iziToast');
            iziToast.hide({}, toast);
            if (data.success) {
                // data = JSON.parse(data);
                // 保存成功

                iziToast.success({
                    title: '成功',
                    position: 'topRight',
                    message: '保存仓库成功!'
                });
                // 刷新数据
                setTimeout(function () {
                    getStoreList();
                }, 1000);
            } else {
                // 显示失败
                iziToast.error({
                    title: '出错了',
                    position: 'topRight',
                    message: '保存仓库信息错误,请稍后重试'
                });
                // 重新获取数据
                getData();
            }
        },
        error: function (data) {
            // 隐藏弹窗
            var toast = document.querySelector('.iziToast');
            iziToast.hide({}, toast);
            // 显示失败
            iziToast.error({
                title: '出错了',
                position: 'topRight',
                message: '保存仓库信息错误,请刷新重试'
            });
        }
    });
}

// 删除仓库内容
function delStore() {
    // 显示正在保存
    iziToast.info({
        title: '请稍等',
        position: 'topRight',
        message: '正在删除仓库,请稍等!'
    });
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
                // data = JSON.parse(data);
                // 保存成功

                iziToast.success({
                    title: '成功',
                    position: 'topRight',
                    message: '删除仓库成功!'
                });
                // 刷新数据
                setTimeout(function () {
                    getStoreList();
                }, 1000);
            } else {
                // 显示失败
                iziToast.error({
                    title: '出错了',
                    position: 'topRight',
                    message: '删除仓库失败,请稍后重试'
                });
                // 重新获取数据
                getData();
            }
        },
        error: function (data) {
            var toast = document.querySelector('.iziToast');
            iziToast.hide({}, toast);
            // 显示失败
            iziToast.error({
                title: '出错了',
                position: 'topRight',
                message: '删除仓库失败,请刷新重试'
            });
        }
    });
}