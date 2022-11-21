import cv2
import numpy as np 
import open3d as o3d

#depth = cv2.imread("/home/saimouli/Desktop/ML_class/NeRF_torch/logs/fern_test/renderonly_path_200000_disp/000.png")
img_cv2 = cv2.imread("/home/saimouli/Desktop/ML_class/NeRF_torch/logs/fern_test/renderonly_path_200000/000.png")

focal = 407.5658

H, W, _ = img_cv2.shape
intrinsic = o3d.camera.PinholeCameraIntrinsic(W,H,focal,focal,0.5*W,0.5*H)
img = o3d.io.read_image("/home/saimouli/Desktop/ML_class/NeRF_torch/logs/fern_test/renderonly_path_200000/000.png")
depth = o3d.io.read_image("/home/saimouli/Desktop/ML_class/NeRF_torch/logs/fern_test/renderonly_path_200000_disp/000.png")



rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(img, depth)
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, intrinsic)

np_colors = []
for row in range(0, H):
    for col in range(0, W):
        #np_colors.append(np.array([0,0,0]))
        np_colors.append(img_cv2[row][col]/255.0)

np_colors = np.array(np_colors)
print(np_colors.shape)
print(len(pcd.points))
pcd.colors = o3d.utility.Vector3dVector(np_colors)
o3d.visualization.draw_geometries([pcd])
