# This is a sample Python script.
import math

# Отсчеты ГТ-3
m_deg = [359,359,359,359,359,359,359,359]
m_min = [18,18,18,18,18,18,18,18]
m_sec = [25.3,23.2,19.1,15.9,11.0,8.3,11.4,11.5]
# Углы между зеркалом ГТ-3 и эталонным зеркалом, измеренные тахеометром
ang_deg = [269,269,269,269,269,269,269,269]
ang_min = [35,35,35,35,35,35,35,35]
ang_sec = [42.9,38.6,35.9,35.0,28.4,25.8,29.6,28.0]
# Значения азимута ГТ-3 по данным тахеометра
az_deg = [359,359,359,359,359,359,359,359]
az_min = [18,18,18,18,18,18,18,18]
az_sec = [18.7,15.0,10.9,10.6,4.3,0.8,5.5,5.1]
# Азимут эталонного зеркала
et = [89,42,34.8]

m_rad     = []
ang_rad   = []
az_rad    = []
popr_rad  = []
popr1_rad = []
# Перевод в радианы
for i in range(len(m_sec)): m_rad.append((m_deg[i] + m_min[i]/60 + m_sec[i]/3600)*math.pi/180)
for i in range(len(ang_sec)): ang_rad.append((ang_deg[i] + ang_min[i]/60 + ang_sec[i]/3600)*math.pi/180)
for i in range(len(az_sec)): az_rad.append((az_deg[i] + az_min[i]/60 + az_sec[i]/3600)*math.pi/180)
et_rad = (et[0] + et[1]/60 + et[2]/3600)*math.pi/180

# Поправки
# Расчитанные по измерениям угла тахеометром
for i in range(len(m_sec)): popr_rad.append((et_rad + ang_rad[i]) - m_rad[i])
# Расчитанные по измерениям азимута тахеометром
for i in range(len(m_sec)): popr1_rad.append(az_rad[i] - m_rad[i])

print('Поправки, рассчитанные по измерениям угла тахеометром: ')
for i in range(len(popr_rad)):
    p_deg = math.floor(abs(popr_rad[i])*180/math.pi)
    p_min = math.floor(((abs(popr_rad[i])*180/math.pi) - p_deg)*60)
    p_sec = ((((abs(popr_rad[i])*180/math.pi) - p_deg)*60 - p_min)*60)
    if (popr_rad[i] >= 0): print('  %3dг%2dм %2.2fс \n' % (p_deg, p_min, p_sec))
    else: print('  -%3dг%2dм %2.2fс \n' % (p_deg, p_min, p_sec))

print('Поправки, рассчитанные по измерениям азимута тахеометром ')
for i in range(len(popr1_rad)):
    p_deg = math.floor(abs(popr1_rad[i])*180/math.pi)
    p_min = math.floor(((abs(popr1_rad[i])*180/math.pi) - p_deg)*60)
    p_sec = ((((abs(popr1_rad[i])*180/math.pi) - p_deg)*60 - p_min)*60)
    if (popr1_rad[i] >= 0): print('  %3dг%2dм %2.2fс \n' % (p_deg, p_min, p_sec))
    else: print('  -%3dг%2dм %2.2fс \n' % (p_deg, p_min, p_sec))

# Расчет средней поправки
mean_popr  = sum(popr_rad)/len(popr_rad)
mean_popr1 = sum(popr1_rad)/len(popr1_rad)

# Расчет СКО
kvadr_razn = []
kvadr_razn1 = []

for i in range(len(popr_rad))  : kvadr_razn.append(math.pow((popr_rad[i] - mean_popr),2))
for i in range(len(popr1_rad)) : kvadr_razn1.append(math.pow((popr1_rad[i] - mean_popr1),2))

sko_popr  = math.pow(sum(kvadr_razn)/len(popr_rad),0.5) * (180/math.pi)*3600
sko_popr1 = math.pow(sum(kvadr_razn1)/len(popr1_rad),0.5) * (180/math.pi)*3600

p_deg = math.floor(abs(mean_popr) * 180 / math.pi)
p_min = math.floor(((abs(mean_popr) * 180 / math.pi) - p_deg) * 60)
p_sec = ((((abs(mean_popr) * 180 / math.pi) - p_deg) * 60 - p_min) * 60)
if (mean_popr >= 0): print('Средняя поправка по измерениям угла тахеометром =  %3dг%2dм %2.2fс \n' % (p_deg, p_min, p_sec))
else: print('Средняя поправка по измерениям угла тахеометром = -%3dг%2dм %2.2fс \n' % (p_deg, p_min, p_sec))
print('СКО по измерениям угла тахеометром = %2.2fс \n' % sko_popr)

p_deg = math.floor(abs(mean_popr1) * 180 / math.pi)
p_min = math.floor(((abs(mean_popr1) * 180 / math.pi) - p_deg) * 60)
p_sec = ((((abs(mean_popr1) * 180 / math.pi) - p_deg) * 60 - p_min) * 60)
if (mean_popr1 >= 0): print('Средняя поправка по измерениям азимута тахеометром =  %3dг%2dм %2.2fс \n' % (p_deg, p_min, p_sec))
else: print('Средняя поправка по измерениям азимута тахеометром = -%3dг%2dм %2.2fс \n' % (p_deg, p_min, p_sec))
print('СКО по измерениям азимута тахеометром = %2.2fс \n' % sko_popr1)