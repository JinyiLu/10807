
f = open('../../data/yolo/results_Dec_7/output_tiny.txt', 'r')

IOU1 = []
IOU2 = []
error = []

flag = True
for line in f:
    if line.startswith('Detection Avg IOU'):
        try:
            iou = line.split(',')[0].replace('Detection Avg IOU:', '').replace('Saving', '').strip()
            iou = float(iou)
        except:
            if 'Saving' in line:
                iou = 0.2852
            print line
        if flag:
            IOU1.append(iou)
            flag = False
        else:
            IOU2.append(iou)
            flag = True
    elif line[0].isdigit() and 'Layer' not in line and ':' in line:
        try:
            er = line.split(',')[0].split(':')[1].strip()
            er = float(er)
            error.append(er)
        except:
            print line
        
        i = 0

print len(IOU1)
print len(IOU2)
print len(error)



