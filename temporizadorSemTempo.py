m = int(input("Digite os minutos (entre 0 a 60): ")) 
s = int(input("Digite os segundos (entre 0 a 60): "))

t = 60

for n in range(m, -1, -1):
    for i in range(s, -1, -1):
        while n <= m:
            s = t
            print(n,"min", i,"s")
            break

if n == 0 and i == 0:
    print("tempo esgotado")
        
    
        
