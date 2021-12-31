for i in range(1,256):
    command = input('输入需要计算的字节')
    #command = 'FF 03 03 00 FF FF FF'
    xorcheck = 0x00
    sumcheck = 0x00
    commandHex = bytes.fromhex(command)
    for i in commandHex:
        sumcheck += i
        xorcheck = i ^ xorcheck
        # print(hex(i))
    sumcheck %= 0x100
    print(hex(xorcheck))
    print(hex(sumcheck))