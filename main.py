# This is a sample Python script.

import math

# отсчеты ГТ-3
m_deg = [359,359,359,359,359,359,359,359]
m_min = [18,18,18,18,18,18,18,18]
m_sec = [25.3,23.2,19.1,15.9,11.0,8.3,11.4,11.5]

# углы медду гт-3 и эталонным зеркалом
ang1 = [269,35,42.9]
ang2 = [269,35,38.6]
ang3 = [269,35,35.9]
ang4 = [269,35,35.0]
ang5 = [269,35,28.4]
ang6 = [269,35,25.8]
ang7 = [269,35,29.6]
ang8 = [269,35,28.0]
ang9 = [54,11,51]
#  Значения азимута гт -3 по данным тахеометра
az1 = [359,18,18.7]# [359,18,30.8]
az2 = [359,18,15.0]# [359,18,27.1]
az3 = [359,18,10.9]#[359,18,23.0]
az4 = [359,18,10.6]#[359,18,22.7]
az5 = [359,18,16.4]
az6 = [359,18,12.9]
az7 = [359,18,17.6]
az8 = [359,18,17.2]
az9 = [269,35,42.9]
# азимут эталонного зеркала
et =  [89,42,34.8] #   было  [89,42,46.9]

# Перевод в радианы
m1_rad = (m1[0] + m1[1]/60 + m1[2]/3600)*math.pi/180
m2_rad = (m2[0] + m2[1]/60 + m2[2]/3600)*math.pi/180
m3_rad = (m3[0] + m3[1]/60 + m3[2]/3600)*math.pi/180
m4_rad = (m4[0] + m4[1]/60 + m4[2]/3600)*math.pi/180
m5_rad = (m5[0] + m5[1]/60 + m5[2]/3600)*math.pi/180
m6_rad = (m6[0] + m6[1]/60 + m6[2]/3600)*math.pi/180
m7_rad = (m7[0] + m7[1]/60 + m7[2]/3600)*math.pi/180
m8_rad = (m8[0] + m8[1]/60 + m8[2]/3600)*math.pi/180
m9_rad = (m9[0] + m9[1]/60 + m9[2]/3600)*math.pi/180

ang1_rad = (ang1[0] + ang1[1]/60 + ang1[2]/3600)*math.pi/180
ang2_rad = (ang2[0] + ang2[1]/60 + ang2[2]/3600)*math.pi/180
ang3_rad = (ang3[0] + ang3[1]/60 + ang3[2]/3600)*math.pi/180
ang4_rad = (ang4[0] + ang4[1]/60 + ang4[2]/3600)*math.pi/180
ang5_rad = (ang5[0] + ang5[1]/60 + ang5[2]/3600)*math.pi/180
ang6_rad = (ang6[0] + ang6[1]/60 + ang6[2]/3600)*math.pi/180
ang7_rad = (ang7[0] + ang7[1]/60 + ang7[2]/3600)*math.pi/180
ang8_rad = (ang8[0] + ang8[1]/60 + ang8[2]/3600)*math.pi/180
ang9_rad = (ang9[0] + ang9[1]/60 + ang9[2]/3600)*math.pi/180

et_rad = (et[0] + et[1]/60 + et[2]/3600)*math.pi/180

#Поправки

p11_rad = (et_rad + ang1_rad) - m1_rad
p22_rad = (et_rad + ang2_rad) - m2_rad
p33_rad = (et_rad + ang3_rad) - m3_rad
p44_rad = (et_rad + ang4_rad) - m4_rad
p55_rad = (et_rad + ang5_rad) - m5_rad
p66_rad = (et_rad + ang6_rad) - m6_rad
p77_rad = (et_rad + ang7_rad) - m7_rad
p88_rad = (et_rad + ang8_rad) - m8_rad
p99_rad = (et_rad + ang9_rad) - m9_rad

p1_rad = abs(p11_rad)
p2_rad = abs(p22_rad)
p3_rad = abs(p33_rad)
p4_rad = abs(p44_rad)
p5_rad = abs(p55_rad)
p6_rad = abs(p66_rad)
p7_rad = abs(p77_rad)
p8_rad = abs(p88_rad)
p9_rad = abs(p99_rad)

p1_deg = math.floor(p1_rad*180/math.pi)
p1_min = math.floor(((p1_rad*180/math.pi) - p1_deg)*60)
p1_sec = ((((p1_rad*180/math.pi) - p1_deg)*60 - p1_min)*60)

if (p11_rad >= 0): print('  p1 = %3dг%2dм %2.2fс \n' % (p1_deg, p1_min, p1_sec))
else: print('  p1 = -%3dг%2dм %2.2fс \n' % (p1_deg, p1_min, p1_sec))

