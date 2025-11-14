import { test } from 'node:test'
import assert from 'node:assert'
import { createRequire } from 'node:module'

const require = createRequire(import.meta.url)
const { fibRecursiveMemo, fibIterative } = require('../fibonacci.js')

test('small values equality', () => {
  for (let n = 0; n <= 20; n++) {
    assert.strictEqual(fibIterative(n), fibRecursiveMemo(n))
  }
})

test('input validation', () => {
  assert.throws(() => fibIterative(-1))
  assert.throws(() => fibIterative(1.5))
  assert.throws(() => fibRecursiveMemo(-1))
  assert.throws(() => fibRecursiveMemo('10'))
})