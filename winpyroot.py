# This library is written by A.M.M. Elsayed for Windows PyROOT.
# add path to your installed root\bin file on windows.
import sys
root_path=r'C:/root/bin' 
sys.path.append(root_path) # adding ROOT to python library paths
import ROOT as R 


#-----------------------------------------------#
#                     PLOTS                     #
#-----------------------------------------------#

# function: Just write the function u want plot in string format, ex sin(x)/x or x^2
# x_: A 2 list x_ = [x_min, x/_max], the domain of your plot
# titles: titles=[title of your plot, title of x axixs, title of y axis]

class Plot():

	def __init__(self,function,x_,titles=[]):
		self.function=function
		self.x_=x_
		self.titles=titles

	def PyROOT_Code(self):
		return R.TF1("res",self.function,float(self.x_[0]),float(self.x_[1]))

	def setting_titles(self,res):
		if len(self.titles)==1:
			res.SetTitle(self.titles[0])
		elif len(self.titles)==2:
			res.SetTitle(self.titles[0])
			res.GetXaxis().SetTitle(self.titles[1])
		elif len(self.titles)==3:
			res.SetTitle(self.titles[0])
			res.GetXaxis().SetTitle(self.titles[1])
			res.GetYaxis().SetTitle(self.titles[2])
		else:
			pass

	def Draw(self):
		res= self.PyROOT_Code()		
		self.setting_titles(res)
		# Creating canavas.
		# The following codes are repsonsible for opening a canvas stably
		# with PyROOT in python. 
		canvas = R.TCanvas()
		res.Draw()
		R.gApplication.Run()

		# One can actually save from GUI opened by .Draw()
	def Save(self,filename):
		res= self.PyROOT_Code()		
		self.setting_titles(res)
		canvas = R.TCanvas()
		res.Draw()
		canvas.Print(filename)
		canvas.Close()


#-----------------------------------------------#
#                 Histogram                     #
#-----------------------------------------------#

class Histogram():
	pass


