def the_power_of_two(N):

    if N % 2 != 0:
        print("NO")

    elif N != 2 and N % 2 == 0:
        the_power_of_two(N//2)
        print("YES")


the_power_of_two(16)