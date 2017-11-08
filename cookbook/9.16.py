# -*- coding: utf-8 -*-
# 函数强制参数签名
from inspect import Signature, Parameter

params = [Parameter('x', Parameter.POSITIONAL_ONLY, default=42),
          Parameter('y', Parameter.POSITIONAL_ONLY, default=1),
          Parameter('z', Parameter.KEYWORD_ONLY, default=None)]
sig = Signature(params)


def my(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)


my('xxx')
