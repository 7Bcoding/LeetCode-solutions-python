class Solution:
    def breakfastNumber(self, staple, drinks, x):
        count = 0
        price_num = [0 for i in range(x + 1)]
        # 解法：哈希表(数组代替)
        # 1. 以空间换时间，首先遍历一次主食的哈希表，获取每种价格的主食food_price出现的
        # 数量，映射到表中，以price_num[food_price] += 1来统计
        # 2. 将主食哈希表中数值累加，计算小于主食价格i的staple的个数
        # 3. 然后用x-drink得到lt，在哈希表中获取小于等于主食价格lt对应的值，即为满足条件的
        # 组合数量，累加至count中即可

        for food_price in staple:
            if food_price < x:
                price_num[food_price] += 1

        for i in range(2, x):
            price_num[i] += price_num[i - 1]

        for drink in drinks:
            lt = x - drink
            if lt <= 0:
                continue
            count += price_num[lt]

        return count % (10 ** 9 + 7)
