for f in $1/*
do
  echo 'start ' $f
  ./darknet yolo test cfg/tiny-yolo.cfg tiny-yolo.weights $f
  echo 'end' $2/${f##*/}
  mv predictions.png $2/${f##*/}
done
