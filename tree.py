import random
from fractions import Fraction
from calculator import calculator
from calculator import NegativeError
from convert import Convert

class Node:
    # 节点类
    def __init__(self,value=None,left=None,right=None):
        self.value = value  #节点的值，为操作符或者操作数
        self.left = left  # 左子树
        self.right = right  # 右子树
        self.oPriority = {'+': 1, '-': 1, '*': 2, '/': 2}  # 设置运算符的优先级

    def is_operator(self,val):
        if val in ['+','-','*','/']:
            return True
        else:
            return False

    def get_mid(self):   # 获取中序表达式，添加小括号区分优先级
        midExpression = []
        #是操作数直接返回
        if not self.is_operator(self.value):
            return [self.value]
        #是操作符继续判断左右子树
        elif self.is_operator(self.value):
            if self.is_operator(self.left.value) and \
                self.oPriority[str(self.value)] > self.oPriority[str(self.left.value)]:
                #处理左子树
                midExpression.append('(')   # 当父母节点的操作符的优先级大于或等于孩子节点的时候，在子树添加小括号
                midExpression += self.left.get_mid()
                midExpression.append(')')
            else:
                midExpression += self.left.get_mid()

            midExpression.append(self.value)                                 #处理中间结点

            if self.is_operator(self.right.value) and \
                    self.oPriority[str(self.value)] >= self.oPriority[str(self.right.value)]:
                # 处理右子树
                midExpression.append('(')     # 当父母节点的操作符的优先级大于或等于孩子节点的时候，在子树添加小括号
                midExpression += self.right.get_mid()
                midExpression.append(')')
            else:
                midExpression += self.right.get_mid()
            return midExpression

    def calc_answer(self):   # 递归计算每个子树结果
        if self.is_operator(self.value):
            lf = self.left.calc_answer()
            rt = self.right.calc_answer()
            return calculator.eval(self.value, lf, rt)
        else:
            return self.value

class Tree:
    def __init__(self):
        self.root = Node()
        self.type = [1, 2]                                           # 操作数类型，1表示整数，2表示分数
        self.midExpression = []                                     # 中缀表达式
        self.afterExpression = []                                      # 后缀表达式
        self.expression = []                                             # 格式化后的表达式
        self.answer = []                                              # 格式化后的答案
        self.opList = ["+", "-", "*", "/"]                               # 根节点的符号类型

    def create(self, numRange, amount):
        num = 0
        while num < amount:
            operatorNum = random.choice([1, 2, 3])  # 随机选择运算符个数
            emptyNode = [self.root]
            for i in range(operatorNum):  #循环获取运算符当节点然后分配左右节点
                node = random.choice(emptyNode)
                emptyNode.remove(node)
                node.value = random.choice(self.opList)
                node.left = Node()
                node.right = Node()
                emptyNode.append(node.left)
                emptyNode.append(node.right)

            for node in emptyNode:
                num_type = random.choice(self.type)   # 随机选择生成整数或分数
                if num_type == 1:
                    node.value = random.randint(1, amount)
                else:
                    node.value = Fraction(random.randint(1, numRange), random.randint(1, numRange))
                    #print(node.value)
            try:
                result = self.root.calc_answer()                # 计算答案
                self.midExpression = self.root.get_mid()                        # 中缀表达式
                self.afterExpression = Convert.change_to_after(self.midExpression)  # 将中缀表达式转化成后缀表达式

                output = Convert.convert_to_standard(self.midExpression)    # 格式化输出###
                if isinstance(result, Fraction):
                    answer = Convert.convert_fraction(result)                # 格式化输出答案
                else:
                    answer = result
                if answer in self.answer:
                    continue
                else:
                     self.expression.append(output)
                     self.answer.append(answer)
            except NegativeError:                      # 异常处理，结果不可为负数
               continue
            except ZeroDivisionError:              # 异常处理，分母不可为0
                continue
            else:
                num += 1
        return self.expression, self.answer

