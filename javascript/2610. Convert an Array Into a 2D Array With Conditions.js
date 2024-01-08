/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var findMatrix = function (nums) {
  var freq = new Array(nums.length + 1).fill(0);
  var ans = [];
  for (let num of nums) {
    freq[num]++;
    if (ans.length < freq[num]) {
      ans.push([]);
    }
    ans[freq[num] - 1].push(num);
  }
  return ans;
};
