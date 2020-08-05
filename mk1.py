def is_prime(n):
    if n < 2:
        return False

    if n in (2, 3):
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def is_prime(n):
    if n < 2:
        return False

    if n in (2, 3):
        return True

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True


class primes:
    def __init__(self):
        # self.next 代表下一个素数
        # 未开始计算前初始为 1
        self.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        # 从上一个素数之后开始寻找
        n = self.next + 1
        # 跳过所有不是素数的 n
        while not is_prime(n):
            n += 1
        # 将找到的下一个素数保存到 self.next
        self.next = n
        return self.next

    def __next__(self):
        # 从上一个素数之后开始寻找
        n = self.next + 1
        while True:
            # 测试每一个 n 是否素数
            # 如是则保存到 self.next 并返回
            # 否则继续测试下一个
            if is_prime(n):
                self.next = n
                return self.next
            else:
                n += 1


if __name__ == '__main__':
    from itertools import islice
    from datetime import datetime

    t1 = datetime.now()
    lst = list(islice(primes(), 0, 100000))
    t2 = datetime.now()
    print(f'Found {len(lst)} primes in {t2 - t1}')