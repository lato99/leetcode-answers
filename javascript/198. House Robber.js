/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  var n = nums.length;
  var dp = Array(n).fill(-1);
  return helper(nums, 0, dp);
};

var helper = (nums, index, dp) => {
  if (index >= nums.length) {
    return 0;
  } else if (dp[index] != -1) {
    return dp[index];
  }
  var currRob = nums[index] + helper(nums, index + 2, dp);
  var currNotRob = helper(nums, index + 1, dp);
  dp[index] = Math.max(currRob, currNotRob);
  return dp[index];
};
