class File:
#分别规范化输出练习、答案、答题情况到各指定文件
    def output_exercise(expressions, exercisePath):
        index = 0
        with open(exercisePath, 'w+', encoding='utf-8') as EP:
            EP.write("题目:\n")
            for expr in expressions:
                index += 1
                EP.write(str(index)+'、'+str(expr)+'\n')
    def out_put_answer(answers,answerPath):
        index = 0
        with open(answerPath, 'w+', encoding='utf-8') as AP:
            AP.write("各题答案:\n")
            for ans in answers:
                index += 1
                AP.write(str(index) + '、' + str(ans) + '\n')

    def output_grade(gradeFile, correct, wrong):
        with open(gradeFile, 'w+', encoding='utf-8') as gf:
            gf.write("{}".format("Correct: ") + str(len(correct)) + str(correct)\
                     .replace('[','(').replace(']',')') + '\n')
            gf.write("{}".format("Wrong: ") + str(len(wrong)) + str(wrong)\
                     .replace('[','(').replace(']',')') + '\n')