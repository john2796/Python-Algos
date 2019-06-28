/* Valid Palindrom 
Given a string, determine if it is a palindrome, considering only alphanumeric characters andd ignoring cases.

Note: For the purpose of this problem,  we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama" ->> true

Example 2:
Input "race a car" -> false

*/

// valid pandindrom is when you reverse the words it would match the original
function validPalindrome(s) {
  // only have alphanumeric
  s = s.replace(/[^0-9a-zA-Z]+/gim, "")
  s = s.toLowerCase()

  // using two pointer
  // one starts at the beginning
  // one at end of s
  let l = 0
  let r = s.length - 1
  // while 0 < length - 1
  while (l <= r) {
    // if char doesn't match return false right away
    if (s[l] !== s[r]) {
      return false
    }
    // else increment the pointer
    l++
    r--
  }
  // once all string has been traversed return true
  return true
}

console.log(validPalindrome("race a car"))
