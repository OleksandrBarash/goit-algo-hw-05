def caching_fibonacci():
    cache = {}  # Словник для кешування результатів

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]

        # Рекурсивне обчислення з кешуванням
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci