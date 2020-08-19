# -*- coding: utf-8 -*-
import sys

from Core.MainProgram import MainProgram

arguments = sys.argv[1:]

(MainProgram()).checkArguments(arguments)