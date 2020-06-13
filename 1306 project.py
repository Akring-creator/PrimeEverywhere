
print(
"""
.: Yuk kita cari bilangan prima terdekat :.
.:   Silahkan, Masukkan Angka di bawah   :.
""")
num = int(input("Number: "))
def ptdb(i = num): # prime_terdekat_dari_bawah
    
    bb = i - 1
    prime1 = 0
    while prime1 == 0:
        for num_a in range (bb, i):
            for x in range (2, num_a):
                if num_a % x == 0:
                    bb -= 1
                    break
            else:
                prime1 = num_a
            break    
    return prime1


def ptda(i = num): # prime_terdekat_dari_atas
    
    ba = i + 1 #Batas Atas
    prime2 = 0
    while prime2 == 0:
        for num_a in range (i, ba):
            for x in range (2, num_a):
                if num_a % x == 0:
                    ba += 1
                    i+= 1
                    break
            else:
                prime2 = num_a
            break
    return prime2

pb = ptdb()
pa = ptda()

def pt():
    sb = num - pb
    sa = pa - num
    if pa == num:
        return f'{pa} adalah bilangan prima :D'
    elif sb > sa:
        return f'{pa} merupakan bilangan prima terdekat dari {num}'
    elif sa > sb:
        return f'{pb} merupakan bilangan prima terdekat dari {num}'
print(pt())
print(".: Selesai :.")
            
    
