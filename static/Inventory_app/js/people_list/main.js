// 数据定义
var currentPageIndex = 0;

// 默认执行

// 获取客户列表
getPeopleList();

// 方法
// 根据客户姓名搜索获取客户列表
function getPeopleList() {
    // 获取客户姓名
    var key = $("#et_keyword").val();
    console.log("要搜索的客户名称:" + key);
    // 搜索
    var url = 'http://localhost:8085/api/people/list';
    // 一页的数量
    var pageSize = 10;
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
            "                        <td>" + bean.tel + "</td>\n" +
            "                        <td>" + bean.state + "</td>\n" +
            "                    </tr>";
        // 添加
        $("#tbody").append(line);

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
                getPeopleList();
            }

        }
    });

}

