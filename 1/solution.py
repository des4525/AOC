def main():
    nums = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"}
   
    print("Part 1: " +  str(sum([int(min([(line.find(num), num) for num in nums.values() if num in line])[1] + max([(line.rfind(num), num) for num in nums.values() if num in line])[1]) for line in open("input.txt")])))
    print("Part 2: " + str(sum([int(min([(line.find(num), nums[num] if num in nums else num) for num in (list(nums.values()) + list(nums.keys()))  if num in line])[1] + max([(line.rfind(num), nums[num] if num in nums else num) for num in (list(nums.values()) + list(nums.keys())) if num in line])[1]) for line in open("input.txt")])))
    

if __name__ == "__main__":
    main()