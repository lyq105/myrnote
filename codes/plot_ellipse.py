from pylab import figure
from matplotlib.patches import Ellipse
from numpy import loadtxt
from matplotlib.backends.backend_pdf import PdfPages

def plot_ellipse(datafilename, pdffilename):

	data = loadtxt(datafilename)
	ells = []
	for ell in data:
		coord = [ell[3],ell[4]]
		ellip = Ellipse(xy=coord,width= 2*ell[0],height = 2*ell[1], angle = (ell[2])*180/3.14159265)
		ells.append(ellip)
#ells = [Ellipse(xy=rand(2)*10, width=rand(), height=rand(), angle=rand()*360)
#        for i in xrange(NUM)]
	fig = figure()
	ax = fig.add_subplot(111, aspect='equal')
	ax.set_axis_off()
	ax.set_axis_bgcolor([1,1,1])
	for e in ells:
		ax.add_artist(e)
		e.set_clip_box(ax.bbox)
		e.set_alpha(1)
		#e.set_facecolor(rand(3))
		e.set_facecolor([1,1,1])
	
	ax.set_xlim(0.0, 0.2)
	ax.set_ylim(0.0, 0.2)

#show()
	pp = PdfPages(pdffilename)
	pp.savefig(fig)
	pp.close()

if __name__ == '__main__':
	plot_ellipse("elip1.txt","ell1.pdf")
