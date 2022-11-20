import sys
import json
import numpy as np
import pytransform3d.transformations as pt
import pytransform3d.camera as pc
import pytransform3d.visualizer as pv


def plot_gt_traj():
    poses = np.array([[[ 9.95694757e-01, -2.07959767e-02, -9.03306156e-02,
            -3.08100194e-01,  3.78000000e+02],
            [ 2.50334200e-02,  9.98626173e-01,  4.60335426e-02,
            1.34677202e-01,  5.04000000e+02],
            [ 8.92492011e-02, -4.80966419e-02,  9.94847357e-01,
            3.98987606e-02,  4.07565796e+02]],

        [[ 9.99291956e-01, -7.34605221e-03, -3.69024836e-02,
            -1.49857640e-01,  3.78000000e+02],
            [ 9.01871826e-03,  9.98929679e-01,  4.53666672e-02,
            1.34402931e-01,  5.04000000e+02],
            [ 3.65297273e-02, -4.56673577e-02,  9.98288572e-01,
            2.90271230e-02,  4.07565796e+02]],

        [[ 9.99992430e-01,  5.53811842e-04,  3.87669704e-03,
            1.10932614e-03,  3.78000000e+02],
            [-6.65359898e-04,  9.99584019e-01,  2.88321339e-02,
            1.22465216e-01,  5.04000000e+02],
            [-3.85910762e-03, -2.88344938e-02,  9.99576807e-01,
            1.45299491e-02,  4.07565796e+02]],

        [[ 9.95121837e-01,  3.26247513e-03,  9.86003727e-02,
            2.13791743e-01,  3.78000000e+02],
            [-5.65946335e-03,  9.99695003e-01,  2.40402296e-02,
            1.07530132e-01,  5.04000000e+02],
            [-9.84918550e-02, -2.44809818e-02,  9.94836748e-01,
            5.52735757e-03,  4.07565796e+02]],

        [[ 9.93794203e-01,  3.32882162e-03,  1.11185275e-01,
            3.14100385e-01,  3.78000000e+02],
            [-4.52491082e-03,  9.99934554e-01,  1.05070220e-02,
            8.38216469e-02,  5.04000000e+02],
            [-1.11143008e-01, -1.09449206e-02,  9.93744135e-01,
            -2.34978367e-02,  4.07565796e+02]],

        [[ 9.94645715e-01,  8.94804858e-03,  1.02956727e-01,
            3.47974807e-01,  3.78000000e+02],
            [-1.03022866e-02,  9.99867141e-01,  1.26292361e-02,
            2.25741956e-02,  5.04000000e+02],
            [-1.02830037e-01, -1.36223035e-02,  9.94605660e-01,
            -1.90437604e-02,  4.07565796e+02]],

        [[ 9.98899639e-01,  3.61912092e-03,  4.67600860e-02,
            1.51978910e-01,  3.78000000e+02],
            [-4.29959036e-03,  9.99886215e-01,  1.44599928e-02,
            2.96725594e-02,  5.04000000e+02],
            [-4.67024259e-02, -1.46451304e-02,  9.98801470e-01,
            6.54883590e-03,  4.07565796e+02]],

        [[ 9.99122858e-01,  2.67302897e-03, -4.17907126e-02,
            -7.79116750e-02,  3.78000000e+02],
            [-1.88392960e-03,  9.99819398e-01,  1.89101603e-02,
            3.83969098e-02,  5.04000000e+02],
            [ 4.18337174e-02, -1.88148413e-02,  9.98947442e-01,
            3.05810161e-02,  4.07565796e+02]],

        [[ 9.93598342e-01, -1.27222924e-03, -1.12964295e-01,
            -2.57195860e-01,  3.78000000e+02],
            [ 3.29771708e-03,  9.99837101e-01,  1.77452900e-02,
            3.90271693e-02,  5.04000000e+02],
            [ 1.12923324e-01, -1.80042144e-02,  9.93440568e-01,
            3.40520963e-02,  4.07565796e+02]],

        [[ 9.86220539e-01, -1.10159069e-02, -1.65069014e-01,
            -3.99508268e-01,  3.78000000e+02],
            [ 1.37643581e-02,  9.99784827e-01,  1.55156665e-02,
            3.78884375e-02,  5.04000000e+02],
            [ 1.64862573e-01, -1.75739378e-02,  9.86159980e-01,
            2.39672493e-02,  4.07565796e+02]],

        [[ 9.88566041e-01, -5.09572309e-03, -1.50702775e-01,
            -3.94398272e-01,  3.78000000e+02],
            [ 4.23126388e-03,  9.99972701e-01, -6.05629152e-03,
            -4.74934354e-02,  5.04000000e+02],
            [ 1.50729507e-01,  5.34937996e-03,  9.88560557e-01,
            3.85743529e-02,  4.07565796e+02]],

        [[ 9.97936010e-01, -2.48011202e-04, -6.42169192e-02,
            -1.62820384e-01,  3.78000000e+02],
            [-5.01705508e-04,  9.99931872e-01, -1.16583640e-02,
            -2.91589275e-02,  5.04000000e+02],
            [ 6.42154366e-02,  1.16665196e-02,  9.97867882e-01,
            3.16228382e-02,  4.07565796e+02]],

        [[ 9.98254836e-01, -1.91860162e-02,  5.58507964e-02,
            3.40105742e-02,  3.78000000e+02],
            [ 1.84937585e-02,  9.99745965e-01,  1.28853424e-02,
            -3.49194668e-02,  5.04000000e+02],
            [-5.60838170e-02, -1.18299639e-02,  9.98355985e-01,
            1.29817249e-02,  4.07565796e+02]],

        [[ 9.94165659e-01, -1.88336540e-02,  1.06208138e-01,
            2.11927474e-01,  3.78000000e+02],
            [ 1.88398790e-02,  9.99822021e-01,  9.44754924e-04,
            -3.79892886e-02,  5.04000000e+02],
            [-1.06207028e-01,  1.06170587e-03,  9.94343460e-01,
            -1.46925086e-02,  4.07565796e+02]],

        [[ 9.89614606e-01, -6.39025262e-03,  1.43604517e-01,
            3.65317494e-01,  3.78000000e+02],
            [ 1.15867062e-02,  9.99306798e-01, -3.53787616e-02,
            -3.85587588e-02,  5.04000000e+02],
            [-1.43278882e-01,  3.66752408e-02,  9.89002585e-01,
            -4.87239771e-02,  4.07565796e+02]],

        [[ 9.88051951e-01, -9.97377560e-03,  1.53798297e-01,
            3.95541102e-01,  3.78000000e+02],
            [ 1.85640082e-02,  9.98340130e-01, -5.45193665e-02,
            -8.73730406e-02,  5.04000000e+02],
            [-1.52999237e-01,  5.67230731e-02,  9.86597061e-01,
            -5.61978184e-02,  4.07565796e+02]],

        [[ 9.96231794e-01, -4.92261164e-03,  8.65920857e-02,
            2.22623512e-01,  3.78000000e+02],
            [ 8.20677169e-03,  9.99258697e-01, -3.76118012e-02,
            -1.09828621e-01,  5.04000000e+02],
            [-8.63427371e-02,  3.81807089e-02,  9.95533645e-01,
            -3.14387307e-02,  4.07565796e+02]],

        [[ 9.99530077e-01,  2.12583654e-02, -2.20871028e-02,
            4.44915891e-03,  3.78000000e+02],
            [-2.18779054e-02,  9.99362886e-01, -2.81975307e-02,
            -1.10959604e-01,  5.04000000e+02],
            [ 2.14736052e-02,  2.86674965e-02,  9.99358356e-01,
            -1.50054935e-02,  4.07565796e+02]],

        [[ 9.95454133e-01,  1.21931117e-02, -9.44588929e-02,
            -1.83856085e-01,  3.78000000e+02],
            [-1.56902466e-02,  9.99215245e-01, -3.63690183e-02,
            -1.25571713e-01,  5.04000000e+02],
            [ 9.39413235e-02,  3.76857705e-02,  9.94864225e-01,
            -1.92486867e-02,  4.07565796e+02]],

        [[ 9.90170598e-01,  4.92434278e-02, -1.30910203e-01,
            -3.29176098e-01,  3.78000000e+02],
            [-5.46562076e-02,  9.97778833e-01, -3.80789191e-02,
            -1.28603607e-01,  5.04000000e+02],
            [ 1.28744304e-01,  4.48596776e-02,  9.90662694e-01,
            -3.94624844e-02,  4.07565796e+02]]], dtype=np.float32)


    poses = poses[:,:3,:4]

    transformation_matrices = np.empty((len(poses), 4, 4))
    for i, camera_pose in enumerate(poses):
        R = np.array(camera_pose[:3,:3])
        p = np.array(camera_pose[:,3])
        transformation_matrices[i] = pt.transform_from(R=R, p=p)


    fig = pv.figure()
    #fig.plot_mesh(mesh_filename)
    for pose in transformation_matrices:
        fig.plot_transform(A2B=pose, s=0.1)
        #fig.plot_camera(M=M, cam2world=pose, virtual_image_distance=0.1, sensor_size=sensor_size)
    fig.show()

