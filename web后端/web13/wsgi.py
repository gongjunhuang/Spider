import sys
from os.path import abspath
from os.path import dirname

# 设置当前目录为工作目录
sys.path.insert(0, abspath(dirname(__file__)))

import app

application = app.app

# 把代码部署到apache nginx的套路