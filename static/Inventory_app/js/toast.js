// 显示提示信息
function showInfo(title, msg) {
    // 隐藏其他内容
    try {
        // 隐藏弹窗
        var toast = document.querySelector('.iziToast');
        iziToast.hide({}, toast);
    } catch (e) {

    }
    // 显示内容
    iziToast.info({
        title: title,
        position: 'topRight',
        message: msg
    });
}

// 显示错误信息
function showError(title, msg) {
    // 隐藏其他内容
    try {
        // 隐藏弹窗
        var toast = document.querySelector('.iziToast');
        iziToast.hide({}, toast);
    } catch (e) {

    }
    // 显示内容
    iziToast.error({
        title: title,
        position: 'topRight',
        message: msg
    });
}

// 显示成功信息
function showSuccess(title, msg) {
    // 隐藏其他内容
    try {
        // 隐藏弹窗
        var toast = document.querySelector('.iziToast');
        iziToast.hide({}, toast);
    } catch (e) {

    }
    // 显示内容
    iziToast.success({
        title: title,
        position: 'topRight',
        message: msg
    });
}