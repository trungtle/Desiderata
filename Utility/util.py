from Utility import UTILITY_ROOT_DIR

def GetModel(name, instance):
	import json
	with open(UTILITY_ROOT_DIR + "/GameSource/MVC/Models/" + name + "Model.json") as f:
		data = f.read()		

	jsonData = json.loads(data)
	return {"name": name, "json": jsonData[instance] }