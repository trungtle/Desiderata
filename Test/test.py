import sys
import os

import __init__ as defs
import EngineCore.Diags.BLogger as logger

if __name__ == "__main__":
	logger.Init()
	print logger.IsEnable()