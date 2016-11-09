# 10-807 Team Project

## Commands
* git clone https://JinyiLu@github.com/JinyiLu/10807.git
* ./darknet yolo valid cfg/tiny-yolo.cfg tiny-yolo.weights
* ./darknet yolo valid cfg/yolo.cfg yolo.weights

## Evaluation
* g++ -O3 -DNDEBUG -o evaluate_object evaluate_object.cpp
* python yolo_to_eva.py ../../../data/yolo/results_Nov_4 ../../../data/yolo/results_Nov_4_eva_format
* ./evaluate_object 7481 FRCNN_Nov_8_rf
* python cal_ap.py ../../../results/yolo_Nov_4_rf/plot

## Yolo
* Nov_4: directly use provided model to make prediction on the whole training set, [result](results/yolo_Nov_4_rf/plot/)

## Faster-RCNN
* [Install on AWS](InstallFRCNN.md)
* Nov_8: directly use provided model
    * ~ 57 min for 7481 images (prediction) on g2.2xlarge
    * [result](results/FRCNN_Nov_8_rf/plot/)


## References
* [KITTI](http://www.cvlibs.net/datasets/kitti/eval_object.php)
* [Object Detection](https://www.zhihu.com/question/34223049/answer/110071873)
* [Yolo](http://pjreddie.com/darknet/yolo/)
* [How to use Yolo](http://blog.csdn.net/samylee/article/details/51729729)
* [Faster-RCNN](https://github.com/rbgirshick/py-faster-rcnn)
* [How to use Faster-RCNN](http://www.itdadao.com/articles/c15a253094p0.html)
* [PASCAL VOC2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/htmldoc/devkit_doc.html#SECTION00050000000000000000)
* [Bittiger Competition](https://www.bittiger.io/competition)
* [CUDA](https://developer.nvidia.com/cuda-downloads)
* [CUDA 7.5](https://developer.nvidia.com/cuda-75-downloads-archive)
* [Caffe](http://caffe.berkeleyvision.org/install_apt.html)