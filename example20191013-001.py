import math
import numpy as np

for kkk in range(20):
    speed = kkk + 1
    print("当兔子速度为 %.2f m/s时: " % speed)
    SUM_S_X = 0
    SUM_S_Y = 0
    S_North = 20
    S_East = 33
    COUNT = 10000
    seg = (S_North / speed - 0) / (COUNT - 1)
    for iii in np.linspace(seg, S_North / speed, COUNT):
        s_x = S_East - SUM_S_X
        s_y = iii * speed - SUM_S_Y
        S_X = (2 * speed * seg) / math.sqrt(pow(s_x, 2) + pow(s_y, 2)) * s_x
        S_Y = (2 * speed * seg) / math.sqrt(pow(s_x, 2) + pow(s_y, 2)) * s_y
        SUM_S_X = SUM_S_X + S_X
        SUM_S_Y = SUM_S_Y + S_Y
        if SUM_S_X > S_East:
            print("  狼在第 %.2f 秒逮住兔子,坐标(0, %2.2f)!" % (iii, speed * iii))
            print("  狼    坐标(%.2f, %.2f)m!" % ((S_East - SUM_S_X), SUM_S_Y))
            break
        elif iii == (S_North / speed):
            distance = math.sqrt(pow(S_East - SUM_S_X, 2) + pow(S_North - SUM_S_Y, 2))
            print("  狼未逮住兔子,最终两者相距 %.2f m!" % distance)
            print("  狼    坐标(%.2f, %.2f)m!" % ((33 - SUM_S_X), SUM_S_Y))
            print("  兔子  坐标(0, 20)m!")








