// 开始页数
var currentIndex = 0;

// 获取数据
getHostoryList();

// 获取历史数据
function getHostoryList() {
    var url = 'http://localhost:8085/api/add/list';
    // 获取每页数量
    var pageSize = 10;
    // 获取关键字
    var key = $("#et_keyword").val();
    // 获取开始日期
    var startDate = $("#plane_history_date_start").val();
    // 获取结束日期
    var endDate = $("#plane_history_date_end").val();
    console.log(key);
    console.log(startDate);
    console.log(endDate);
    // 获取数据列表
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            pageIndex: currentIndex,
            pageSize: pageSize,
            startDate: startDate,
            endDate: endDate,
            key: key
        },
        // datatype: "json",
        // contentType: "application/json",
        success: function (data) {
            if (data.success) {
                // data = JSON.parse(data);
                showHistoryData(data);
            } else {
                // 显示失败
                showError('出错了', '获取回访计划列表失败,请稍后重试');
            }
        },
        error: function (data) {
            // 显示失败
            showError('出错了', '获取回访计划失败,请刷新重试');
        }
    });
}

// 显示历史数据
function showHistoryData(data) {
    // 清空内容
    $(".tr_add").remove();
    // 循环添加
    for (var i = 0; i < data.data.length; i++) {
        var bean = data.data[i];
        var line = "<tr class=\"tr_add\">\n" +
            "        <td>"+bean.name+"</td>\n" +
            "        <td>"+bean.num+"</td>\n" +
            "        <td>"+bean.price+"</td>\n" +
            "        <td>"+bean.unit+"</td>\n" +
            "    </tr>";
        // 添加到内容
        $("#tbody").append(line);
    }
    // 滚动到顶部
    $('html,body').animate({scrollTop: '0px'}, 600);
    // 显示分页
    $('#page').jqPaginator({
        totalPages: data.allpage,
        visiblePages: 10,
        currentPage: currentIndex + 1,
        prev: '<li class="page-item"><a class="page-link" href="#">上一页</a></li>',
        next: '<li class="page-item"><a class="page-link" href="#">下一页</a></li>',
        page: '<li class="page-item"><a class="page-link" href="#">{{page}}</a></li>',
        onPageChange: function (num, type) {
            if (type == 'change') {
                currentIndex = num - 1;
                getHostoryList();
            }

        }
    });
}
