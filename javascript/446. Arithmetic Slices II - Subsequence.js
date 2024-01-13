/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfArithmeticSlices = function (nums) {
  let dp = [];
  let ans = 0;
  let n = nums.length;

  for (let i = 0; i < n; i++) {
    dp.push(new Map());
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < i; j++) {
      let diff = nums[i] - nums[j];

      if (dp[i].has(diff)) {
        // If there are previous subarrays ending at j with the same difference
        // Add those to the count and extend the subarrays ending at i
        dp[i].set(diff, dp[i].get(diff) + 1);
      } else {
        // Initialize the difference in the map
        dp[i].set(diff, 1);
      }

      if (dp[j].has(diff)) {
        dp[i].set(diff, (dp[i].get(diff) || 0) + dp[j].get(diff));
        ans += dp[j].get(diff);
      }
    }
  }

  return ans;
};
