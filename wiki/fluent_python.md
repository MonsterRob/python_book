1 技术盲点在哪里？

2 掌握程度怎么样？

3 熟练程度怎么样？

流畅的Python 读书笔记 
    
    关键词：始基单元 即编程语言词汇即关键字
    特殊方法的存在是为了让解释器调用
 

特殊方法：

    与运算符无关的：
    
        字符串表示形式：__repr__ __str__ __formats__ __bytes__
        数值转换：__abs__ __bool__ __complex__ __int__ __float__ __hash__ __index__
        集合模拟：__len__ __getitem__ __setitem__ __delitem__ __contains__
        迭代枚举：__iter__ __reversed__ __next__
        可调用模拟：__call__
        上下文管理:__enter__ __exit__
        实例创建和销毁:__new__ __init__ __del__
        属性管理:__getattr__ getattribute__ __setattr__ __delattr__ __dir__
        属性描述符:__get__ __set__ __delete__
        根类相关的服务:__prepare__ __instancechcek__ __subclasscheck__
    
    与运算符有关的：
        
        很多
        
        