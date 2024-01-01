/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function (g, s) {
  g.sort(sortNum);
  s.sort(sortNum);
  var gIndex = 0;
  var sIndex = 0;
  while (gIndex < g.length && sIndex < s.length) {
    var gVal = g[gIndex];
    var sVal = s[sIndex];
    if (gVal <= sVal) {
      gIndex += 1;
      sIndex += 1;
    } else {
      sIndex += 1;
    }
  }
  return gIndex;
};

const sortNum = (a, b) => {
  return a - b;
};
