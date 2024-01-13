/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var minSteps = function (s, t) {
  let map = Array(27).fill(0);

  for (let i = 0; i < s.length; i++) {
    sOrd = s.charCodeAt(i) - "a".charCodeAt(0);
    tOrd = t.charCodeAt(i) - "a".charCodeAt(0);
    map[sOrd] += 1;
    map[tOrd] -= 1;
  }
  let ans = 0;
  for (let i of map) {
    ans += Math.max(i, 0);
  }
  return ans;
};

//Time Complexity: The algorithm iterates over characters of string s, which is O(n) time where n is the length of the string s. Then inside the for loop, the operaionts are constant time. So overall the time complexity is O(n).
//Space Complexity: Only data structure that is used is the array that we are storing the occurences of the characters. It has fixed length of 27. So the space complexity is O(1) which is constant space.
