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
数据结构

    容器序列：list tuple deque Queue
    扁平序列 str bytes bytearray memeryviwe
    可变序列 list deque ...
    不可变序列 tuple str bytes
    列表推导式 生成器表达式
    就地 原地 改变
    切片操作
    Python tutor 网站分析工具
    不要将可变对象放在元组里/ 增量操作不是原子的
    += *= 区别对待可变和不可变序列
    Timsort Tim Peters
    
字典和集合
    
    {key:value, key1:value1,...}
    散列表的原理？
    对象的生命周期 散列值不变
    字典的多种构造方式
    字典推到式
    defaultdict 与可调用对象
    __slots__改变实例属性的存储方式
    
文本和字节序列

    人类使用文本 计算机使用字节序列
   
函数--对象

    一等对象：在运行时创建 能赋值给变量 能作为参数传递给函数 能作为函数的额返回结果
    对象的属性：数据属性 可调用属性
    高阶函数
    匿名函数
    可调用对象 调用运算符 
    生成器函数---> 生成器
    函数内省
    函数签名
    可调用对象协议
    函数注解
    函数式编程：operator functools
    partial 函数
    
使用一等函数实现设计模式

     符合模式并不表示做的对
    
    
        