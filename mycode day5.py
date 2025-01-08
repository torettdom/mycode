#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Enter a positive integer: "))

for i in range(1, n + 1):
    print(i)

sum_of_numbers = 0
counter = 1
while counter <= n:
    sum_of_numbers += counter
    counter += 1

print("The sum of numbers from 1 to", n, "is:", sum_of_numbers)


# In[2]:


def calculate_square(n):
    return n ** 2

def main():
    try:
        user_input = int(input("Enter a positive integer: "))
        if user_input < 0:
            print("Error: Please enter a positive integer.")
        else:
            result = calculate_square(user_input)
            print(f"The square of {user_input} is {result}.")
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()


# In[ ]:




