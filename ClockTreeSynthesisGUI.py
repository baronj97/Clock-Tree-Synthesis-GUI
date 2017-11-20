#Author: Jacob Baron and Scott Lerner
#Developer's Notes: Below is a scripting software that parses .im files for Node Number, the Parent, the Buffer, the Left Child, and the Right Child (and etc.) and
#places the information into a singly linked-list.
import matplotlib
import pylab as plt
from tkinter import *
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.backend_bases import MouseEvent
from matplotlib.figure import Figure
class Node:
    def __init__(self, NodeNumber, Capacitance, Delay, LocationX, LocationY, OrigPermReg, PermReg, SubtreeCost, SlewConstant, Parent, Buf, Distance, LeftChild, RightChild):
        self.NodeNumber = NodeNumber
        self.Capacitance = Capacitance
        self.Delay = Delay
        self.LocationX = LocationX
        self.LocationY = LocationY
        self.OrigPermReg = OrigPermReg
        self.PermReg = PermReg
        self.SubtreeCost = SubtreeCost
        self.SlewConstant = SlewConstant
        self.Parent = Parent
        self.Buf = Buf
        self.Distance = Distance
        self.LeftChild = LeftChild
        self.RightChild = RightChild
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def AddNode(self, NodeNumber, Capacitance, Delay, LocationX, LocationY, OrigPermReg, PermReg, SubtreeCost, SlewConstant, Parent, Buf, Distance, LeftChild, RightChild):
        new_node = Node(NodeNumber, Capacitance, Delay, LocationX, LocationY, OrigPermReg, PermReg, SubtreeCost, SlewConstant, Parent, Buf, Distance, LeftChild, RightChild)

        if self.head == None:
            self.head = new_node

        if self.tail != None:
            self.tail.next = new_node

        self.tail = new_node

    def PrintList(self):
        node = self.head
        while node != None:
            print("Node Number: ", node.NodeNumber)
            print("Capacitance: ", node.Capacitance)
            print("Delay: ", node.Delay)
            print("Location X: ", node.LocationX)
            print("Location Y: ", node.LocationY)
            print("Original Permissible Region", node.OrigPermReg)
            print("Permissible Region", node.PermReg)
            print("Subtree Cost: ", node.SubtreeCost)
            print("Slew Constant: ", node.SlewConstant)
            print("Parent: ", node.Parent)
            print("Buffer: ", node.Buf)
            print("Distance: ", node.Distance)
            print("Left Child: ", node.LeftChild)
            print("Right Child: ", node.RightChild)
            print("----------------------------------------------------------------------------------------------------------------------")
            node = node.next

    def PrintNodeDetails(self, index):
        if(index > len(NodeNumbers)):
            print("This Node does not exist")
            return
        else:
            global catString
            node = self.head
            i = 0
            while (i< index):
                node = node.next
                i = i + 1
            if (i == index):
                numStr = "Node Number: " + str(node.NodeNumber) + "\n"
                capacStr = "Capacitance: " + str(node.Capacitance) + "\n"
                delayStr = "Delay: " + str(node.Delay) + "\n"
                locationxStr = "Location X: " + str(node.LocationX) + "\n"
                locationyStr = "Location Y: " + str(node.LocationY) + "\n"
                origPermRegStr = "Original Permissible Region: " + str(node.OrigPermReg) + "\n"
                permRegStr = "Permissible Region: " + str(node.PermReg) + "\n"
                subtreeCostStr = "Subtree Cost: " + str(node.SubtreeCost) + "\n"
                slewConstStr = "Slew Constant: " + str(node.SlewConstant) + "\n" 
                parentStr = "Parent: " + str(node.Parent) + "\n"
                bufferStr = "Buffer: " + str(node.Buf) + "\n"
                distanceStr = "Distance: " + str(node.Distance) + "\n"
                leftChildStr = "Left Child: " + str(node.LeftChild) + "\n"
                rightChildStr = "Right Child: " + str(node.RightChild) + "\n"
                space = "-------------------------------------------------------------------------------------" + "\n"
                catString = numStr + capacStr + delayStr + locationxStr + locationyStr + origPermRegStr + permRegStr + subtreeCostStr + slewConstStr + parentStr + bufferStr + distanceStr + leftChildStr + rightChildStr + space
                return catString

    def DeleteNode(self, index): 
        prev = None
        node = self.head
        i = 0

        while (node != None) and (i < index):
            prev = node
            node = node.next
            i = i + 1
        if prev == None:
            self.head = node.next
        else:
            prev.next = node.next

    def getSize(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.next
        return count

    def getNode(self, index):
        target = float(index)
        if(target > len(NodeNumbers)):
            print("This Node does not exist")
            return
        else:
            node = self.head
            i = 0
            while (i< target):
                node = node.next
                i = i + 1
            if (i == target):
                target = node
                return target
#################### Parsing Begins Here ########################

#You should change this variable!
filename = "cns01.im" #Declare the file name


List = LinkedList() #Establish the linked list

#Create lists for each field of the "Node." These lists are later used to add information into a linked list
NodeNumbers = list()
Capacitance = list()
Delay = list()
LocationX = list()
LocationY = list()
SubtreeCost = list()
SlewConst = list()
Buffers = list()
parents = list()
Distance = list()
LeftChild = list()
RightChild = list()
OrigPermReg = list()
PermReg = list()

f = open(filename, 'r')

#You should change this variable!
padding = 1107 #Change this variable based on how many nodes DO NOT HAVE 

for i in range(0,padding):
    LeftChild.append("None")
    RightChild.append("None")
    OrigPermReg.append("None")
    PermReg.append("None")
    Distance.append("None")



while True:
    text = f.readline()
    if 'Node number' in text:
        tempNodeNum = text.split("Node number ", 1 )[1]
        temp2NodeNum = tempNodeNum.split()[0]
        storedNumNode = int(temp2NodeNum)
        NodeNumbers.append(storedNumNode)
        tempCapac = tempNodeNum.split()[2]
        storedNumCapac = float(tempCapac)
        Capacitance.append(storedNumCapac)
    elif 'delay' in text:
        tempDelay = text.split("delay: ",1)[1]
        storedDelay = str(tempDelay)
        Delay.append(storedDelay)
    elif 'location' in text:
        tempLocationX = text.split("location: ",1)[1]
        temp2LocationX = tempLocationX.split()[0]
        storedNumX = float(temp2LocationX)
        LocationX.append(storedNumX)
        tempLocationY = tempLocationX.split()[1]
        storedNumY = float(tempLocationY)
        LocationY.append(storedNumY)
    elif 'parent:' in text:
        tempParent = text.split("parent: ",1)[1]
        temp2Parent = tempParent.split()[0]
        storedParent = int(temp2Parent)
        parents.append(storedParent)
    elif 'buf:' in text:
        tempBuf = text.split("buf: ",1)[1]
        temp2Buf = tempBuf.split()[0]
        storedBuf = int(temp2Buf)
        Buffers.append(storedBuf)
    elif 'orig permissible region:' in text:
        tempOrigPermReg = text.split("orig permissible region: ",1)[1]
        storedOrigPermReg = str(tempOrigPermReg)
        OrigPermReg.append(storedOrigPermReg)
    elif 'permissible region:' in text:
        tempPermReg = text.split("permissible region: ",1)[1]
        storedTempPermReg = str(tempPermReg)
        PermReg.append(storedTempPermReg)
    elif 'subtree cost:' in text:
        tempSubtreeCost = text.split("subtree cost: ",1)[1]
        temp2SubtreeCost = tempSubtreeCost.split()[0]
        storedSubTree = int(temp2SubtreeCost)
        SubtreeCost.append(storedSubTree)
    elif 'slew const:' in text:
        tempSlewConst = text.split("slew const: ",1)[1]
        temp2SlewConst = tempSlewConst.split()[0]
        storedSlewConst = float(temp2SlewConst)
        SlewConst.append(storedSlewConst)
    elif 'slew_const' in text:
        tempSlewConst = text.split("slew_const: ",1)[1]
        temp2SlewConst = tempSlewConst.split()[0]
        storedSlewConst = float(temp2SlewConst)
        SlewConst.append(storedSlewConst)
    elif 'dist:' in text:
        tempDistance = text.split("dist: ",1)[1]
        temp2Distance = tempDistance.split()[0]
        storedDist = float(temp2Distance)
        Distance.append(storedDist)
    elif 'left child' in text:
        if 'NULL' in text:
            leftChild.append("None")
        else:
            tempLeftChild = text.split("number: ",2)[1]
            temp2LeftChild = tempLeftChild.split()[0]
            storedLeftChild = int(temp2LeftChild)
            LeftChild.append(storedLeftChild)
    elif 'right child'in text:
        if 'NULL' in text:
            RightChild.append("None")
        else:
            tempRightChild = text.split("number: ",2)[1]
            temp2RightChild = tempRightChild.split()[0]
            storedRightChild = int(temp2RightChild)
            RightChild.append(storedRightChild)
    elif not text:
        break
   
#Fix next five lines to automatically handle cases where "distance" is not present
temp = Distance[len(Distance)-1]
Distance.pop(len(Distance)-1)
Distance.append("None")
Distance.append("None")
Distance.append(temp)


if (len(NodeNumbers) == len(Capacitance) == len(Delay) == len(LocationX) == len(LocationY) == len(OrigPermReg) == len(PermReg) == len(SubtreeCost) == len(SlewConst) == len(Distance) == len(Buffers) == len(parents) == len(LeftChild) == len(RightChild)): #Check to make sure all the lists are of equal length
    numElements = len(NodeNumbers)
else:
    print("The list sizes do not match")
    print(len(NodeNumbers))
    print(len(Capacitance))
    print(len(Delay))
    print(len(LocationX))
    print(len(LocationY))
    print(len(OrigPermReg))
    print(len(PermReg))
    print(len(SubtreeCost))
    print(len(SlewConst))
    print(len(Distance))
    print(len(parents))
    print(len(Buffers))
    print(len(LeftChild))
    print(len(RightChild))

for i in range(0,numElements): #add the elements into the linked list
    List.AddNode(NodeNumbers[i], Capacitance[i], Delay[i], LocationX[i], LocationY[i], OrigPermReg[i], PermReg[i], SubtreeCost[i], SlewConst[i], parents[i], Buffers[i], Distance[i], LeftChild[i], RightChild[i])


################################## BEGIN CREATING THE GUI HERE ###################################
class ClockTreeGUI():
    
    def __init__(self, root):
        self.root = root
        self.root.title("Drexel University VANDAL Lab: Clock Tree Synthesis, Version 0.4")
        root.minsize(width = 1280, height = 750)
        root.maxsize(width = 1280, height = 750)

        #Place widgets below here
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "Close", command = self.close)
        menubar.add_cascade(label = "File", menu = filemenu)
        helpmenu = Menu(menubar, tearoff = 0)
        helpmenu.add_command(label = "How to Use", command = self.showHelp)
        menubar.add_cascade(label = "Help", menu = helpmenu)
        levelmenu = Menu(menubar, tearoff = 0)
        levelmenu.add_command(label = "Enable Levels")
        menubar.add_cascade(label = "Levels", menu = levelmenu)

        global f
        f = Figure(figsize=(7,4), dpi =100)
        global a
        a = f.add_subplot(111)
        a.plot(LocationX, LocationY, '.')
        a.set_title('Clock Tree')
        a.set_xlabel('X-Location')
        a.set_ylabel('Y-Location')

        self.v = IntVar()
        self.v.set(0)
        self.frame2 = LabelFrame(root, text = "List of Nodes", width = 640, height = 300, bd = 5)
        self.frame3 = LabelFrame(root, text = "Detailed Node Information", width = 640, height = 350, bd = 5)
        self.frame4 = LabelFrame(root, text = "Search", width = 200, height = 100, bd = 5)
        self.canvasTree = FigureCanvasTkAgg(f, master = root)
        toolbarFrame = Frame(root)
        self.scrollBar = Scrollbar(self.frame2, orient = VERTICAL, jump = 1)
        self.scrollBarText = Scrollbar(self.frame3, orient = VERTICAL)
        self.ListBox1 = Listbox(self.frame2, width = 18, height = 15, yscrollcommand = self.scrollBar.set)
        self.SearchEntry = Entry(self.frame4, width = 25)
        self.NodeInfoTextBox = Text(self.frame3, height = 15, width = 85, yscrollcommand = self.scrollBarText.set)
        self.SearchButton = Button(text = "Search", width = 25, command = self.searchNode)
        self.DisplayButton = Button(text = "Display", width = 25, command = self.displayNodeInfo)
        self.ClearButton = Button(text = "Clear", width = 25, command = self.clearText)
        self.CheckButton = Checkbutton(root, text = "Display Children with Parent", onvalue = 1, offvalue = 0, variable = self.v)
        
        global canvas
        canvas = FigureCanvasTkAgg(f, master = root)
        canvas.show()
        canvas.get_tk_widget().grid(row = 1, column = 1, columnspan = 5)
        canvas._tkcanvas.grid(row = 0, column = 1)

        def getClosestNode(self, XCoord, YCoord):
            closestNode = 0
            totaldistance = 100000000000.0
            xdistance = 0.0
            ydistance = 0.0
            for i in range(0, len(LocationX)):
                xdistance = abs(XCoord - LocationX[i])
                ydistance = abs(YCoord - LocationY[i])
                if(totaldistance > (xdistance + ydistance)):
                    totaldistance = xdistance + ydistance
                    closestNode = i
            self.NodeInfoTextBox.insert(END, List.PrintNodeDetails(closestNode))


        def callback(event):
            global XCoord, YCoord
            tempx = float(event.xdata)
            tempy = float(event.ydata)
            XCoord = float(round(tempx,2))
            YCoord = float(round(tempy,2))
            getClosestNode(self, XCoord, YCoord)
            
        canvas.mpl_connect('button_press_event', callback)
        
        toolbarFrame.grid(row=0, column = 0, columnspan = 3)
        toolbar = NavigationToolbar2TkAgg(canvas, toolbarFrame)
        #Set up the grid of the GUI here
        self.scrollBar.grid(row = 2, column = 1, sticky = 'NW')
        self.ListBox1.grid(row = 2, column = 0 )
        self.NodeInfoTextBox.grid(row = 2, column = 0)
        self.SearchEntry.grid(row = 2, column = 1)
        
        self.frame2.grid(row = 2, column = 0)
        self.frame3.grid(row = 2, column = 3, sticky = 'NW')
        self.frame4.grid(row = 2, column = 1, sticky = 'NW')
        self.SearchButton.grid(row = 2, column = 1, sticky = 'W')
        self.DisplayButton.grid(row = 2, column = 2)
        self.ClearButton.grid(row = 2, column = 2, sticky = 'NW')
        self.CheckButton.grid(row = 3, column = 1, sticky = 'NW')




        #Print the Nodes into the list box here
        for i in range(0, len(NodeNumbers)):
            self.ListBox1.insert(END, "Node Number: " + str(i))

        #Configure the widgets here
        root.config(menu = menubar)
        self.scrollBar.config(command = self.ListBox1.yview)
        self.scrollBarText.config(command = self.NodeInfoTextBox.yview)
       
