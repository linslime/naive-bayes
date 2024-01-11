import math
import csv



def bayes():
    filename = 'D:\\document\\code\\naiveBayes\\mainProcess\\西瓜的数据集.csv'
    data = []
    with open(filename, encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        for row in csv_reader:
            data.append(row)
    for x in data:
        train(x[0:6], x[-1])



def HANDLE1(key):
    return number[key] / allNumber


def HANDLE(tag, key):
    tmp_tags = tagNumber[key]
    if tag not in tagNumber[key]:
        return landa / (number[key] + len(tmp_tags) * landa)
    return (tmp_tags[tag] + landa) / (number[key] + len(tmp_tags) * landa)

def train(taglist, key):

    global allNumber
    allNumber += 1
    if key in number:
        number[key] += 1
    else:
        number[key] = 1
    if key not in tagNumber:
        tagNumber[key] = {}
    tmp_tags = tagNumber[key]
    for tag in taglist:
        if tag in tmp_tags:
            tmp_tags[tag] += 1
        else:
            tmp_tags[tag] = 1



def test(test_tags):
    res = ''
    res_P = None
    for key in number.keys():
        log_HANDLE = 0
        for tag in test_tags:
            log_HANDLE += math.log(HANDLE(tag, key), 2)
        tmp_P = log_HANDLE + math.log(HANDLE1(key), 2)
        if res_P is None:
            res = key
            res_P = tmp_P
        if tmp_P > res_P:
            res = key
            res_P = tmp_P
    return res, res_P

allNumber = 0
number = {}
tagNumber = {}
landa = 0.6




if __name__ == '__main__':
    bayes()
    testcs = ['乌黑', '稍蜷', '浊响', '清晰', '凹陷', '软粘']
    print("单例测试为：", testcs)
    print('测试结果：', test(testcs))

