def ar keliamieji(x:int) ->bool:
    if x % 400 == 0 or x %100 ! =0 and x % 4 == 0:
        return True
    else:
        return False

print(ar_keliamieji(2000))