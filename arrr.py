def find_prime():
    lst = [2,3,5,6,7,9]
    new_lst=[]

    for i in lst:
        if i > 1:
            is_prime = True
            for j in range(2,i):
                if i%j==0:
                    is_prime = False
                    break
            if is_prime:
                new_lst.append(i)
    print(new_lst)
find_prime()
