
*
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1]
 then that's the value of last stone.
*/
var lastStoneWeight = function(stones) {
  const sorted = stones.sort();
  let stoneX = stones[sorted.length - 2];
  let stoneY = stones[sorted.length - 1];
  console.log(sorted, sorted.pop(2));
  // while(stoneX != null) {

  // }
  // if x == y both stones are totally destroyed
  // if x !==  y the stone of weight x is totally destroyed, and the stone of weight
  // y has new weight y = y-x
  // if there's only 1 stone left return or 0 if there are no stones left.
};
lastStoneWeight([2, 7, 4, 1, 8, 1]);
