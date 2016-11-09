# Evaluation

## Required Files
~~~~
code/
 ---scripts/
        ---eva/
            ---evaluate_object.cpp  // KITTI eval script
            ---yolo_to_eva.py       // yolo test result to KITTI format
            ---cal_ap.py            // calculate average precision
data/
 ---object/
       ---label_2/  // ground truth label for development set (7481)
 ---train.txt       // list of images for training (4953)
 ---valid.txt       // list of images for validation (2528)
results/
    ---yolo_Nov_4_rf/      
                  ---data/        // prediction results for development set (7481)
                  ---plot/        // eval results for development set (7481)
                  ---plot_train/  // eval results for training set (4953)
                  ---plot_valid/  // eval results for validation set (2528)
evaluate_object       // executable file
~~~~

## Commends
~~~~
# optional, recompile evaluate_object.cpp
g++ -O3 -DNDEBUG -o evaluate_object code/scripts/eva/evaluate_object.cpp

# reformat yolo output, if eval yolo models
python code/scripts/eva/yolo_to_eva.py YOLO_RAW_OUTPUT results/yolo_Nov_4_rf/data

# eval, 0 for development set, 1 for training set, 2 for validation set
./evaluate_object 1 yolo_Nov_4_rf

# calculate ap, ap result can be found at results/yolo_Nov_4_rf/plot_train/ap.txt
python code/scripts/eva/cal_ap.py results/yolo_Nov_4_rf/plot_train
~~~~