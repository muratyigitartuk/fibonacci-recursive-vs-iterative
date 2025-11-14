## Overview
- Implement recursive (with memoization) and iterative Fibonacci in Python and JavaScript
- Benchmark execution time for `n = 30, 40, 50` and summarize results
- Explain time and space complexity for each approach
- Produce a professional README with a Mermaid diagram
- Add `.gitignore` (including `.trae\documents`) and a CI pipeline YAML
- Work through phased plan; at each phase create and complete a todo list; mark phase complete in `plan.md`

## Deliverables
- `python/fibonacci.py` (recursive with memoization, iterative)
- `python/benchmark.py` (timing for 30/40/50; prints table)
- `python/tests/test_fibonacci.py` (correctness tests)
- `js/fibonacci.js` (recursive with memoization, iterative; CommonJS to avoid extra config)
- `js/benchmark.js` (timing for 30/40/50; prints table)
- `js/tests/fibonacci.test.mjs` (Node built-in `node:test` correctness tests)
- `README.md` (detailed explanation, complexities, how to run; Mermaid diagram)
- `plan.md` (phases, per-phase todo lists; checkboxes to mark completion)
- `.gitignore` (Python/Node standard + `.trae\documents`)
- `.github/workflows/ci.yaml` (best-practice CI for Python and Node)

## Phases
### Phase 1: Setup & Scaffolding
- Create project structure, `.gitignore`, and initialize `plan.md` with phases and checkboxes
- No external dependencies; all standard libs only
- Define task list for this phase; complete tasks; mark phase complete in `plan.md`

### Phase 2: Core Implementations + Tests
- Implement Fibonacci functions in Python and JS:
  - Recursive with memoization (dictionary/object)
  - Iterative O(n) time, O(1) space
- Add minimal unit tests comparing both implementations on small n (e.g., 0..20)
- Define and complete phase todo list; mark phase complete

### Phase 3: Benchmarking
- Write benchmark scripts using high-resolution timers
  - Python: `time.perf_counter()`
  - Node: `process.hrtime.bigint()`
- Warm-up once per method; run multiple trials; report average in ms
- Benchmark `n = 30, 40, 50`; print formatted tables
- Define and complete phase todo list; mark phase complete

### Phase 4: Documentation
- Author `README.md` with:
  - Overview, how to run tests and benchmarks for both languages
  - Time/space complexity analysis: recursive naive vs memoized vs iterative
  - Sample benchmark outputs (from Phase 3) with a summary table
  - Mermaid flowchart showing approach selection and benchmarking pipeline
- Define and complete phase todo list; mark phase complete

### Phase 5: CI Pipeline
- Create `.github/workflows/ci.yaml` with best practices:
  - Triggers on `push` and `pull_request`
  - Jobs: `python` and `node`
    - Python job: setup Python 3.11, run unit tests, run benchmarks (non-blocking, ensure success)
    - Node job: setup Node 20, run `node --test` unit tests, run benchmarks
  - Upload benchmark logs as artifacts for visibility
- Define and complete phase todo list; mark phase complete

### Phase 6: Finalization
- Ensure all phase checkboxes in `plan.md` are marked complete
- Final quick pass for consistency and formatting

## Implementation Details
- Python
  - Functions: `fib_recursive_memo(n, memo=None)`, `fib_iterative(n)`
  - Input validation for non-negative integers
  - Tests via `unittest` (no third-party libs)
- JavaScript
  - Functions: `fibRecursiveMemo(n)`, `fibIterative(n)`
  - CommonJS (`module.exports` / `require`) to avoid `package.json` changes
  - Tests via built-in `node:test` on Node ≥18
- Code contains no comments per instruction; readability via clear naming and structure

## Complexity Explanation (to include in README)
- Naive recursive: time ~ O(φ^n) (commonly stated O(2^n)), space O(n)
- Recursive with memoization: time O(n), space O(n) (memo + call stack)
- Iterative: time O(n), space O(1)
- Note on closed-form (Binet’s): not used due to floating inaccuracies for large n

## Benchmarking Method
- Each method warmed once; then run 5 trials per n; average reported in ms
- Python uses `time.perf_counter()`; Node uses `process.hrtime.bigint()` converted to ms
- Output formatted per language as a table printed to stdout

## CI Pipeline Details
- OS: `ubuntu-latest`
- Python job
  - `actions/setup-python@v5` with `python-version: '3.11'`
  - Run `python -m unittest -v`
  - Run `python python/benchmark.py`; save outputs as artifact
- Node job
  - `actions/setup-node@v4` with `node-version: '20'`
  - Run `node --test js/tests/fibonacci.test.mjs`
  - Run `node js/benchmark.js`; save outputs as artifact
- Jobs run in parallel; both must pass

## Documentation
- README sections:
  - Introduction and goals
  - How to run (Python/JS tests & benchmarks)
  - Complexity analysis
  - Benchmark results (tables)
  - Mermaid diagram: flowchart of approach selection and benchmarking pipeline
  - Notes and limitations

## .gitignore
- Include common Python/Node ignores (e.g., `__pycache__/`, `.pytest_cache/`, `node_modules/`, `dist/`, `.DS_Store`)
- Explicitly add `.trae\documents` as requested

## Acceptance Criteria
- Both languages provide correct Fibonacci values for tested range
- Benchmarks print timings for 30/40/50 for memoized recursive and iterative
- README contains complexities, sample outputs, and Mermaid diagram
- CI runs and passes unit tests for both languages; benchmark outputs uploaded
- `plan.md` reflects phases and completion status

## Next Steps
- Upon approval, proceed to Phase 1 and create per-phase todo lists; implement and verify each phase; update `plan.md` accordingly