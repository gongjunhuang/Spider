class HashTable(object):
    def __init__(self):
        # table 是用来存储数据的数组
        # 先让它有 10007 个格子好了
        # 上课的时候说过, 这个尺寸最好选素数
        # 这样可以得到更为合理的下标分布
        self.table_size = 10007
        self.table = [0] * self.table_size

    def __contains__(self, item):
        return self.has_key(item)

    def has_key(self, key):
        index = self._index(key)
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == key:
                    return True
        return False

    def _insert_at_index(self, index, key, value):
        v = self.table[index]
        data = [key, value]
        if isinstance(v, int):
            # 如果是第一次, 得到的是 int 0
            # 那么就插入一个 list 来存, 以后相同 key 的元素都放这里面
            # 注意我们把 key value 作为一个数组保存进去了, 这是因为
            # 会出现相同 hash 值的 key
            # 这时候就需要比较原始信息来找到相应的数据
            self.table[index] = [data]
        else:
            self.table[index].append(data)

    def add(self, key, value):
        index = self._index(key)
        self._insert_at_index(index, key, value)

    def get(self, key, default_value=None):
        index = self._index(key)
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == key:
                    return kv[1]
        return default_value

    def _index(self, key):
        return self._hash(key) % self.table_size

    def _hash(self, s):
        n = 1
        f = 1
        for i in s:
            n += ord(i) * f
            f *= 10
        return n

def test():
    import uuid
    names = [
        'gua',
        'xiao',
        'name',
        'web',
        'python',
    ]
    ht = HashTable()
    for key in names:
        value = uuid.uuid4()
        ht.add(key, value)
        print('add 元素', key, value)
    for key in names:
        v = ht.get(key)
        print('get 元素', key, v)
    print('魔法方法', 'gua' in ht)

if __name__ == '__main__':
    test()
