class MyHashSet:

    def __init__(self):
        self.numbers = [False] * ((10**6)+1)

    def add(self, key: int) -> None:
        self.numbers[key] = True

    def remove(self, key: int) -> None:
        self.numbers[key] = False

    def contains(self, key: int) -> bool:
        if self.numbers[key]:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)