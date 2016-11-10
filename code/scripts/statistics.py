import os

def count(fn):
    cars_box = 0
    peds_box = 0
    cycs_box = 0

    f = open(fn, 'r')
    for line in f:
        if line.strip().startswith('Car'):
            cars_box += 1
        elif line.strip().startswith('Pedestrian'):
            peds_box += 1
        elif line.strip().startswith('Cyclist'):
            cycs_box += 1
    f.close()
    return cars_box, peds_box, cycs_box

gt = '../../data/object/label_2/'
train_mask = '../../data/train.txt'
valid_mask = '../../data/valid.txt'

train = []
valid = []

f = open(train_mask, 'r')
for line in f:
    train.append(line.strip()[:-4])
f.close()

f = open(valid_mask, 'r')
for line in f:
    valid.append(line.strip()[:-4])
f.close()


tota_img = 0
cars_box = 0
peds_box = 0
cycs_box = 0


for f in os.listdir(gt):
    if f.endswith('.txt'):
        if f[:-4] not in valid:
            continue
        tota_img += 1
        ca, pe, cy = count(gt+f)
        cars_box += ca
        peds_box += pe
        cycs_box += cy

print 'total img %d' % tota_img
print 'total car box %d avg %f' % (cars_box, cars_box/float(tota_img))
print 'total pedestrian box %d avg %f' % (peds_box, peds_box/float(tota_img))
print 'total cyclists box %d avg %f' % (cycs_box, cycs_box/float(tota_img))

