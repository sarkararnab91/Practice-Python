from functools import reduce

class FindNumber():
    def __init__(self):
        self.minim = 0
        self.sum=0
    def _min_n(self,x,y):
        return x if x <= y else y
    def minimum(self,*args):
        alist = list(map(int, args))
        #print(alist)
        # Use filter to filter out smallest number
        asmall_list = reduce(self._min_n, alist)
        print("smallest numbers", asmall_list)
        return asmall_list
    
    def palindrome(self,n):
        word = str(n)
        print(word)
        return print("yes") if word == word[::-1] else print("no")
    
    def _div_by_four(self,n):
        if n%4==0:
            self.sum+=n
            return True
    def div_by_four_sum(self):
        while True:
            user_input = input("Enter a number: ")
            if user_input == "exit":
                break
            try:
                n = int(user_input)
                if self._div_by_four(n):
                    print("Sum of numbers divisible by 4: ", self.sum)
                else:
                    print("Not divisible by 4")
            except ValueError:
                print("Enter a valid number")
                continue


class DigitOperate(FindNumber):

    def __init__(self):
        pass

    def armstrong_number(self,n:int):
        int_n_list = map(int,list(str(n)))
        cube_power_sum = True if reduce(lambda x,y: x+y, map(lambda x: x**3, int_n_list)) == n else False
        if cube_power_sum:
            print("Armstrong number")
        else:
            print("Not an Armstrong number")
        


