# Install Faster R-CNN on AWS

## 
* CUDA 7.5
* cuDNN
* Caffe
* openCV

## Commands
~~~~
sudo apt-get update
sudo apt-get upgrade
wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-command-line-tools-7-5_7.5-18_amd64.deb

# cuda 7.5
wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_7.5-18_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1404_7.5-18_amd64.deb

# driver
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y opencl-headers build-essential protobuf-compiler \
    libprotoc-dev libboost-all-dev libleveldb-dev hdf5-tools libhdf5-serial-dev \
    libopencv-core-dev  libopencv-highgui-dev libsnappy-dev libsnappy1 \
    libatlas-base-dev cmake libstdc++6-4.8-dbg libgoogle-glog0 libgoogle-glog-dev \
    libgflags-dev liblmdb-dev git python-pip gfortran

sudo apt-get install -y linux-image-extra-`uname -r` linux-headers-`uname -r` linux-image-`uname -r`

# install cuda 7.5
sudo apt-get install -y cuda
sudo apt-get clean

# install cudnn 4
tar -xvf cudnn-7.0-linux-x64-v4.0-prod.tgz
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo cp cuda/include/cudnn.h /usr/local/cuda/include

sudo sh -c "sudo echo '/usr/local/cuda/lib64' > /etc/ld.so.conf.d/cuda_hack.conf"
sudo ldconfig /usr/local/cuda/lib64

# caffe
git clone https://github.com/BVLC/caffe.git
cd caffe
cd python
for req in $(cat requirements.txt); do sudo pip install $req; done

# opencv
sudo apt-get install libopencv-dev python-opencv

# Faster-RCNN
pip install cython
sudo pip install easydict

git clone --recursive https://github.com/rbgirshick/py-faster-rcnn.git

cd $FRCN_ROOT/lib
make

cd $FRCN_ROOT/caffe-fast-rcnn
make all -j8
make pycaffe

make test -j8
make runtest

# 
ssh -X

# verify cuda
nvcc -V
nvidia-smi
~~~~



## References
* https://github.com/BVLC/caffe/wiki/Caffe-on-EC2-Ubuntu-14.04-Cuda-7
* https://developer.nvidia.com/cuda-75-downloads-archive
* https://developer.nvidia.com/rdp/cudnn-download
* https://github.com/rbgirshick/py-faster-rcnn
* https://github.com/rbgirshick/py-faster-rcnn/issues/129
* https://github.com/BVLC/caffe/issues/861
* https://github.com/rbgirshick/py-faster-rcnn/issues/237