"""
1.JPEGImages文件夹:改名
2.Annotations文件夹:xml文件
(1)mat=>txt
(2)txt=>xml
3.ImageSets.Main文件夹:数据集分割成train,val,test: 1752,751,626 ok!
"""
"""
the third step!
"""
import os
import random
from to_Annotations import WPI_CLASSES, TXTPath

sample_split = ['test', 'trainval', 'train', 'val']
# 以下参数需根据文件路径修改
root_dir = r"C:\Users\zh99\Desktop\database\VOC2007"  # VOC根路径


def dataset_split(trainval_percent=0.8, train_percent=0.7):
    """
    数据集划分
    :param trainval_percent:
    :param train_percent:
    :return:
    """
    # 0.8trainval 0.2test
    xmlfilepath = root_dir + '/Annotations'
    txtsavepath = root_dir + '/ImageSets/Main'
    total_xml = os.listdir(xmlfilepath)

    num = len(total_xml)  # 3129
    list = range(num)
    tv = int(num * trainval_percent)  # 2503
    tr = int(tv * train_percent)  # 2503*0.7=1752
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)

    ftrainval = open(root_dir + '/ImageSets/Main/trainval.txt', 'w')
    ftest = open(root_dir + '/ImageSets/Main/test.txt', 'w')
    ftrain = open(root_dir + '/ImageSets/Main/train.txt', 'w')
    fval = open(root_dir + '/ImageSets/Main/val.txt', 'w')

    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftrain.write(name)
            else:
                fval.write(name)
        else:
            ftest.write(name)

    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()


def sample_describe(split='trainval', cls_id=0):
    """
    生成cls_split.txt
    :param split:
    :param cls: 类别
    :return:
    """
    describe_txt = open(root_dir + '/ImageSets/Main/%s_%s.txt' % (WPI_CLASSES[cls_id], split), 'w')
    split_txt = open(root_dir + '/ImageSets/Main/%s.txt' % split).read().splitlines()
    annotation_lines = open(os.path.join(TXTPath, 'annotation.txt')).read().splitlines()
    split_gts = {}  # name: ['ob1', 'ob2', ...] 选出对应split的图片信息
    for line in annotation_lines:
        gt = line.split(' ')
        key = gt[0]
        if key in split_txt:
            gt.pop(0)
            split_gts[key] = gt
    for name, bboxs in split_gts.items():
        sample = -1
        for bbox_id, bbox in enumerate(bboxs):
            bbox_cls = bboxs[bbox_id][-1]
            if int(bbox_cls) == cls_id:
                sample = 1
        describe_txt.write(name + ' ' + str(sample) + '\n')
    describe_txt.close()


def all_sample_describe():
    for split in sample_split:
        for cls_id, cls in enumerate(WPI_CLASSES):
            sample_describe(split=split, cls_id=cls_id)


if __name__ == '__main__':
    dataset_split()
    all_sample_describe()
