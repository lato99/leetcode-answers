/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function (nums) {
  var freq = new Array(nums.length).fill(0);
  for (let num of nums) {
    freq[num - 1]++;
  }
  var missingNum = 0;
  var duplicateNum = 0;
  for (var i = 0; i < nums.length; i++) {
    if (freq[i] == 0) {
      missingNum = i + 1;
    } else if (freq[i] == 2) {
      duplicateNum = i + 1;
    }
  }
  return [duplicateNum, missingNum];
};
