/*

given an integer array nums, find the configuous subarray (containing at least one number )
which has the largest sum and return its sum.


input: [-2,1,-3,4,-1,2,1,-5,4]

output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.

*/

const maxSubArray = nums => {
  let max_current = nums[0];
  let max_global = nums[0];
  for (let i = 0; i < nums.length; i++) {
    max_current = Math.max(nums[i] + max_current + nums[i]);
    if (max_current > max_current) {
      max_global = max_current;
    }
  }
  return max_global;
};

console.log(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
