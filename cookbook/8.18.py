# -*- coding: utf-8 -*-
# 利用Mixins 扩展类功能


class LoggedMappingMixin:
    __slots__ = ()  # 此类不接受实例动态绑定属性

    def __getitem__(self, item):
        print('Getting', str(item))
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print('Setting {}={}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting', key)
        return super().__delitem__(key)


class LoggedDict(LoggedMappingMixin, dict):
    pass


# 类装饰器
def logged_mapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, item):
        print('get', item)
        return cls_getitem(self, item)

    def __setitem__(self, item, value):
        print('set', item)
        return cls_setitem(self, item, value)

    def __delitem__(self, item):
        print('del', item)
        return cls_delitem(self, item)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__

    return cls


@logged_mapping
class MyDict(dict):
    pass


d = MyDict()
d['x'] = 10
print(d['x'])
del d['x']
