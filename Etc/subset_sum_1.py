from itertools import chain, combinations

MAX_COMBO = 5


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(MAX_COMBO+1))


nums = [1257605320,
395900000,
339980000,
100700,
74611800,
58850000,
58447840,
49972450,
33812320,
33160800,
32450000,
15537200,
30800000,
29403000,
28976730,
13750000,
27500000,
13717000,
26180000,
25135820,
25085080,
25000000,
2013000,
23199000,
24144000,
360000,
22593310,
22593310,
20102800,
20000000,
32560000,
7598800,
17186400,
7348000,
16311450,
774000,
15855300,
15400000,
15254800,
2271540,
14584240,
14500000,
14500000,
14179000,
6209280,
7260000,
13287000,
13000000,
12977390,
5655100,
12530000,
10200960,
4840000,
9800000,
9783400,
9757000,
9735000,
433660,
9600000,
154000,
9333280,
176000,
220000,
225000,
8119070,
8000000,
242000,
360000,
380000,
385000,
7131150,
440000,
440000,
880000,
6864000,
1216000,
1220000,
6470000,
1588000,
1654400,
1760000,
5602300,
5412000,
1781000,
4991800,
1815000,
2453000,
2508000,
4680000,
2805000,
3365000,
4400000,
3557000,
4345000,
4202000,
3780000,
4079760,
3960000,
3952000,
3830000,
4131600,
2130000,
4389000,
3520000,
3480000,
4505000,
3300000,
3300000,
3000000,
2871000,
2871000,
2856660,
4620000,
2690210,
2640000,
4700000,
4966500,
5310000,
2226400,
6248000,
2050400,
2030900,
6600000,
1921700,
1819540,
27314980,
1811950,
6647300,
7670300,
1709760,
1700000,
6930000,
3937500,
1320000,
1301360,
1300000,
1297000,
1265000,
6982500,
6997100,
1210000,
1091550,
1073600,
990000,
905000,
8600000,
880000,
8690000,
720000,
706200,
600000,
9176200,
9570000,
9676700,
390720,
389400,
9939600,
12540000,
14652000,
16997600,
249560,
246800,
243000,
17864000,
19033300,
24400000,
24950000,
27996100,
150480,
104280,
82500000]

inputSum = 149425100

nums_filter = set([n for n in nums if n <= inputSum])
print("nums : {}, filtered : {}".format(len(nums), len(nums_filter)))
for i, combo in enumerate(powerset(nums_filter), 1):
    sum = 0
    for num in combo:
        sum += int(num)
    if sum == inputSum:
        print(combo)