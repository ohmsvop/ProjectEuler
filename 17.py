# Number letter counts

dictionary = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
              6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
              11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
              15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
              19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 
              50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
              90: "ninety", 100: "hundred", 1000: "thousand"}

def digit_to_english(n):
    english_number = []
    
    if n == 1000:
        english_number.extend([dictionary[1], dictionary[n]])
        return english_number
    
    if n >= 100:
        n100 = n/100
        english_number.extend([dictionary[n100], dictionary[100]])
        if n % 100 == 0:
            return english_number 
        else:    
            english_number.append("and")

    n = n % 100
    if n > 20:
        n1 = n % 10
        n10 = n - n1 
        if n1 != 0:
            english_number.extend([dictionary[n10],dictionary[n1]])
        else:
            english_number.append(dictionary[n10])
    else:
        english_number.append(dictionary[n])
    return english_number

total_length = 0
for i in range(1, 1001):
    words = digit_to_english(i)
    total_length += len("".join(words))
