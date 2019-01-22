import sys
import os
import argparse
from shutil import copy2

# function to copy selected scans + extra data to a new directory
# input is the scan number corresponding to a pose

def select(scan_number):

    # name the paths as per the MPI-Faust training data directory structure
    path = os.getcwd() + "/Pose_" + str(scan_number)
    path_ground = path + "/ground_truth_vertices_" + str(scan_number) 
    path_registrations = path + "/registrations_" + str(scan_number)
    path_scans = path + "/scans_" + str(scan_number)

    # define access rights
    access_rights = 0o777

    # if directory does not exist
    if not os.path.isdir(path):
       
        # create the directories
        os.mkdir(path, access_rights)
        os.mkdir(path_ground, access_rights)
        os.mkdir(path_registrations, access_rights)
    #    os.mkdir(path_scans, access_rights)
    
    for i in range(0, 10):

        # copy the training data ground truth vertices
        # format = tr_gt_0[person][pose]
        src = "training/ground_truth_vertices/tr_gt_0" + str(i) + str(scan_number) + ".txt"
        dst = path_ground + "/tr_gt_0" + str(i) + str(scan_number) + ".txt"
        copy2(src, dst)

        # copy the registrations. ply only
        # format = tr_gt_0[person][pos].ply
        src = "training/registrations/tr_reg_0" + str(i) + str(scan_number) + ".ply"
        dst = path_registrations + "/tr_gt_0" + str(i) + str(scan_number) + ".ply"
        copy2(src, dst)

        """
        # copy the scans. ply only
        # format = tr_gt_0[person][pose].ply
        src = "training/scans/tr_gt_0" + str(i) + str(scan_number) + ".ply"
        dst = path_scans + "/tr_gt_0" + str(i) + str(scan_number)
        copy2(src, dst)       
        """
        
    return

#var = input("Enter an MPI-Faust pose number: ")
select(0)
