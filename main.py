import os
import argparse
import tree
import file
from calculator import calculator


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', dest='amount', type=int, default=10, help='指定生成题目的数量')
    parser.add_argument('-r', dest='range', type=int, default=10, help='指定生成题目中的数值最大值')
    parser.add_argument('-e', dest='exercise', type=str, default='Exercise.txt', help='指定练习题的文件名')
    parser.add_argument('-a', dest='answer', type=str, default='Answers.txt', help='指定练习题答案的文件名')
    parser.add_argument('-g', dest='grade', type=str, default='Grade.txt', help='指定得分情况的文件名')
    args = parser.parse_args()
    exercisePath = os.path.join('./output', args.exercise)         #习题的输出路径
    answerPath = os.path.join('./output', args.answer)            #答案的输出路径
    gradePath = os.path.join('./output', args.grade)              #成绩的输出路径
    tree = tree.Tree()
    inputAnswers = []
    expressions, answers = tree.create(args.range, args.amount)         #指定参数生成题目和答案
    file.File.output_exercise(expressions,exercisePath)     # 题目以文件的形式保存
    file.File.out_put_answer(answers,answerPath)   #答案以文件的形式保存
    for i in range(args.amount):
        print(expressions[i],end='')
        inp = input()
        inputAnswers.append(inp)
    correct, wrong = calculator.output_correct_rate(inputAnswers, answers)    # 统计成绩
    file.File.output_grade(gradePath, correct, wrong)                     #将答题情况以文件的形式保存