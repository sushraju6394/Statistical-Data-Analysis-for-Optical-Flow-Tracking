# Statistical Data Analysis for Optical Flow Tracking
## Description
Optical flow algorithm is used to describe motion of person in an omnidirectional image. The exr files are analysed and channel information is extracted. The extracted channel information is used to draw a bounding box across the person and the centroid is calculated. Later all the centroids of various exr files are visualized using matplotlib.   
A similar analysis is carried out on various datasets like Virtual KITTI, Monkaa, Driving, FlyingChairs, HD1K, KITTI 2012, KITTI 2015, Middlebury, SceneNet RGB-D, Sintel, SplitSphere, UCL, Virtual KITTI 2. To analyse the data, the flow magnitude, flow angles, mean displacements, histogram of flow magnitude and flow angles are calculated. 
## Dataset
The references of the dataset is stored in [References_dataset.txt](https://github.com/sushraju6394/Statistical-Data-Analysis-for-Optical-Flow-Tracking/files/9924181/References_dataset.txt) file. 
## Installation
Jupyter, Python3, matplotlib
## Citation
```
@inproceedings{scheck2020learning,
  title={Learning from theodore: A synthetic omnidirectional top-view indoor dataset for deep transfer learning},
  author={Scheck, Tobias and Seidel, Roman and Hirtz, Gangolf},
  booktitle={Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision},
  pages={943--952},
  year={2020}
}

@inproceedings{seidel2021omniflow,
  title={OmniFlow: Human omnidirectional optical flow},
  author={Seidel, Roman and Apitzsch, Andr{\'e} and Hirtz, Gangolf},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={3678--3681},
  year={2021}
}
```





