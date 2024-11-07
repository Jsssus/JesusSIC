import found_cal as fc
def main():
    t = int(input("ingresa un numero de personas que participaron: "))
    total = fc.fund(t)
    
    print("la donacion fue de:", total)
    
main()