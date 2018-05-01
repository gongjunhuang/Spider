import time
from models import Model

# 针对我们的数据 TODO
# 我们要做 4 件事情
"""
C create 创建数据
R read 读取数据
U update 更新数据
D delete 删除数据

Todo.new() 来创建一个 todo
"""
class Todo(Model):
    @classmethod
    def new(cls, form):
        """
        创建并保存一个 todo 并且返回它
        Todo.new({'title': '吃饭'})
        :param form: 一个字典 包含了 todo 的数据
        :return: 创建的 todo 实例
        """
        t = cls(form)
        t.save()
        return t

    @classmethod
    def update(cls, id, form):
        t = cls.find(id)
        valid_name = [
            'title',
            'completed'
        ]
        for key in form:
            if key in valid_name:
                setattr(t, key, form(key))

        t.save()
        return t

    @classmethod
    def complete(cls, id, completed=True):
        t = cls.find(id)
        t.completed = completed
        t.save()
        return t

    def __init__(self, form):
        self.id = None
        self.title = form.get('title', '')
        self.completed = False
        self.ct = int(time.time())
        self.ut = self.ct