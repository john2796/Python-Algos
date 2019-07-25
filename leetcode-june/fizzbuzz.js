/* Fizz Buzz



*/

var fizzbuzz = function(n) {
  let result = []
  // Write a program that outputs the string representation of numbers from 1 to n.
  for (let i = 1; i < n + 1; i++) {
    // For numbers which are multiples of both three and five output “FizzBuzz”.
    if (i % 15 === 0) {
      result[result.length] = "FizzBuzz"
      // But for multiples of three it should output “Fizz”
    } else if (i % 3 === 0) {
      result[result.length] = "Fizz"
    }
    //  instead of the number and for the multiples of five output “Buzz”.
    else if (i % 5 === 0) {
      result[result.length] = "Buzz"
    } else {
      result[result.length] = String(i)
    }
  }
  return result
}

console.log(fizzbuzz(15))
