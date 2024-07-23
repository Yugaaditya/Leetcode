class Solution:
    #Time Complexity- O(n)
    #Space Complexity- O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        i,currSum=0,0
        #intializing the current sum to be zero and the index to be zero
        
        ans=float('-inf') #here i will store my answer

        while i!=len(nums):  #iterating over the array
            currSum+=nums[i]  #finding the currentsum
            ans=max(ans,currSum)  #finding the maximum sum after every iteration

            #if the current sum is less than zero then make the current sum=0 and iterate further
            #now suppose there are only negative number (edge case) ,using this it will take the least negative number
            #suppose if there were positive numbers also then when the current sum is less than zero
            #it is better to discard that sum and move on ahead as we know that sum will atleast be
            #positive in this case
            if currSum<0:                  
                currSum=0
            i+=1
        return ans
