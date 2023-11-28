/**
 * @param {number[]} dist
 * @param {number[]} speed
 * @return {number}
 */
var eliminateMaximum = function (dist, speed) {
  const n = dist.length;
  var arrivalTime = new Array(n);
  for (var i = 0; i < n; i++) {
    arrivalTime[i] = dist[i] / speed[i];
  }
  arrivalTime.sort((a, b) => a - b);
  var ans = 0;
  while (ans < n && arrivalTime[ans] - ans > 0) {
    ans += 1;
  }
  return ans;
};
