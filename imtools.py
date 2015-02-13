import os
def get_imlist(path):
	'''
	return all *.jpg file
	'''
	return [os.path.join(path,f) for f in f.endswite('.jpg')]

