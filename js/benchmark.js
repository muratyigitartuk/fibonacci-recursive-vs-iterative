'use strict'

const { fibRecursiveMemo, fibIterative } = require('./fibonacci.js')

function msFromNs(ns) {
  return Number(ns) / 1e6
}

function timeCall(fn, n, trials = 5) {
  fn(n)
  let totalNs = 0n
  for (let i = 0; i < trials; i++) {
    const start = process.hrtime.bigint()
    fn(n)
    const end = process.hrtime.bigint()
    totalNs += end - start
  }
  const avgNs = totalNs / BigInt(trials)
  return msFromNs(avgNs)
}

function run() {
  const ns = [30, 40, 50]
  console.log('Node.js Fibonacci Benchmarks')
  console.log('method\tn=30\tn=40\tn=50 (ms)')
  for (const [name, fn] of [['recursive_memo', fibRecursiveMemo], ['iterative', fibIterative]]) {
    const row = [name]
    for (const n of ns) {
      if (fibIterative(n) !== fibRecursiveMemo(n)) throw new Error('mismatch between implementations')
      row.push(timeCall(fn, n).toFixed(3))
    }
    console.log(row.join('\t'))
  }
}

run()