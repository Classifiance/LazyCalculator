
operations = ["+", "-", "*", "/"]
memory = 0

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"


def cast_to_int_or_float(usernumber):
    if type(usernumber) == int or type(usernumber) == float:
        return usernumber
    elif "." in usernumber:
        return float(usernumber)
    elif "," in usernumber:
        return float(usernumber)
    else:
        return int(usernumber)


# ok don basic truc pour assigner a float ou int blk un peu


def is_one_digit(v):
    if -10 < v < 10 and float(v).is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()
    if x == "M":
        x = memory
    elif y == "M":
        y = memory
    try:
        x = cast_to_int_or_float(x)
        y = cast_to_int_or_float(y)
    except ValueError:
        print(msg_1)
        continue
    if (type(x) != float and type(x) != int) or (type(y) != float and type(y) != int):
        print(msg_1)
        continue
    if oper not in operations:
        print(msg_2)
        continue
    check(x, y, oper)
    if oper == "+":
        result = x + y
        result = float(result)
        print(result)
    elif oper == "-":
        result = x - y
        result = float(result)
        print(result)
    elif oper == "*":
        result = x * y
        result = float(result)
        print(result)
    elif oper == "/" and y != 0:
        result = x / y
        result = float(result)
        print(result)
    else:
        print(msg_3)
        continue
    answer = input(msg_4)
    if answer == "y":
        memory = result
    answer = input(msg_5)
    if answer == "y":
        continue
    break