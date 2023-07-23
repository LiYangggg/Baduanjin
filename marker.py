import os
import shutil
#技术原因只能设定绝对路径QAQ
path = "C:/Users/happy/Desktop/Joyce/AI作业/final/test_set"

pics = os.listdir(path)


while len(pics):
    pic = pics[:3000]
    pics = pics[3000:]
    des = os.path.join(path, "../temp")
    os.makedirs(des)
    for p in pic:
        shutil.copyfile(os.path.join(path,p),os.path.join(des,p))
    os.system(f'cd  C:\\Users\\happy\\desktop\\openpose && .\\bin\\OpenPoseDemo.exe --image_dir {des} --write_json C:/Users/happy/Desktop/Joyce/AI作业/final/test_set_marked')
    shutil.rmtree(des)