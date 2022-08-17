def house():
    length = ''
    width = ''
    area =''
    length = input("What's the length of your house? ")
    width = input("What's the width of your house? ")
    area = float(length) * float(width)
    print(f'Your house is {area} feet!')
