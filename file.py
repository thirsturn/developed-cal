


def history_f():
    fo = open("history.txt", "a+")
    history = fo.readlines()
    for i in range(len(history)):
        print(history[i])
    fo.close()


  

