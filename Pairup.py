class pair_elements:

    def TwoSum(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = 1

value = int(input("Enter sum you would like : "))

print("index 1 = %d, index 2 = %d" % pair_elements().TwoSum((10, 20, 30, 40, 50, 60, 70), value))
