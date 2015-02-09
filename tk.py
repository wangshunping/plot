from Tkinter import *
import tkMessageBox
from matplotlib.colors import LogNorm
import pylab
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        Label(self,text="We do crosstalk right. ",font=("Helvetica",20,'bold italic')).grid(row=2,column=1)
 
         #text
        #Label(self,text="Input your Intensity file: ", font=("Arial", 12)).grid(row=3)
        Label(self,text="Input your Intensity file: ", font=("Arial", 12)).grid(row=3,sticky=W)

         # input 
        self.nameInput = Entry(self,width=70,insertofftime=500,relief='sunken')
        self.nameInput.grid(row=3,column=1,columnspan=2)

        Label(self,text="-"*100).grid(row=4,column=0,columnspan=3)
        Label(self,text="Choose a mode to plot:").grid(row=5,column=0,sticky=N)
        Label(self,text="-"*100).grid(row=6,column=0,columnspan=3)

        self.model = IntVar()
        self.model.set('1')
        print self.model.get()
        Radiobutton(self,variable=self.model,text='Four Channel',indicatoron =0,relief='sunken',value=1).grid(row=7,column=0)
        Radiobutton(self,variable=self.model,text='AC Channel',indicatoron =0,relief='sunken',value=2).grid(row=7,column=1)
        Radiobutton(self,variable=self.model,text='GT Channel',indicatoron =0,relief='sunken',value=3).grid(row=7,column=2)

        Label(self,text="-"*100).grid(row=8,column=0,columnspan=3)

        self.alertButton = Button(self, text='plot',font=('Arial',15,'bold'), command=self.plot)
        self.alertButton.grid(row =9,column=2 )
        
        Label(self,text="Version 0.9",font=("Arial",10)).grid(row=11,column=2,sticky=SE)
        Label(self,text="BaseCalling & ImageAnalysis Team",font=("Arial",10)).grid(row=10,column=2,sticky=SE)


    def plot(self):
        self.inputFile = self.nameInput.get() or 'nice.txt'
        try:
            open(self.inputFile)
        except:
            tkMessageBox.showinfo('Message','No such file!')
        self.inputFile = os.path.abspath(self.inputFile)
        mydir,file = os.path.split(self.inputFile)   
        outputFile = self.inputFile + ".png"
        self.baseInfoList,numChan = self.processFile()

        #self.plot2ChanCrossTalk(outputFile)
        #print self.model;
        if (numChan==4) & (self.model.get()==1):
            self.plot4ChanCrossTalk(outputFile)
        elif self.model.get()==2:
            self.plotACcrossTalk(outputFile)
        elif self.model.get()==3:
            self.plotGTcrossTalk(outputFile)
        else:
            tkMessageBox.showinfo('Message', 'done, %s !' % self.inputFile)    


    def processFile(self):
        totalList=[[],[],[],[]]
        #print len(totalList)
        inFile = open(self.inputFile)
        firstLine = inFile.readline()
        fisttmp = firstLine.strip().split()
        
        chan = len(fisttmp) 
        #print chan
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

    def plotACcrossTalk(self,outputFile):
        bases = "ACGT"
        #read a file
        plt.hist2d(self.baseInfoList[0], self.baseInfoList[1], bins=169,norm=LogNorm())
        plt.grid(True)

        plt.colorbar()
        plt.title('A C Crosstalk Plot',multialignment='left', fontsize=20,style='italic',weight=700)
        plt.savefig(outputFile,dpi=250)
        plt.show()

    def plotGTcrossTalk(self,outputFile):
        bases = "ACGT"
        #read a file
        plt.hist2d(self.baseInfoList[2], self.baseInfoList[3], bins=169,norm=LogNorm())
        plt.grid(True)

        plt.colorbar()
        plt.title('G T Crosstalk Plot',multialignment='left', fontsize=20,style='italic',weight=700)
        plt.savefig(outputFile,dpi=250)
        plt.show()

def main():
    app = Application()
    app.master.title('Plot CrossTalk... V0.9')
    app.master.geometry('680x280') 
    app.mainloop()

if __name__ =="__main__":
    main()
