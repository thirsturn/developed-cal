fo = open("history.txt", "r")
history = fo.readlines()

def history_f():

    for i in range(len(history)):
        print(history[i])

    fo.close()

def clean():

    history.clear()

    fo.close()

