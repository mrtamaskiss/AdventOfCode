with open('input.txt', 'r') as f:
    file_input = f.read()

def calculate(input):
    sum = 0
    for line in input.split('\n'): # iterationg through the measurements
        nums = [int(n) for n in line.split()] # splitting the existing values

        allnums = []
        allnums.append(nums) # adding the existing values to a 2 dimensional array as the first element
        
        # filling the array with the 'pyramid' based on the existing values
        while not all(val == 0 for val in nums):
            nums = []
            for i in range(0, len(allnums[len(allnums)-1])-1):
                nums.append( (allnums[len(allnums)-1][i+1]-allnums[len(allnums)-1][i]))
            allnums.append(nums)

        # calculate the next value
        
        i = len(allnums)-1
        allnums[i].append(0) # fill the 0 to the last line

        # building up the stairs
        while i>0:
            i -= 1
            allnums[i].append( allnums[i+1][len(allnums[i+1])-1] + allnums[i][len(allnums[i])-1] )

        # # print the 'pyramid'
        # for i in range(0, len(allnums)):
        #    print (i, '\t', allnums[i])

        sum += allnums[0][len(allnums[0])-1] # adding the new value to the sum
    return sum

print('Part 1 value:', calculate(file_input))