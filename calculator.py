import asyncio, time
from file import history_f

history_file = open("history.txt", "a+")

try:

    async def addition(number1, number2):
        answer = number1 + number2
        return answer

    async def subtraction(number1, number2):
        answer = number1 - number2
        return answer

    async def multiplication(number1, number2):
        answer = number1 * number2
        return answer

    async def division(number1, number2):
        answer = number1 / number2
        return answer

    async def power(number1, number2):
        answer = number1 ** number2
        return answer

    async def HISTORY():
        history_f()
        
except:
    print("error detected...")




async def INPUT():
    try:
        number1 = float(input("Enter number1 :"))
        number2 = float(input("Enter number2 :"))
        return number1, number2
    except:
        print("error")

while True:
    
    op = input("Enter the operator :")

    if op == "+":

        x = asyncio.run(INPUT())
        ans = asyncio.run(addition(x[0], x[1]))
        print(ans)
        history_file.writelines(str(x[0]) + " " + "+" + " " + str(x[1]) + " " + "=" + " " + str(ans) + "\n")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        
    elif op == "-":

        x = asyncio.run(INPUT())
        ans = asyncio.run(subtraction(x[0], x[1]))
        print(ans)
        history_file.writelines(str(x[0]) + " " + "-" + " " + str(x[1]) + " " + "=" + " " + str(ans) + "\n")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

    elif op == "x":

        x = asyncio.run(INPUT())
        ans = asyncio.run(multiplication(x[0], x[1]))
        print(ans)
        history_file.writelines(str(x[0]) + " " + "x" + " " + str(x[1]) + " " + "=" + " " + str(ans) + "\n")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

    elif op == "/":
        
        x = asyncio.run(INPUT())
        ans = asyncio.run(division(x[0], x[1]))
        print(ans)
        history_file.writelines(str(x[0]) + " " + "/" + " " + str(x[1]) + " " + "=" + " " + str(ans) + "\n")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

    elif op == "^":

        x = asyncio.run(INPUT())
        ans = asyncio.run(power(x[0], x[1]))
        print(ans)
        history_file.writelines(str(x[0]) + " " + "^" + " " + str(x[1]) + " " + "=" + " " + str(ans) + "\n")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

    elif op == "s":
        
        print("Calculation is terminated\nCalculations are stored in 'history.txt'")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        history_file.close()
        asyncio.run(HISTORY())
        break
        

    else:

        print("Invalid operator...")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        
    
    
        