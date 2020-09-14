# WPI交通信号灯数据集格式转换成VOC2007

## 1.简述

初学交通信号灯目标检测时，总是苦于找不到合适的交通灯数据集。即使找到了数据集，也往往因为格式不同而无法直接使用。因为大部分目标检测代码都只支持VOC或COCO数据集格式，为了保证程序的正常运行，必须先将数据集格式转换成支持的格式。这也是我在初学目标检测时遇到的比较麻烦的问题之一。

本文将介绍如何通过python脚本将WPI数据集格式转换成VOC2007数据集格式。

## 2.WPI数据格式介绍

首先介绍一下WPI数据集的文件格式：

└─WPI
    ├─test
    │  ├─labels
    │  │      label1.mat
    │  │      label2.mat
    │  │      ...
    │  │      label17.mat
    │  │      readme.txt
    │  ├─seq1
    │  ├─seq2
    │  ├─...
    │  ├─seq17
    │          
    └─trainval
        ├─labels
        │      readme.txt
        │      label01.mat
        │      ...
        │      label07.mat
        ├─seq01
        ├─...
        └─seq07

WPI数据集由两个文件夹组成，分别为test和trainval文件夹，其内部格式是相同的。文件夹内均有标注文件和对应交通灯图片。

其中，标注文件放在labels文件夹内，以mat格式存储标注数据，可用MATLAB打开。关于标注数据各个值所代表的含义可查看readme.txt文件。图片文件放在seq文件夹内，label序号和图片所放的文件夹seq序号一一对应。

## 3.格式转换步骤

首先要先做一些准备工作。查看WPI文件夹，可以发现标注文件和图片文件命名并不一致。为了保持一致，需要做出相应修改：

1. 将labels内标注文件命名改为对应的seqX.mat；

2. 将trainval内序号从0X改为X.

   改好后，文件树结构应为：

   └─WPI
       ├─test
       │  ├─labels
       │  │      **seq1.mat**
       │  │      **seq2.mat**
       │  │      ...
       │  │      **seq17.ma**t
       │  │      readme.txt
       │  ├─seq1
       │  ├─seq2
       │  ├─...
       │  ├─seq17
       │          
       └─trainval
           ├─labels
           │      readme.txt
           │      **seq1.mat**
           │      ...
           │      **seq7.mat**
           ├─**seq1**
           ├─...
           └─**seq7**

3. test文件夹中有些图片并没有对应的标注文件，为了脚本需要，要将其无标注的图片删去.

准备工作做好之后就可以进行数据集格式的转换了。整个过程主要分为三步：

1. 将WPI内的图片重新命名并将其放入VOC2007内的JPEGImages文件夹内；
2. 将mat标注文件转换为VOC标注格式的XML文件，并放入VOC2007内的Annotations文件夹内；
3. 将数据集重新分割为test和trainval并生成对应txt文件，放入VOC2007内的ImageSets\Main文件夹内.
