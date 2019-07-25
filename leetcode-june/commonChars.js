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
  let originalChars = A[0].split("")
  for (let i = 1; i < A.length; i++) {
    let tempChars = A[i].split("")

    originalChars = originalChars.filter(item => {
      let index = tempChars.indexOf(item)
      return index > -1 ? tempChars[index] : false
    })
  }

  console.log(originalChars)
  return originalChars
}

commonChars(["bella", "label", "roller"])
commonChars(["cool", "lock", "cook"])
