class Solution:
    def findMissingNumbers(self, numbers):
            #type numbers: list of float
            #return type: list of int
            if len(numbers) == 0:
                 return "Invalid input"
            if len(numbers) == 1:
                 return "None missing"
            
            #TODO: Write code below to return an int list with the solution to the prompt.
            missing = []
            for i in range(len(numbers)-1):
                if numbers[i+1] > (numbers[i] + 1):
                     for num in (numbers[i+1]-numbers[i]):
                        missing.append(numbers[i]+num)
            return missing
            pass

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = float(array[x])

    tc1 = Solution()
    ans = tc1.findMissingNumbers(array)
    print(ans)

if __name__ == "__main__":
    main()
    
#listOfNumbers = [0, 3, 3, 3, 4, 7, 3]  # STEP 1: get the in input
#print(findMissingNumbers(listOfNumbers)) # Step 2: Call a function to handle the input
