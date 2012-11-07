import os
import sys

def GetRoot(up):
	root_dir = os.path.abspath(__file__)

	for level in range(up):
		root_dir, dir_name = os.path.split(root_dir)

	root_dir += "/"
	return root_dir


# ==============================================================================
MVC_ROOT_DIR = GetRoot(2)
RESOURCE_DIR = MVC_ROOT_DIR + "GameSource/Resources/"
SOUND_DIR = RESOURCE_DIR + "Sounds/"
UBUNTU_FONT_DIR = RESOURCE_DIR + "ubuntu_font/"
CONFIG_DIR = MVC_ROOT_DIR + "Config/"

import json
with open(CONFIG_DIR + "config.json") as f:
	CONFIG = f.read()

CONFIG = json.loads(CONFIG)