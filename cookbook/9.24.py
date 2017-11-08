# encoding=utf-8
# 源码分析
import ast

ex = ast.parse('2+4*10-5', mode='eval')
print(ast.dump(ex))
