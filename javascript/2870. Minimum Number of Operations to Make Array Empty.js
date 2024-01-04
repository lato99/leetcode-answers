/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function (nums) {
  let map = {};
  let ans = 0;
  for (let num of nums) {
    if (map.hasOwnProperty(num)) {
      map[num] = map[num] + 1;
    } else {
      map[num] = 1;
    }
  }
  for (let key in map) {
    let val = map[key];
    if (val === 1) {
      return -1;
    } else if (val === 2) {
      ans += 1;
    } else {
      while (val !== 0) {
        if (val % 3 === 0) {
          ans += val / 3;
          break;
        } else {
          val -= 2;
          ans += 1;
        }
      }
    }
  }
  return ans;
};

//Time complexity : O(N), n is the length of the nums array. We iterate over the nums to put the values into the hashmap, then we iterate over the hashmap. In the while loop, the worst case of iteration until breaking out of the while loop is v/2 which is constant O(1). Therefore Time complexity is O(N) in worst case.
// Space complexity : O(N), this is because we put the nums into a hash map, and in worse case every value has one occurence, and in that case, we get O(N) space complexity.
