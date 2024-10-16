# TODO Найдите количество книг, которое можно разместить на дискете
v = 1.44  # Mb
pages = 100
strings = 50
symbols = 25
v_symbol = 4  # b


v *= 1024 * 1024

otv = int(v // (pages * strings * symbols * v_symbol))

print("Количество книг, помещающихся на дискету:", otv)
