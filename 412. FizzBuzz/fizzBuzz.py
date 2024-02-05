class Solution(object):
    def fizzBuzz(self, n):
        list = []

        for count in range(1, n + 1):
            if count % 3 == 0 and count % 5 == 0:
                list.append("FizzBuzz")
            elif count % 3 == 0:
                list.append("Fizz")
            elif count % 5 == 0:
                list.append("Buzz")
            else:
                list.append(str(count))
                
        return list