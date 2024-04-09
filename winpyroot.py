# This library is written by A.M.M. Elsayed for Windows PyROOT.


# add path to your installed root\bin file on windows.
import sys
root_path=r'C:/root/bin' 
sys.path.append(root_path) # adding ROOT to python library paths
import ROOT as R 


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

def Plot(function,x_,titles=[]):
	res =R.TF1("res",function,float(x_[0]),float(x_[1]))
	# setting titles
	if len(titles)==1:
		res.SetTitle(titles[0])
	elif len(titles)==2:
		res.SetTitle(titles[0])
		res.GetXaxis().SetTitle(titles[1])
	elif len(titles)==3:
		res.SetTitle(titles[0])
		res.GetXaxis().SetTitle(titles[1])
		res.GetYaxis().SetTitle(titles[2])
	else:
		pass
	# Creating canavas
	canvas = R.TCanvas()
	res.Draw()
	R.gApplication.Run()




def FuncHistogram(function,x_,):
	pass

#Can also fill with other functions;
#gaus, expo, landau, pol0,1..,10, chebyshev
def RandomHistrogram(type_,N_bins,x_,titles):
	res=R.TH1F(type_+" histogram",titles[0],N_bins,int(x_[0]),int(x_[1]))
	res.FillRandom(type_)

	#Creating canavas
	canvas = R.TCanvas()
	res.Draw()
	R.gApplication.Run()


def histogram(hist_name,hist_title,n_events,n_bins,x_min,x_max,mean=0,std_dev=1,type="Gaus"):
	import ROOT as R 
	hist = R.TH1F(hist_name, hist_title, n_bins, x_min, x_max)
	for i in range(n_events):  # Adjust the number of iterations for more/less data points
	  	value = R.gRandom.Gaus(mean, std_dev)  # Generate Gaussian random number with mean and std_dev
	  	hist.Fill(value)
	hist.GetXaxis().SetTitle("Random Value")
	hist.GetYaxis().SetTitle("Counts")
	pad = R.TPad("pad", "", 0, 0, 1, 1)
	filename = "histogram.png"
	pad.SaveAs(filename)














######### Open Saved Image #########
# In most cases pyroon canvas is unstable
# and closes directly after code run therefore
# it is nessascry to save image into disk and open it using Pillow;
#from PIL import Image
#Image.open(image_name).show()