# -*- coding: utf-8 -*-
import ast
import operator as op
from NumericParser import NumericStringParser

nsp = NumericStringParser()

def results(fields, original_query):
    expr = ""
    if len(fields):
        expr = fields["~expr"]

    res = nsp.eval(expr)
    return {
        "title": "The result is {0}".format(res)
    }


def run():
    return None
