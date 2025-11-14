import time
try:
    from .fibonacci import fib_recursive_memo, fib_iterative
except ImportError:
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from fibonacci import fib_recursive_memo, fib_iterative


def ms(seconds):
    return seconds * 1000.0


def time_call(fn, n, trials=5):
    fn(n)  # warm-up
    total = 0.0
    for _ in range(trials):
        start = time.perf_counter()
        fn(n)
        end = time.perf_counter()
        total += (end - start)
    return ms(total / trials)


def run():
    ns = [30, 40, 50]
    header = "Python Fibonacci Benchmarks\nmethod\tn=30\tn=40\tn=50 (ms)"
    lines = [header]
    for name, fn in [("recursive_memo", fib_recursive_memo), ("iterative", fib_iterative)]:
        row = [name]
        for n in ns:
            if fib_iterative(n) != fib_recursive_memo(n):
                raise RuntimeError("mismatch between implementations")
            row.append(f"{time_call(fn, n):.3f}")
        lines.append("\t".join(row))
    output = "\n".join(lines)
    print(output)
    try:
        with open("python_bench.txt", "w", encoding="utf-8") as f:
            f.write(output + "\n")
    except Exception:
        pass


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        try:
            with open("python_bench.txt", "w", encoding="utf-8") as f:
                f.write(str(e) + "\n")
        except Exception:
            pass
        raise