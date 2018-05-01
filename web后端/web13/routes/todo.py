from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    Blueprint,
    url_for,
)

# 一次性引入多个 flask 里面的名字
# 注意最后一个后面也应该加上逗号
# 这样的好处是方便和一致性

from models.todo import Todo


# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字, 以后会有用(add函数里面就用到了)
# 第二个参数是套路
main = Blueprint('todo', __name__)

@main.route('/')
def index():
    todo_list = Todo.all()
    # flask 已经配置好了 jinja2 模板引擎
    # 并且可以直接使用 render_template 来生成响应数据(http_response)
    return render_template('todo_index.html', todos=todo_list)

@main.route('/add', methods=['POST'])
def add():
    form = request.form
    t = Todo.new(form)
    t.save()
    return redirect(url_for('todo.index'))

@main.route('/delete/<int:todo_id>/')
def delete(todo_id):
    """
    <int:todo_id> 的方式可以匹配一个 int 类型
    int 指定了它的类型，省略的话参数中的 todo_id 就是 str 类型

    这个概念叫做 动态路由
    意思是这个路由函数可以匹配一系列不同的路由

    动态路由是现在流行的路由设计方案
    """
    t = Todo.delete(todo_id)
    return redirect(url_for('.index'))


