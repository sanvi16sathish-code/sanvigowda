import time

def quadratic_time(n):
    print(f"\nO(n²) for n={n}")
    start = time.perf_counter()
    for i in range(n):
        for j in range(n):
            pass  # Simulates a constant-time operation
    end = time.perf_counter()
    print(f"Time taken: {end - start} seconds")

quadratic_time(100)
quadratic_time(200)
quadratic_time(400)