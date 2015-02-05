from matplotlib.colors import LogNorm
from pylab import *
#import fileinput
import numpy as np
import matplotlib.pyplot as plt

def temp_processFile(inputFileName):
    totalList = []
    baseA = []
    baseC = []
    baseG = []
    baseT = []
    inFile = open(inputFileName)
    qwe = inFile.readline()

    for line in inFile:
        tmp = line.strip().split()
        [float(item) for item in tmp]
        baseA.append(float(tmp[0]))
        baseC.append(float(tmp[1]))
        baseG.append(float(tmp[2]))
        baseT.append(float(tmp[3]))
    nA = np.array(baseA)
    nC = np.array(baseC)
    nG = np.array(baseG)
    nT = np.array(baseT)
    totalList.append(nA)
    totalList.append(nC)
    totalList.append(nG)
    totalList.append(nT)
    return totalList

def processFile(inputFileName):
	totalList=[[],[],[],[]]
	print len(totalList)
	inFile = open(inputFileName)
	firstLine = inFile.readline()
	fisttmp = firstLine.strip().split()
	
	chan = len(fisttmp) 
	print chan
	for line in inFile:
		tmp = line.strip().split()
		for i in xrange(chan):
			totalList[i].append(float(tmp[i]))
	return totalList,chan

def plot4ChanCrossTalk(baseInfoList,outputFile):
	bases = "ACGT"
	fig, axarr = matplotlib.pyplot.subplots(nrows=2, ncols=3)#,sharex='col',sharey='row')	
	fig.subplots_adjust(left=0.03, bottom=0.05, right=0.88, top=0.80, wspace=0.18, hspace=0.18)
	num = 0

	'''	
	for f in xrange(len(baseInfoList)):
			temp.extend(baseInfoList[f]) 
	sortmp = sorted(temp)
	temp = sortmp[int(len(sortmp)*0.001):int(len(sortmp)*0.999)]
	maxi = max(temp)
	mini = min(temp)
	print maxi
	print mini
	'''
	maxi = max([max(baseInfoList[f]) for f in xrange(len(baseInfoList))])
	mini = min([min(baseInfoList[f]) for f in xrange(len(baseInfoList))])

	for i in xrange(4):
		for j in xrange(i+1,4):
			if(num>=3):
				m = 1;n=num-3
			else:
				m=0;n=num

			im = axarr[m,n].hist2d(baseInfoList[i], baseInfoList[j], bins=139,norm=LogNorm())
			num+=1
			axarr[m,n].set_title(bases[i] + bases[j])
			axarr[m,n].grid(True)
			axarr[m,n].axis([mini, maxi, mini, maxi])
			axarr[m,n].xaxis.get_label().set_size('xx-large')
			axarr[m,n].yaxis.get_label().set_size('xx-large')
			for label in axarr[m,n].xaxis.get_ticklabels():
				label.set_fontsize(5)
			for label in axarr[m,n].yaxis.get_ticklabels():
				label.set_fontsize(5) 
	
	cbar_ax = fig.add_axes([0.0001, 0.0001, 0.0001, 0.0001])
	H, xedges, yedges = np.histogram2d(baseInfoList[0], baseInfoList[1],bins=139)
	im =  imshow(H)
	cbar_ax = fig.add_axes([0.90, 0.05, 0.03, 0.8])
	fig.colorbar(im, cax=cbar_ax)
	#subplot_tool()
	xlabel('number')
	fig.suptitle('Pairwise Intensity Crosstalk Plot',multialignment='left',position=(0.45,0.95), fontsize=20,style='italic',weight=700)
	plt.savefig(outputFile,dpi=250)
	''
	plt.show()

def plit2ChanCrossTalk(baseInfoList,outputFile):
	bases = "ACGT"
	#read a file
	hist2d(baseInfoList[0], baseInfoList[1], bins=169,norm=LogNorm())
	grid(True)

	colorbar()
	plt.savefig(outputFile,dpi=250)
	plt.show()

def plotCrossTalk(inputFile,outputFile):
	
	#read a file
	baseInfoList,numChan = processFile(inputFile)

	if numChan==4:
		plot4ChanCrossTalk(baseInfoList,outputFile)
	elif numChan==2:
		plit2ChanCrossTalk(baseInfoList,outputFile)

	

	
	

def main():
	inFile = "brilliant.txt"
	outFile = "shit.png"
	plotCrossTalk(inFile,outFile)
	
if __name__=="__main__":
	main()
