from androguard.core.bytecodes.apk import APK

def get_permissions(file):
	a = APK(file)
	return a.get_permissions()

def get_name(file):
	a = APK(filename)
	return a.package
