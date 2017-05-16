#!/usr/bin/python


class Values:
	plugin 		= ''
	interval	= ''
	plugin_instance 	= ''
	type 		= ''
	type_instance = ''
	values 		= ''

	def dispatch(self):
		pass
		#print "instance/type/type_instance: %s/%s/%s =  %s" % (self.plugin_instance, self.type, self.type_instance, self.values)
#		print ""

def info(self, arg=''):
	pass


def register_read(read_callback):
	pass
	
