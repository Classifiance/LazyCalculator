msg_3 = "Yeah... division by zero. Smart move..."
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
oper = ["+", "-", "*", "/"]
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
memory = 0


def is_one_digit(v):
    k = True
    try:
        if -10 < v < 10 and float(v).is_integer():
            k = k
    except:
        k = False
    return k


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v3):
        msg = msg + msg_6
    if (v1 == 1 or v3 == 1) and v2 == "*":
        msg = msg + msg_7
    if (v1 == 1 or v3 == 1) and (v2 == "*" or v2 == "+" or v2 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    x, ope, y = input(msg_0).split()
    # ca te permet de faire une boucle infinie
    if x == "M":
        x = memory
    elif y == "M":
        y = memory

    try:
        x = float(x)
    except:
        print(msg_1)
        continue
    # continue te ramène au début de la boucle

    try:
        y = float(y)
    except:
        print(msg_1)
        continue

    if ope not in oper:
        print(msg_2)
        continue

    elif ope == "+":

        result = x + y

    elif ope == "-":

        result = x - y

    elif ope == "*":

        result = x * y

    elif ope == "/" and y != 0:

        result = x / y

    else:
        print(msg_3)
        continue
    check(x, ope, y)
    print(result)

    while True:
        # on note que le W de while est minuscule psk on est dans un grand while
        print(msg_4)
        answer = input()
        if answer == "y":
            memory = result
            break
        # on break ce while la et on passe au suivant
        elif answer == "n":
            break
            # print(msg_5)
        elif answer != "n":
            continue
        # on revien ou msg4

    semaphore = False

    while True:
        print(msg_5)
        answer_2 = input()
        if answer_2 == "y":
            semaphore = True
            break
        else:
            if answer_2 == "n":
                break
            else:
                continue

    if semaphore == True:
        continue
    # dcp la on recommence au tt début
    elif semaphore == False:
        break

    else:
        print(msg_2)
        continue