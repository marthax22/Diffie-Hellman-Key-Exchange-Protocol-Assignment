#Author: marthachd

#Υλοποίηση του αλγορίθμου 7.2.3
def square_multiply(base, exp, mod):
   
    result = 1
    base = base % mod
    
    while exp > 0:
        # Αν το τρέχον bit είναι 1,το πολλαπλασιάζει
        if exp % 2 == 1:
            result = (result * base) % mod
        # Τετραγωνίζει τη βάση
        base = (base * base) % mod
        # πάει στο επόμενο bit
        exp = exp // 2
    
    return result

#Πρωτόκολλο ανταλλαγής κλειδιών Diffie-Hellman
def diffie_hellman_protocol(g, p, a, b):
  
    print("Πρωτόκολλο Diffie-Hellman")
    print("Δημόσιες παράμετροι")
    print(f"p = {p}")
    print(f"g = {g}")
    print(f"\nΤο μυστικό κλειδί της Alice είναι a = {a}")
    print(f"Το μυστικό κλειδί του Bob είναι b = {b}")

    #Για την Alice το δημόσιο κλειδί είναι: A = g^a mod p
    A = square_multiply(g, a, p)
    print(f"\nΤο δημόσιο κλειδί της Alice είναι: ")
    print(f"A = g^a mod p = {g}^{a} mod {p} = {A}")
    
    #Για τον Bob το δημόσιο κλειδί είναι: B = g^b mod p
    B = square_multiply(g, b, p)
    print(f"\nΤο δημόσιο κλειδί του Bob είναι: ")
    print(f"B = g^b mod p = {g}^{b} mod {p} = {B}")
    
    #Υπολογισμός κοινού κλειδιού
    # Alice: K = B^a mod p
    K_alice = square_multiply(B, a, p)
    print(f"\nΥπολογισμός κοινού κλειδιού:")
    print(f"Alice: K = B^a mod p = {B}^{a} mod {p} = {K_alice}")
    
    # Bob: K = A^b mod p
    K_bob = square_multiply(A, b, p)
    print(f"Bob: K = A^b mod p = {A}^{b} mod {p} = {K_bob}")
    print("\n")
    
    # Επαλήθευση
    if K_alice == K_bob:
        print(f"Το κοινό κλειδί είναι: K = {K_alice}")
    else:
        print("Τα κλειδιά δεν συμφωνούν.")
  
    return K_alice

#Κύριο Πρόγραμμα 
g = 3   #g: generator
p = 101 #p: πρώτος αριθμός (prime)
a = 77  #a: μυστικό κλειδι Alice
b = 91  #b: μυστικό κλειδί Bob
    
key = diffie_hellman_protocol(g, p, a, b) #κοινό κλειδί
