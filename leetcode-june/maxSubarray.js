/*

given an integer array nums, find the configuous subarray (containing at least one number )
which has the largest sum and return its sum.


input: [-2,1,-3,4,-1,2,1,-5,4]

output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.


---- the naive method 
 is to run two loops. The outer loop picks the beginning element, the innter loop finds the maximum possible sum with first
 element picked bu outer loop and compares this maximum with the overall maximum. Finally return the overall maximum.
 The time complexity of the Naive method is (n^2).

*/

const maxSubArray = nums => {
  let maxSoFar = nums[0];
  let maxEndingHere = nums[0];

  for (let i = 1; i < nums.length; i++) {
    console.log(maxEndingHere, "+", a[i], "=", maxEndingHere + a[i]);
    //   1 '+' -2 '=' -1
    //  -1 '+'  2 '=' .1
    //   2 '+' -3 '=' -1
    //  -1 '+'  2 '='. 1
    //   2 '+'  3 '='. 5
    maxEndingHere = Math.max(maxEndingHere + nums[i], nums[i]);
    maxSoFar = (maxSoFar, maxEndingHere);
  }
  return maxSoFar;
};

maxSubArray([1, -2, 2, -3, 2, 3]);
//Kadane's Algorithm
