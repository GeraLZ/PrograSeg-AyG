def ipValida(direccion):
    dir = "0.0.0.0"
    if dir == direccion:
        return False
    x = direccion.split(".")
    if len(x) == 4:
        if int(x[0]) == 0 or int(x[3]) == 0:
            return False
        cont = 0
        for y in x:
                if int(y) >= 0 and int(y) <= 254:
                        cont = cont + 1
        if cont == 4:
            return True
    else:
        return False