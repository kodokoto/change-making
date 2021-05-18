import time

change = 16
coinSet = (1, 5, 12, 20)
memory = {} # here the results of cn(x) will be stored in the format ['16': 4]

def efficient(x :int) -> int: # worst case scenario should be O(n)
    if x == 0:
        return 0
    elif x in memory: # if x in is memory then we have already calculated it
        return memory[x]
    else:
        # this line is equivalent to cn(x) = 1 + min(cn(x-1), cn(x-5), cn(x-12), cn(x-20))
        # but I use a list comprehension to not only make it more consise, but to also make it expandable
        memory[x] = 1 + min(efficient(x-i) for i in coinSet if x-i>=0) # filter out any negative x
        return memory[x]

# this is my one liner version of this function which doesnt use the dictionary to store previous values
# roughly O(1.346^n)
cn = lambda x: 0 if x==0 else 1 + min([cn(x-i) for i in (1, 5, 12, 20) if x-i>=0])

# its a low slower, cost of efficiency for aesthetics

cn_start = time.time()
print(cn(change)) # on my computer cn(50) takes 7 seconds, I wouldnt go much higher than that
cn_end = time.time()

cn_speed = cn_end - cn_start

efficient_start = time.time()
print(efficient(change)) # this is super fast, even around the maximum recursion depth its still around 1/100th
efficient_end = time.time()

efficient_speed = efficient_end - efficient_start

percentage = (cn_speed/efficient_speed)*100

print(f"Brute force: {cn_speed}, dynamic: {efficient_speed}")
print(f" efficient({change}) is {round(percentage)}% faster than cn({change})")


