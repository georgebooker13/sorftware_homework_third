import fractions
#输出的格式
class Convert:

    def convert_fraction(answer):         # 将分数统一表示为真分数
        if (answer > 1 or answer < -1) and answer.denominator != 1:
            answerNumerator = answer.numerator % answer.denominator      # 分子以分母为模取余
            answerDenominator = answer.denominator                       # 分母
            answerRight = fractions.Fraction(answerNumerator, answerDenominator)  #真分数右边的分数部分
            answerLeft = answer.numerator // answer.denominator          #真分数左边的整数部分
            result = str(answerLeft) + '\'' + str(answerRight)
        else:
            result = str(answer)
        return result

    def convert_to_standard(expression):      # 规范化输出时的格式
        output = ''
        for expr in expression:
            if isinstance(expr, fractions.Fraction):
                output += Convert.convert_fraction(expr)
            elif isinstance(expr, int):
                output += str(expr)
            elif expr == '+':
                output += ' + '
            elif expr == '-':
                output += ' - '
            elif expr == '*':
                output += ' x '
            elif expr == '/':
                output += ' ÷ '
            else:
                output += expr
        output += ' ＝ '
        return output

    def change_to_after(expression):    #转化成后缀表达式
        outputExpression = []  # 存放已经生成的表达式
        operatorStack = []  # 把操作符入栈存放
        operatorPriority = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}
        for expr in expression:
            if isinstance(expr, int) or isinstance(expr, fractions.Fraction):
                outputExpression.append(expr)
            elif expr == '(':                         # (优先级最低，直接入栈
                operatorStack.append(expr)
            elif expr == ')':                      # )优先级最高
                while operatorStack[-1] != '(':
                    outputExpression.append(operatorStack.pop())
                operatorStack.pop()
            else:
                while len(operatorStack) > 0 and \
                operatorPriority[operatorStack[-1]] >= operatorPriority[expr]:   #优先级大于栈顶元素压栈,否则将operatorPriority中优先级大于或等于该操作符的元素输出,最后压栈
                    outputExpression.append(operatorStack.pop())
                operatorStack.append(expr)

        while operatorStack:
            outputExpression.append(operatorStack.pop())

        return outputExpression

