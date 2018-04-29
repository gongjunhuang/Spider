/*
1, 给 add button 绑定事件
2, 在事件处理函数中, 获取 input 的值
3, 用获取的值 组装一个 todo-cell HTML 字符串
4, 插入 todo-list 中
*/
var log = function() {
    console.log().apply(console, arguments)
}

var e = function(sel) {
    return document.querySelector(sel)
}

var ajax = function(method, path, data, responseCallback) {
    var r =  new XMLHttpRequest()
    r.open(method, path, true)
    //设置发送的数据格式胃application/json
    r.setRequestHeader('Content-Type', 'application/json')
    //注册响应函数
    r.onreadystatechange = function() {
        if(r.readyState == 4) {
            responseCallback(r.response)
        }
    }
    //把数据转换成json格式字符串
    data = JSON.stringify(data)
    r.send(data)
}

var apiTodoAll = function(callback) {
    var path = '/api/todo/all'
    ajax('GET', path, '', callback)
}

var apiTodoAdd = function(form, callback) {
    var path = '/api/todo/add'
    ajax('POST', path, form, callback)
}
