/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var getWinner = function (arr, k) {
  var l = arr[0];
  var winStreak = 0;
  for (var i = 1; i < arr.length; i++) {
    var r = arr[i];
    if (l > r) {
      winStreak += 1;
    } else {
      l = r;
      winStreak = 1;
    }
    if (k == winStreak) {
      return l;
    }
  }
  return l;
};
