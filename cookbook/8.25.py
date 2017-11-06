# encoding=utf-8
import weakref


class Spam:
    spam_cache = weakref.WeakValueDictionary()

    def __init__(self, name):
        self.name = name


def get_spam(name):
    if name not in Spam.spam_cache:
        s = Spam(name)
        Spam.spam_cache[name] = s
    else:
        s = Spam.spam_cache[name]
    return s


a = get_spam('foo')
b = get_spam('bar')
c = get_spam('foo')
print(a is b)
