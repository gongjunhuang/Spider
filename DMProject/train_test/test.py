def mcnuggets(n):
    """ Determine if it's possible to buy exactly n McNuggets with packages
        of 6, 9 and 20 McNuggets.

        The solution is a Diophantine equation with 3 variables (ax+by+cz=n).
        Calculate z=(n-ax-by)/c for all x,y. The time complexity is O(n^2).
    """
    packs = {'6': 0, '9': 0, '20': 0}
    r1 = n // 6 + 1
    r2 = n // 9 + 1
    for x in range(r1):
        for y in range(r2):
            z, remainder = divmod(n - 6 * x - 9 * y, 20)
            if remainder > 0 or z < 0:
                continue
            else:
                #return {'6': x, '9': y, '20': z}
                return True
    return False


numbers = [50, 51, 52, 53, 54, 55, 7]

for n in numbers:
    print(n, mcnuggets(n))