####### Utility functions to display node information ##########
    def searchNode(self):
        node = self.SearchEntry.get()
        if (node == ''):
            error = "Please make a valid search!"
            print(error)
        else:
            int(node)
            self.ListBox1.selection_set(node)
            self.ListBox1.see(node)
        #ADD ERROR CHEKCING AT SOME POINT
    
    def displayNodeInfo(self):
        line = self.ListBox1.curselection()
        value = self.ListBox1.get(line[0])
        number = value.strip("Node Number: ")
        numberFloat = int(number)
        choice = self.v.get()
        self.NodeInfoTextBox.insert(END, List.PrintNodeDetails(numberFloat))
        target = List.getNode(numberFloat)
        if(choice == 1):
            self.showChildren(target)
        a.plot(target.LocationX, target.LocationY, marker = 'o')
        canvas.draw()
        if(target.LeftChild != "None"):
            leftChild = List.getNode(target.LeftChild)
            x = [target.LocationX, leftChild.LocationX]
            y = [target.LocationY, leftChild.LocationY]
            a.plot(x,y)
            canvas.draw()
        if(target.RightChild != "None"):
            rightChild = List.getNode(target.RightChild)
            x = [target.LocationX, rightChild.LocationX]
            y = [target.LocationY, rightChild.LocationY]
            a.plot(x,y)
            canvas.draw()
        

    def clearText(self):
        self.NodeInfoTextBox.delete('1.0', END)
        f.clf()
        canvas.draw()
        a = f.add_subplot(111)
        a.plot(LocationX, LocationY, '.')
        a.set_title('Clock Tree')
        a.set_xlabel('X-Location')
        a.set_ylabel('Y-Location')
        canvas.show()


    def showHelp(self):
        print("This is a work in progress\n")

    def close(self):
        exit(-1)

    def showChildren(self, parent):
        leftChildNum = parent.LeftChild
        rightChildNum = parent.RightChild
        if(leftChildNum != "None"):
            self.leftChild = Toplevel(width = 85, height = 16)
            self.textBoxLeft = Text(self.leftChild, height = 25, width = 85, yscrollcommand = self.scrollBarText.set)
            self.textBoxLeft.pack()
            self.textBoxLeft.insert(END, List.PrintNodeDetails(leftChildNum))
        if (rightChildNum != "None"):
            self.rightChild = Toplevel(width = 85, height = 16)
            self.textBoxRight = Text(self.rightChild, height = 25, width = 85, yscrollcommand = self.scrollBarText.set)
            self.textBoxRight.pack()
            self.textBoxRight.insert(END, List.PrintNodeDetails(rightChildNum))

root = Tk()
my_gui = ClockTreeGUI(root)
root.mainloop() #Keeps the GUI running
