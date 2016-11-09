import sys

class PredResult:
    def __init__(self, line, category):
        sp = line.split()
        self.category = category
        self.img_name = sp[0].strip()
        self.thresh = sp[1].strip()
        self.x1 = sp[2].strip()
        self.y1 = sp[3].strip()
        self.x2 = sp[4].strip()
        self.y2 = sp[5].strip()
        self.alpha = 0.0

    def to_eva(self):
        trash = 0.0
        re = '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % \
        (self.category, trash, trash, self.alpha, self.x1, self.y1, \
            self.x2, self.y2, trash, trash, trash, trash, trash, trash, trash, self.thresh)
        return re


def load_from_file(f_name, category, results):
    f = open(f_name, 'r')
    for line in f:
        pred_re = PredResult(line, category)
        if pred_re.img_name in results:
            results[pred_re.img_name].append(pred_re)
        else:
            results[pred_re.img_name] = [pred_re]

def save_to_file(out_dir, results):
    for img_name in results:
        f = open(out_dir+'/'+img_name+'.txt', 'w')
        for pred_re in results[img_name]:
            f.write(pred_re.to_eva()+'\n')
        f.close()


if __name__ == "__main__":
    results = {}
    yolo_results_dir = sys.argv[1]
    out_dir = sys.argv[2]

    prefix = 'comp4_det_test_'

    # yolo_Nov_4
    # categories = {'car':yolo_results_dir+'/'+prefix+'car.txt',\
    # 'cyclist':yolo_results_dir+'/'+prefix+'bicycle.txt',\
    # 'pedestrian':yolo_results_dir+'/'+prefix+'person.txt'}

    # yolo_Nov_9
    categories = {'car':yolo_results_dir+'/'+prefix+'car.txt',\
    'pedestrian':yolo_results_dir+'/'+prefix+'pedestrian.txt'}

    for category in categories:
        load_from_file(categories[category], category, results)
    save_to_file(out_dir, results)

