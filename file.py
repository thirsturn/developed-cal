fo = open("history.txt", "r")
def history_f():
    
    history = fo.readlines()

    for i in range(len(history)):
        print(history[i])

    fo.close()

