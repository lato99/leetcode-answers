/**
 * @param {string[]} bank
 * @return {number}
 */
var numberOfBeams = function (bank) {
  var prevBeans = 0;
  var ans = 0;
  for (let str of bank) {
    var noCurBeam = getNoBeams(str);
    if (noCurBeam === 0) {
      continue;
    } else if (prevBeans === 0) {
      prevBeans = noCurBeam;
    } else {
      ans += prevBeans * noCurBeam;
      prevBeans = noCurBeam;
    }
  }
  return ans;
};

const getNoBeams = (row) => {
  var ans = 0;
  for (let i = 0; i < row.length; i++) {
    if (row.charAt(i) === "1") {
      ans += 1;
    }
  }
  return ans;
};
