from Tkinter import *
import tkMessageBox
from matplotlib.colors import LogNorm
#from pylab import *
import pylab
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        Label(self,text="we do crosstalk right. ",font=("Arial",20)).grid(row=1)
 
         #text
        Label(self,text="Input your Intensity file: ", font=("Arial", 12)).grid(row=3)
        Label(self,text="Input your Intensity file: ", font=("Arial", 12)).grid(row=3)

         # input 
        self.nameInput = Entry(self,width=50)
        self.nameInput.grid(row=3,column=2)
        
       

        self.alertButton = Button(self, text='begin_plot', command=self.plot)
        self.alertButton.grid(row =5 )
        

    def plot(self):
        self.inputFile = self.nameInput.get() or 'nice.txt'
        outputFile = "output.png"
        self.baseInfoList,numChan = self.processFile()

        #self.plot2ChanCrossTalk(outputFile)
        
        if numChan==4:
            self.plot4ChanCrossTalk(outputFile)
        elif numChan==2:
            self.plot2ChanCrossTalk(outputFile)

        tkMessageBox.showinfo('Message', 'done, %s !' % inputFile)    


    def processFile(self):
        totalList=[[],[],[],[]]
        print len(totalList)
        inFile = open(self.inputFile)
        firstLine = inFile.readline()
        fisttmp = firstLine.strip().split()
        
        chan = len(fisttmp) 
        print chan
        for line in inFile:
            tmp = line.strip().split()
            for i in xrange(chan):
                totalList[i].append(float(tmp[i]))
        return totalList,chan

    def plot4ChanCrossTalk(self,outputFile):
        bases = "ACGT"
        fig, axarr = matplotlib.pyplot.subplots(nrows=2, ncols=3)#,sharex='col',sharey='row')   
        fig.subplots_adjust(left=0.03, bottom=0.05, right=0.88, top=0.80, wspace=0.18, hspace=0.18)
        num = 0

        maxi = max([max(self.baseInfoList[f]) for f in xrange(len(self.baseInfoList))])
        mini = min([min(self.baseInfoList[f]) for f in xrange(len(self.baseInfoList))])

        for i in xrange(4):
            for j in xrange(i+1,4):
                if(num>=3):
                    m = 1;n=num-3
                else:
                    m=0;n=num

                im = axarr[m,n].hist2d(self.baseInfoList[i], self.baseInfoList[j], bins=139,norm=LogNorm())
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
        H, xedges, yedges = np.histogram2d(self.baseInfoList[0], self.baseInfoList[1],bins=139)
        im =  plt.imshow(H)
        cbar_ax = fig.add_axes([0.90, 0.05, 0.03, 0.8])
        fig.colorbar(im, cax=cbar_ax)
        #subplot_tool()
        plt.xlabel('number')
        fig.suptitle('Pairwise Intensity Crosstalk Plot',multialignment='left',position=(0.45,0.95), fontsize=20,style='italic',weight=700)
        plt.savefig(outputFile,dpi=250)
        ''
        plt.show()

    def plot2ChanCrossTalk(self,outputFile):
        bases = "ACGT"
        #read a file
        plt.hist2d(self.baseInfoList[0], self.baseInfoList[1], bins=169,norm=LogNorm())
        plt.grid(True)

        plt.colorbar()
        plt.savefig(outputFile,dpi=250)
        plt.show()


def main():
    app = Application()
    app.master.title('Plot CrossTalk...')
    app.master.geometry('600x800') 
    app.mainloop()

if __name__ =="__main__":
    main()