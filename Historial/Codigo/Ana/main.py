# -*- coding: utf-8 -*-
import sys
from Reader import Reader
from lark import Lark
from Grammar import *
import sys

param = sys.argv[1:]

reader = (Reader()).read2(param)
parser = Lark(grammar, parser="lalr")
language = parser.parse

sample = reader.text
try:
    language(sample)
except Exception as e:
    print ("Error: %s" % e)