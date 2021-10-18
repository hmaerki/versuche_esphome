
# Some examples of difficult to read yaml literals

While studing the source of pyyaml, I constructed some difficult to read literals.

The 'source code under test' is the method `construct_yaml_int()` in https://github.com/yaml/pyyaml/blob/master/lib/yaml/constructor.py

example|yaml
--|:--:
a|`1`
b|`-1`
c|`1.0`
d|`-1.0`
e|`0xA`
f|`-0xA`
g|`-0XA`
h|`yes`
i|`no`
j|`NO`
k|`-05_5:7.6`
l|`-0x5_5:7.6`
m|`0x5_5:7.6`
n|`0x57`
o|`1:2:3:4`
p|`-1:2:3:4`
q|`-01:2:3:4`
r|`0xA01`
s|`0XA01`
t|`0xA_01`
u|`{ 1 : 2 }`
v|`{ 1 : 2}`
w|`{ 1_ : 2}`
x|`{ _1 : 2}`
y|`{ 1 :2}`
aa|`{ 1: 2}`
ab|`{ 1:2}`
ac|`{1:2}`
