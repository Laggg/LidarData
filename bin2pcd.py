import numpy as np
import sys
import open3d as o3d


def bin_to_pcd(binFileName,folder_for_pcds):
    
    data = np.fromfile(binFileName)
    data = data.reshape((-1, 64, 2048, 4))
    print(data.shape)
    
    for i in range(data.shape[0]):
        np_scan = data[i].reshape(-1, 4)
        points_xyz = np_scan[:,:3]
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points_xyz)
        o3d.io.write_point_cloud(folder_for_pcds+'ts_{}.pcd'.format(i), pcd)
#===============================================================================
        
if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    bin_to_pcd(a,b)