//find the longest common prefix string amongs an array of strings.

const longestCommonPrefix = arr => {
  if (arr.length === 0) return "";

  // make a copy of array and sort
  const sorted_arr = arr.concat().sort();
  //first item
  const r1 = sorted_arr[0];
  //second item in sorted array
  const r2 = sorted_arr[arr.length - 1];
  let a = 0;

  while (a < r1.length && r1.charAt(a) === r2.charAt(a)) {
    a++;
  }
  return r1.substring(0, a); // return substring from r1 start to loop in    common
};

console.log(longestCommonPrefix(["flower", "flowers", "flight"]));
