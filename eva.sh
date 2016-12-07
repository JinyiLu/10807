# ./evaluate_object 2 yolo_Nov_4_rf
# ./evaluate_object 2 yolo_Nov_9_rf
# ./evaluate_object 2 yolo_Dec_7_rf

# python code/scripts/eva/cal_ap.py results/yolo_Nov_4_rf/plot_valid_30
# python code/scripts/eva/cal_ap.py results/yolo_Nov_9_rf/plot_valid_30
# python code/scripts/eva/cal_ap.py results/yolo_Dec_7_rf/plot_valid_30

# ./evaluate_object 2 FRCNN_Nov_8_rf
# python code/scripts/eva/cal_ap.py results/FRCNN_Nov_8_rf/plot_valid_30

# ./evaluate_object 2 FRCNN_Dec_7_tiny
# python code/scripts/eva/cal_ap.py results/FRCNN_Dec_7_tiny/plot_valid_30

./evaluate_object 2 FRCNN_Dec_7_mid
python code/scripts/eva/cal_ap.py results/FRCNN_Dec_7_mid/plot_valid_30

