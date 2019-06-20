/*
  this will not work 
    - [x] constraint , Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) constant extra memory.


  const reverseString = s => {
  let res = [];
  for (let i = s.length - 1; i >= 0; i--) {
    res[res.length] = s[i];
  }
  return res;
};

console.log(reverseString(["h", "e", "l", "l", "o"]));
*/

const reverseString = s => {
  for (let i = 0, j = s.length - 1; i < j; i++, j--) {
    const x = s[i]; // 0, 1, ,3, 4
    const y = s[j]; // 4 ,3 ,2 ,1
    s[i] = y; // assinging values
    s[j] = x;
  }
  return s;
};

console.log(reverseString(["h", "e", "l", "l", "o"]));
