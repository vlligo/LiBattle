i = 1

while True:
    try:
        exec("import b" + str(i))
        exec("b" + str(i) + ".main()")
        i += 1
    except:
        break
