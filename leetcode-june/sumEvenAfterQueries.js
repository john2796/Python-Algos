/*
 Sum of Even Number after Queries 

 We have an array A of integers, and an array queries of queries.
 
 For the i-th query val = queries[i][0],. Then, the answer to i-th query is the we add val to A[]wer to i-th queryindex is th. Then, the answer to i A[]e sum of the even values oindexf A.L0. Then, the answer to i-th query is the sum of the even values of A.

 (Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

 Return the answer to all queries. Your answer array should have answer[i] as the answer to the i-th query.


 I:  A = [1,2,3,4], queries = [[1,0], [-3,1], [-4,0], [2,3]]
 O: [8,6,2,4]
 
 Explanation:
 At the beginning, the array is [1,2,3,4].
 After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is
  2 + 2 + 4 = 8.
 After adding -3 to A[1], the array is [2, -1, 3, 4], and the sum of eve values is 2 + 4 = 6.
 After adding -4 to A[0], the array is [-2, -1, 3, 4], and the sum of even values is -2 + 4 = 2.
 After adding to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
 */

// const sumEvenAfterQueries = (A, queries) => {
//   let a_counter = 0;
//   let q_counter = 0;

//   for (let i = 0; i < A.length; i++) {
//     if (i % 3 === 0) {
//       a_counter = 0;
//     }

//     let qValue = queries[q_counter][0];
//     A[a_counter] = qValue + A[a_counter];
//     console.log(A, A[i], qValue, A[a_counter]);

//     // A[i] = a_counter + qValue;
//     q_counter += 1;
//     a_counter += q_counter;
//   }
const sumEvenAfterQueries = (A, queries) => {
  for (let i = 0; i < queries.length; i++) {
    A[queries[i][1]] += queries[i][0];
    // [ 2, 2, 3, 4 ]
    // [ 2, -1, 3, 4 ]
    // [ -2, -1, 3, 4 ]
    // [ -2, -1, 3, 6 ]
    queries[i] = A.reduce((acc, a) => (a % 2 == 0 ? acc + a : acc), 0);
  }
  return queries;
};

sumEvenAfterQueries([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]);
