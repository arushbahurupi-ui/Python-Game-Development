i_n = int(input("Enter your weight: "))
print(i_n)
w_type = input("(L)bs or (K)g: ")
if w_type.upper() == "L":
    n_w = i_n / 2.205
    print(f"Your weight in Kg's is: {n_w}")
elif w_type.upper() == "K":
    n_w = i_n * 2.205
    print("Your weight in Lbs is:", n_w)