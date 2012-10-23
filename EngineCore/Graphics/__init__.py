import os
import sys

UP_LEVEL = 3

def ImportPath():
	root_dir = os.path.abspath(__file__)
	for i in range(UP_LEVEL):
		root_dir, DIR_NAME = os.path.split(root_dir)
	root_dir += "/"
	sys.path.append(root_dir)
	return root_dir


# ==============================================================================
ROOT_DIR = ImportPath()