
# Some examples of difficult to read yaml literals

While studing the source of pyyaml, I constructed some difficult to read literals.

The 'source code under test' is the method `construct_yaml_int()` in https://github.com/yaml/pyyaml/blob/master/lib/yaml/constructor.py

example|yaml|data|datatype
--|:--:|:--:|:--:
a|`1`|`1`|int
b|`-1`|`-1`|int
c|`1.0`|`1.0`|float
d|`-1.0`|`-1.0`|float
e|`0xA`|`10`|int
f|`-0xA`|`-10`|int
g|`-0XA`|`'-0XA'`|str
h|`yes`|`True`|bool
i|`no`|`False`|bool
j|`NO`|`False`|bool
k|`-05_5:7.6`|`-3307.6`|float
l|`-0x5_5:7.6`|`'-0x5_5:7.6'`|str
m|`0x5_5:7.6`|`'0x5_5:7.6'`|str
n|`0x57`|`87`|int
o|`1:2:3:4`|`223384`|int
p|`-1:2:3:4`|`-223384`|int
q|`-01:2:3:4`|`'-01:2:3:4'`|str
r|`0xA01`|`2561`|int
s|`0XA01`|`'0XA01'`|str
t|`0xA_01`|`2561`|int
u|`{ 1 : 2 }`|`{1: 2}`|int -> int
v|`{ 1 : 2}`|`{1: 2}`|int -> int
w|`{ 1_ : 2}`|`{1: 2}`|int -> int
x|`{ _1 : 2}`|`{'_1': 2}`|str -> int
y|`{ 1 :2}`|`{'1 :2': None}`|str -> NoneType
aa|`{ 1: 2}`|`{1: 2}`|int -> int
ab|`{ 1:2}`|`{62: None}`|int -> NoneType
ac|`{1:2}`|`{62: None}`|int -> NoneType
