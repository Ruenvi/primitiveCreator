import maya.cmds as cmds

def createPrimitive(slItem,name):
	slItem = slItem.text().lower()

	if slItem == "cube":
		cmds.polyCube(name = name)
		cmds.rename
	elif slItem == "sphere":
		cmds.polySphere(name = name)
	elif slItem == "cone":
		cmds.polyCone(name = name)
	elif slItem == "torus":
		cmds.polyTorus(name = name)

