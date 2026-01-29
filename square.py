n = float(input("Enter a number:"))
# guess = n/2                                      # Sqrt_n = n** 0.5
# while((guess*guess>n)):                          # print(Sqrt_n)
#     guess=guess - 0.00001

# print("Square root:",guess)



guess = n/2
while(guess !=((guess + n / guess))/2):
    guess = ((guess + n/guess))/2
    print("Guess:",guess)

print("Square root:",guess)