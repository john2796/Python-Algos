/*
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
*/

var commonChars = function(A) {
  // get first item in array and split each char
  let originalChars = A[0].split("")
  // loop through array starting from second index
  for (let i = 1; i < A.length; i++) {
    // split rest of item in A array
    let tempChars = A[i].split("")
    // reasigned originalChars to filtered items
    originalChars = originalChars.filter(item => {
      // get index of each tempChars
      // The indexOf() method returns the first index at which a given element can be found in the array
      let index = tempChars.indexOf(item)
      // -1 if it is not present.
      // console.log("tempChars[index]", tempChars[index])
      // if index greater than -1 that means it's present set tempChars[index] to true else false
      return index > -1 ? (tempChars[index] = true) : false
    })
  }

  // console.log(originalChars)
  return originalChars
}

commonChars(["bella", "label", "roller"])
commonChars(["cool", "lock", "cook"])
