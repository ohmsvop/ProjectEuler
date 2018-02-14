import numpy as np

def streak(n):
    i = 1
    count = 0
    while n % i == 0:
        # print n,i
        n += 1
        i += 1
        count += 1
    return count

def find_multiplier(multiplier):
    interval = int(np.prod(multiplier))
    start = interval + 1
    streak_ini = streak(start)
    m = 1
    n = start
    while True:
        n += interval
        m += 1
        # print n, streak(n), streak_ini, "*"
        if streak(n) != streak_ini:
            break
    return m

def find_number(start, interval, upperbound):
    return (upperbound-start)/interval + 1

def pfunction(power):
    sum_n = 0
    if multiplier_s.index(power):
        m0 = multiplier_s.index(power) + 1
        interval = np.prod(multiplier[:m0+1])
        m1 = multiplier[m0]
        m2 = interval/m1
        start = 1
        for i in range(m1-1):
            start += m2
            n = find_number(start,interval,4**power)
            sum_n += n
            # print "{}+{}n\t{}".format(start,interval, n)
    return sum_n

if __name__ == "__main__":

    # multiplier = []
    #for i in range(10):
    #    multiplier.append(find_multiplier(multiplier))

    multiplier = [1,2,3,2,5,7,2,3,11,13,2,17,19,23,5,3,29,31,2,37,41]

    # multiplier_s = []
    # for i in range(1,20):
    #    multiplier_s.append(streak(np.prod(multiplier[:i])+1))

    multiplier_s = [1, 2, 3, 4, 6, 7, 8, 10, 12, 15, 16, 18, 22, 24, 26, 28, 30, 31, 36]

    sum_p = 0
    for i in multiplier_s[1:-1]:
        sum_p += pfunction(i)
        # print pfunction(i),

    print sum_p + 1
    # final asnwer = 1617243
