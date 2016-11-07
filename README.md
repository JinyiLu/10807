# 10-807 Team Project

## Commands
* git clone https://JinyiLu@github.com/JinyiLu/10807.git
* ./darknet yolo valid cfg/tiny-yolo.cfg tiny-yolo.weights
* ./darknet yolo valid cfg/yolo.cfg yolo.weights
* python yolo_toeva.py ../../../data/yolo/results_Nov_4 ../../../data/yolo/results_Nov_4_eva_format
* g++ -O3 -DNDEBUG -o evaluate_object evaluate_object.cpp

## Yolo
* Nov_4: directly use provided model to make prediction on the whole training set

## References
* [Object Detection](https://www.zhihu.com/question/34223049/answer/110071873)
* http://blog.csdn.net/samylee/article/details/51729729
* [Yolo](http://pjreddie.com/darknet/yolo/)
* [PASCAL VOC2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/htmldoc/devkit_doc.html#SECTION00050000000000000000)
* https://www.bittiger.io/competition
* [KITTI](http://www.cvlibs.net/datasets/kitti/eval_object.php)