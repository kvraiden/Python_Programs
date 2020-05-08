import math
UTC = 0
P_rotat = int(input())
Longi = float(input())
RTime = float(UTC+(P_rotat/360)*Longi)
float(RTime)
#math.modf(RTime)


NTime = ('%.2f' %RTime)

res = [int(ele) for ele in str(NTime) if ele.isdigit()]

h = res[0]
m = res[1:]

int(h)

m_str = [str(int) for int in m]
ma_str = "".join(m_str)
fi_str = int(ma_str)

min = fi_str


if min > h:
    angle = 5.5*(min)- 30*(h)
    print(angle)
if h > min:
    angle = 30*(h) - 5.5*(min)
    print(angle)







