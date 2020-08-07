# -*- coding:utf-8 -*-

import re
from lark import Transformer, v_args

@v_args(inline=True)

class TableGenerator(Transformer):
    def __init__(self):
        self.variables = {}

    def assignment(self, name, value):
