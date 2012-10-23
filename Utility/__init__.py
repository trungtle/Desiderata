import os
import sys

def GetRoot(up):
	root_dir = os.path.abspath(__file__)

	for level in range(up):
		root_dir, dir_name = os.path.split(root_dir)

	root_dir += "/"
	return root_dir


# ==============================================================================
UTILITY_ROOT_DIR = GetRoot(2)