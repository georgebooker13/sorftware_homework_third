import operator
import fractions


class calculator:
    def eval(_operator, value1, value2):        #定义两个操作数（只有一个运算符号）
        answer = 0
        if _operator == "+":
            answer = operator.add(value1, value2)
        elif _operator == "-":
            if operator.lt(value1, value2):    #value1是否小于value2,通过operator的lt方法，若value1<value2则返回1,否则返回0
                raise NegativeError()         #当被减数大于减数的时抛出异常
            else:
                answer = operator.sub(value1, value2) #保证了value1大于value2则正常计算减法
        elif _operator == "*":
            answer = operator.mul(value1, value2)
        elif _operator == "/":
            if value2 == 0:
                raise ZeroDivisionError                  #当除数大于被除数时抛出异常
            answer = operator.truediv(value1, value2)
            if isinstance(answer, float):    # 若答案为浮点数，则转换为分数
                answer = operator.truediv(fractions.Fraction(value1), fractions.Fraction(value2))
        return answer


    def output_correct_rate(studentInputs, answerList):         # 试题正确率的计算
        correct = []
        wrong = []
        length = len(studentInputs)
        for index, inp, answer in zip(range(1, length + 1), studentInputs, answerList):
            if inp == answer:
                correct.append(index)
            else:
                wrong.append(index)
        return correct, wrong

#负数处理
class NegativeError(Exception):
    def __init__(self):
        super(NegativeError, self).__init__()