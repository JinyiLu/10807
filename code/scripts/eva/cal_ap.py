import os
import sys

def cal_ap(f_name):
    precision = []
    f = open(f_name, 'r')
    for line in f:
        sp = line.split()
        precision.append([float(sp[0]), float(sp[1]), float(sp[2]), float(sp[3])])
    ap = [0.0, 0.0, 0.0]
    for i in range(0, 41, 4):
        ap[0] += precision[i][1]
        ap[1] += precision[i][2]
        ap[2] += precision[i][3]
    return ap[0]/11.0, ap[1]/11.0, ap[2]/11.0

if __name__ == "__main__":
    f_out = open(sys.argv[1]+'/'+'ap.txt', 'w')

    for f in os.listdir(sys.argv[1]):
        if f.endswith('.txt') and f != 'ap.txt' :
            easy, mod, hard = cal_ap(sys.argv[1]+'/'+f)
            f_out.write('f %s\nEasy %f\tModerate %f\tHard %f\n' % (f, easy, mod, hard))
    f_out.close()