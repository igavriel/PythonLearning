import sys
import traceback
from pprint import pprint as pp

class BullsAndCows:
    def __init__(self):
        self.reset()

    def reset(self):
        self._bulls = 0
        self._cows = 0
    
    @property
    def bulls(self):
        return self._bulls

    @property
    def cows(self):
        return self._cows

    def add_bull(self):
        self._bulls = self._bulls + 1
        
    def add_cow(self):
        self._cows = self._cows + 1

    def won(self):
        return self.bulls == 4

class BullsAndCowsGame:

    def __init__(self, code: int):
        self._code = code % 10000   # force 4 digits number
        self._code_set = self._validate_num(self._code)
        
    def _validate_num(self, num: int):
        new_num = num
        code_set = set()
        
        for i in range(0,4):
            digit = new_num%10
            new_num = int(new_num/10)
            if(digit not in code_set):
                code_set.add(digit)
                #pp(f"add {digit} to {code_set}")
            else:
                raise ValueError("duplicate digits")
        return code_set

    def guess(self, num: int):
        code = num % 10000   # force 4 digits number
        self._validate_num(code)

        if(code == self._code):
            print("you won")
            return True
        
        the_code = self._code
        bc = BullsAndCows()
        for i in range(0,4):
            digit = code%10
            code_digit = the_code%10
            
            code = int(code/10)
            the_code = int(the_code/10)
            
            if digit==code_digit:
                bc.add_bull()
                continue
            elif digit in self._code_set:
                bc.add_cow()
                continue

        pp(f"Bulls {bc.bulls}, Cows {bc.cows}")
        return False


def main(code: int):
    pp(code)
    code_num = int(code)
    try:
        bc = BullsAndCowsGame(code_num)
        
        guess = False
        count = 0
        while guess is not True :
            try:
                user_input = input(f"Guess {count}: ")
                count = count+1
                if user_input == '0':
                    break
                guess = bc.guess(int(user_input))

            except ValueError as err:
                pp(err)
            except:
                error_info = traceback.format_exc()
                pp(error_info)
                
    except ValueError as err:
        pp(err)

if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename
