"""Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

Пример:

2 + 2 => 4;

1 + 2 * 3 => 7;

1 - 2 * 3 => -5;"""


def WriteListToFile(fileName, textData):
    textData = '- The result of the expression is ' + str(textData) + '\n'
    with open(fileName, "a") as file:
       file.write(textData)
       file.close

def StrParse(str):
    lenght = len(str)
    flag = False
    operand_1_str = ''
    operand_2_str = ''
    for i in range (lenght):
        if str[i].isdigit() or (str[i]=='-' and i==0):
            if flag == False:
                operand_1_str = operand_1_str+str[i]
        else:
            flag = True
            operation = str[i]
            break
    for i in reversed(str):
        if i.isdigit():
            if flag == True:
                operand_2_str = operand_2_str+i
        else:
            flag = False
            break
    operand_1 = float(operand_1_str)
    operand_2 = float(operand_2_str[::-1])
    return [operand_1, operand_2, operation]

def GetOperation(operands):
    match operands[2]:
        case '+':
            result = operands[0]+operands[1]
        case '-':
            result = operands[0]-operands[1]
        case '/':
            try:
                result = operands[0]/operands[1]
            except ZeroDivisionError:
                print("Zero division!")
                return None
        case '*':
            result=operands[0]*operands[1]
    return result

inputStr=input("арифметическоге выражение заданное строкой: ")
operands=StrParse(inputStr)
result=GetOperation(operands)
WriteListToFile('LogData.txt',result)
print(f" result  {inputStr} = {result}")