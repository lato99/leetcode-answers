/**
 * @param {number} n
 * @return {number}
 */
var countVowelPermutation = function (n) {
  let a = 1n,
    e = 1n,
    i = 1n,
    o = 1n,
    u = 1n;
  var mod = BigInt(Math.pow(10, 9) + 7);
  for (var _ = 1; _ < n; _++) {
    let new_a = 0n,
      new_e = 0n,
      new_i = 0n,
      new_o = 0n,
      new_u = 0n;
    new_a = e;
    new_e = (a + i) % mod;
    new_i = (a + e + o + u) % mod;
    new_o = (i + u) % mod;
    new_u = a;
    (a = new_a), (e = new_e), (i = new_i), (o = new_o), (u = new_u);
  }
  return (a + e + i + o + u) % mod;
};
