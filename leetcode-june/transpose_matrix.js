/*  Transpose Matrix
 Given a matrix , return the transpose of A.
 - notes
 The tranpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
 Example : 1
 I: [[1,2,3], [4,5,6], [7,8,9]]
 O: [[1,4,7], [2,5,8], [6,6,0]]
 Example : 2
 I: [[1,2,3], [4,5,6]]
 O: [[1,4], [2,5] , [3,6]]

 Note:
  1. 1 <= A.length <= 1000
  2. 1 <= A[0].length <= 1000
MY Understanding of problem
- [] base on the length of the matrix that's how many split i need.
- [] place all the first indices base on the length of matrix
  */

//============= solution 1 =================
const transpose = a => {
  // outer grab the length
  let matrix = [];
  for (let i = 0; i < a[0].length; i++) {
    // inner
    matrix[i] = [i];
    for (let y = 0; y < a.length; y++) {
      console.log(matrix, a[y][i]);
      //result[a[y].length] = a[y][i];
      matrix[i][y] = a[y][i];
    }
  }
  return matrix;
};

//console.log(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));
//console.log(transpose([[1, 2, 3], [4, 5, 6]]));

//============= solution 2 =================
const transpose2 = A => {
  // set empty arr length of inner
  let res = new Array(A[0].length);

  for (let i = 0; i < res.length; i++) {
    // res[i] is 1 , 2, 3 is the length of inner items
    // new Array(A.length); how many []
    res[i] = new Array(A.length);
    // inner loop
    for (let j = 0; j < res[i].length; j++) {
      // add all first indices of arr
      // console.log(res, A[j][i]);

      res[i][j] = A[j][i];
    }
  }
  return res;
};
console.log(transpose2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));
