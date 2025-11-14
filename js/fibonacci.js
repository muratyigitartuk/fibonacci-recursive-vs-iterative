'use strict'

function fibRecursiveMemo(n, memo) {
  if (typeof n !== 'number' || !Number.isInteger(n)) throw new TypeError('n must be an integer')
  if (n < 0) throw new RangeError('n must be non-negative')
  if (!memo) memo = {}
  if (memo[n] !== undefined) return memo[n]
  if (n < 2) {
    memo[n] = n
    return n
  }
  const result = fibRecursiveMemo(n - 1, memo) + fibRecursiveMemo(n - 2, memo)
  memo[n] = result
  return result
}

function fibIterative(n) {
  if (typeof n !== 'number' || !Number.isInteger(n)) throw new TypeError('n must be an integer')
  if (n < 0) throw new RangeError('n must be non-negative')
  let a = 0, b = 1
  for (let i = 0; i < n; i++) {
    const t = a
    a = b
    b = t + b
  }
  return a
}

module.exports = { fibRecursiveMemo, fibIterative }