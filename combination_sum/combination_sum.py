#!/usr/bin/env python3
import itertools
import math

class BinaryOperator(object):
    """ 2項演算子 """
    def __init__(self, operator, name, priority):
        self.op = operator
        self.name = name
        self.priority = priority
    def __lt__(self, other): return self.priority < other.priority
    def __call__(self, *args): return self.op(args[0], args[1])
    def __str__(self): return self.name

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else math.inf

# input
arg_list = [5, 5, 5, 1]
op_list = [add, sub, mul, div]
expected = 24
op_str = {add: '+', sub: '-', mul: '*', div: '/'}

op_combi = tuple(itertools.product(op_list, repeat=len(arg_list)-1))
priority_combi = tuple(itertools.permutations(range(0, len(arg_list)-1), len(arg_list) - 1))
ops = tuple(
    tuple(
        BinaryOperator (op, op_str[op], priority) for op, priority in zip(op_tuple, priority_tuple)
    ) for op_tuple in op_combi for priority_tuple in priority_combi
)
args = tuple(itertools.permutations(arg_list))

def make_rpn(arg, op):
    """ 逆ポーランド記法スタックを生成 """
    stack = []
    stack_op = []
    for i in range(0, len(op)):
        stack.append(arg[i])
        while len(stack_op) > 0 and stack_op[-1] < op[i]:
            stack.append(stack_op.pop())
        stack_op.append(op[i])
    stack.append(arg[-1])
    while len(stack_op):
        stack.append(stack_op.pop())
    return tuple(stack)

def eval_rpn(rpn_formula, apply):
    """ 逆ポーランド記法 の数式を計算"""
    stack = []
    for element in rpn_formula:
        if isinstance(element, BinaryOperator):
            rhs = stack.pop()
            lhs = stack.pop()
            result = apply(element, lhs, rhs)
            stack.append(result)
        else:
            stack.append(element)
    return stack.pop()

def round_if_int(a):
    return a if math.isinf(a) or int(a) != a else int(a)

# setで重複する式を除外
rpn_formulae = set(make_rpn(arg, op) for arg in args for op in ops)

for formula in rpn_formulae:
    ans = eval_rpn(formula, lambda op, lhs, rhs: op(lhs, rhs))
    expression = eval_rpn(formula, lambda op, lhs, rhs: f'({lhs} {op} {rhs})')
    result = f'{expression[1:][:-1]} = {round_if_int(ans)}'
    if (expected == ans):
        print(f"{result}")