p2_deg = math.floor(p2_rad*180/math.pi)
p2_min = math.floor(((p2_rad*180/math.pi) - p2_deg)*60)
p2_sec = ((((p2_rad*180/math.pi) - p2_deg)*60 - p2_min)*60)

if (p22_rad >= 0): print('  p2 = %3dг%2dм %2.2fс \n' % (p2_deg, p2_min, p2_sec))
else: print('  p2 = -%3dг%2dм %2.2fс \n' % (p2_deg, p2_min, p2_sec))

p3_deg = math.floor(p3_rad*180/math.pi)
p3_min = math.floor(((p3_rad*180/math.pi) - p3_deg)*60)
p3_sec = ((((p3_rad*180/math.pi) - p3_deg)*60 - p3_min)*60)

if (p33_rad >= 0): print('  p3 = %3dг%2dм %2.2fс \n' % (p3_deg, p3_min, p3_sec))
else: print('  p3 = -%3dг%2dм %2.2fс \n' % (p3_deg, p3_min, p3_sec))

p4_deg = math.floor(p4_rad*180/math.pi)
p4_min = math.floor(((p4_rad*180/math.pi) - p4_deg)*60)
p4_sec = ((((p4_rad*180/math.pi) - p4_deg)*60 - p4_min)*60)

if (p44_rad >= 0): print('  p4 = %3dг%2dм %2.2fс \n' % (p4_deg, p4_min, p4_sec))
else: print('  p4 = -%3dг%2dм %2.2fс \n' % (p4_deg, p4_min, p4_sec))

p5_deg = math.floor(p5_rad*180/math.pi)
p5_min = math.floor(((p5_rad*180/math.pi) - p5_deg)*60)
p5_sec = ((((p5_rad*180/math.pi) - p5_deg)*60 - p5_min)*60)

if (p55_rad >= 0): print('  p5 = %3dг%2dм %2.2fс \n' % (p5_deg, p5_min, p5_sec))
else: print('  p5 = -%3dг%2dм %2.2fс \n' % (p5_deg, p5_min, p5_sec))

p6_deg = math.floor(p6_rad*180/math.pi)
p6_min = math.floor(((p6_rad*180/math.pi) - p6_deg)*60)
p6_sec = ((((p6_rad*180/math.pi) - p6_deg)*60 - p6_min)*60)

if (p66_rad >= 0): print('  p6 = %3dг%2dм %2.2fс \n' % (p6_deg, p6_min, p6_sec))
else: print('  p6 = -%3dг%2dм %2.2fс \n' % (p6_deg, p6_min, p6_sec))

p7_deg = math.floor(p7_rad*180/math.pi)
p7_min = math.floor(((p7_rad*180/math.pi) - p7_deg)*60)
p7_sec = ((((p7_rad*180/math.pi) - p7_deg)*60 - p7_min)*60)

if (p77_rad >= 0): print('  p7 = %3dг%2dм %2.2fс \n' % (p7_deg, p7_min, p7_sec))
else: print('  p7 = -%3dг%2dм %2.2fс \n' % (p7_deg, p7_min, p7_sec))

p8_deg = math.floor(p8_rad*180/math.pi)
p8_min = math.floor(((p8_rad*180/math.pi) - p8_deg)*60)
p8_sec = ((((p8_rad*180/math.pi) - p8_deg)*60 - p8_min)*60)

if (p88_rad >= 0): print('  p8 = %3dг%2dм %2.2fс \n' % (p8_deg, p8_min, p8_sec))
else: print('  p8 = -%3dг%2dм %2.2fс \n' % (p8_deg, p8_min, p8_sec))

p9_deg = math.floor(p9_rad*180/math.pi)
p9_min = math.floor(((p9_rad*180/math.pi) - p9_deg)*60)
p9_sec = ((((p9_rad*180/math.pi) - p9_deg)*60 - p9_min)*60)

if (p99_rad >= 0): print('  p9 = %3dг%2dм %2.2fс \n' % (p9_deg, p9_min, p9_sec))
else: print('  p9 = -%3dг%2dм %2.2fс \n' % (p9_deg, p9_min, p9_sec))

popr1 = [-7.6,-9.8,-8.4,-6.1,-7.8,-7.7,-7.0,-8.7]
popr2 = [5.5-12.1,3.9-12.1,3.9-12.1,6.8-12.1,5.4-12.1,4.6-12.1,6.2-12.1]
poprmean1 = sum(popr1)/len(popr1)
poprmean2 = sum(popr2)/len(popr2)
print(poprmean1)
print(poprmean2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
