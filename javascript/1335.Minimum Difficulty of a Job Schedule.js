/**
 * @param {number[]} jobDifficulty
 * @param {number} d
 * @return {number}
 */
var minDifficulty = function (jobDifficulty, d) {
  return dpHelper(jobDifficulty, d);
};

var dpHelper = function (jobDifficulty, d) {
  var n = jobDifficulty.length;
  if (n < d) {
    return -1;
  }
  const dp = new Array(n + 1).fill(null).map(() => Array(d + 1).fill(Infinity));
  dp[0][0] = 0;

  for (let i = 1; i < n + 1; i++) {
    for (let j = 1; j < d + 1; j++) {
      var max_diff = 0;
      for (let k = i; k > 0; k--) {
        max_diff = Math.max(max_diff, jobDifficulty[k - 1]);
        dp[i][j] = Math.min(dp[i][j], max_diff + dp[k - 1][j - 1]);
      }
    }
  }
  return dp[n][d] === Infinity ? -1 : dp[n][d];
};