def plot_novel_traj():

    c2w = np.array([[ 1.0000000e+00,  0.0000000e+00,  0.0000000e+00,  1.4901161e-09, 3.7800000e+02],
                    [ 0.0000000e+00,  1.0000000e+00, -1.8730975e-09, -9.6857544e-09, 5.0400000e+02],
                    [-0.0000000e+00,  1.8730975e-09,  1.0000000e+00,  0.0000000e+00, 4.0756580e+02]], dtype=np.float32)
    
    up = np.array([0.0000000e+00, 9.9999988e-01, 4.1797702e-04], dtype=np.float32)

    rads = np.array([0.39451256, 0.12918354, 0.04078128])
    focal = 4.306292964914568
    zdelta = 0.23999998569488526

    render_poses = render_path_spiral(c2w, up, rads, focal, zdelta, zrate=.5, rots=2, N=120)
    render_poses = np.array(render_poses).astype(np.float32)
    poses = render_poses[:,:3,:4] # Tcam2wld pose
    #poses = poses[:,:3,:4]

    transformation_matrices = np.empty((len(poses), 4, 4))
    for i, camera_pose in enumerate(poses):
        R = np.array(camera_pose[:3,:3])
        p = np.array(camera_pose[:,3])
        transformation_matrices[i] = pt.transform_from(R=R, p=p)


    fig = pv.figure()
    #fig.plot_mesh(mesh_filename)
    for pose in transformation_matrices:
        fig.plot_transform(A2B=pose, s=0.1)
        #fig.plot_camera(M=M, cam2world=pose, virtual_image_distance=0.1, sensor_size=sensor_size)
    fig.show()


def normalize(x):
    return x / np.linalg.norm(x)

def viewmatrix(z, up, pos):
    vec2 = normalize(z)
    vec1_avg = up
    vec0 = normalize(np.cross(vec1_avg, vec2))
    vec1 = normalize(np.cross(vec2, vec0))
    m = np.stack([vec0, vec1, vec2, pos], 1)
    return m

def render_path_spiral(c2w, up, rads, focal, zdelta, zrate, rots, N):
    render_poses = []
    rads = np.array(list(rads) + [1.])
    hwf = c2w[:,4:5]
    
    for theta in np.linspace(0., 2. * np.pi * rots, N+1)[:-1]:
        c = np.dot(c2w[:3,:4], np.array([np.cos(theta), -np.sin(theta), -np.sin(theta*zrate), 1.]) * rads) 
        z = normalize(c - np.dot(c2w[:3,:4], np.array([0,0,-focal, 1.])))
        render_poses.append(np.concatenate([viewmatrix(z, up, c), hwf], 1))
    return render_poses


plot_novel_traj()