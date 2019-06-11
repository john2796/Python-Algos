//-------------------- remoeDuplicates-----------------------

// implementation 1
//const removeDuplicates = nums => {
//const unique = Array.from(new Set(nums));
//return unique;
//};

//console.log(removeDuplicates([1, 1, 2]));

//--------------- in place O(1) -------------------
const removeDuplicates = nums => {
  let y = 0;
  // loop through nums length
  for (let i = 0; i < nums.length; i++) {
    // if nums[i] is not equal to nums[0]
    console.log(nums[i], nums[y]);
    if (nums[i] !== nums[y]) {
      // update nums
      nums[++y] = nums[i];
    }
  }
  // else return length of nums and and 1 to go to next number
  return nums.length && y + 1;
};

console.log(removeDuplicates([1, 1, 2]));

//const removeElement = (nums, val) => {
//let y = 0;
//for (let i = 0; i < nums.length; i++) {
//if nums i is equal to 3
//if (nums[i] == val) {
//remove it to current nums
//val[++y] = nums[i];
//}
//}
//return nums.length && y + 1;
//};

//console.log(removeElement([3, 2, 2, 3], 3));
