'''
Name: Tanvi Ravindra Pawale
Date: 10/15/2016
Class and Section: CS524-02
Pyhton Version: Python 2.7.10

The below program will take .ppm image file as input.It will apply various basic filters such as 
grayscale, flatten red, flatten green, flatten blue, invert image and few extra fliters like 
extreme contrast and horizontal blur. This filters are applied according to user input, thus
it might be just one filter or combination of filters. It will give one output file which 
represents all user desired filters in it.

'''

#os library is imported just to get current directory of script being running so that path will be taken directly
import os;

#--------------------Class ppmReader -------------------------
class ppmReader(object):
    def __init__(self, iFile, oFile, path):
        
        self.iFile = iFile;
        
        # this if statement is to make sure if user do not enter output file name program takes default name
        if(oFile == " "):
            self.oFile = "output.ppm" 
        elif((os.path.splitext(oFile)) != ".ppm"):
            self.oFile = oFile + ".ppm"
        else:
            self.oFile = oFile; 
        
        self.path = path;
        
        # open file with concatination of path and file name, r means read   
        self.data= open(self.path + "/" + self.iFile,"r")  
        self.data_in=self.data.read()
        
        #splits file in 5 parts
        self.splits=self.data_in.split(None, 4)  
        self.type=self.splits[0]
        self.columns=int(self.splits[1])
        self.rows=int(self.splits[2])
        self.colour=int(self.splits[3])
        
        #convert to list
        self.pixels = self.splits[4].split(); 
     
                   
    #-------------------method which converts image to greyscale----------------
    def greyScale(self):
        
        # takes average of red, green, blue pixels and replace r, g, b with average value.  
        # this gives greyscale
        
        #range will make ind variable go from 0 to len(self.pixels)-1 with step of 3
        for ind in range(0, len(self.pixels), 3): 
            r, g, b = self.pixels[ind:ind+3]
            r, g, b =int(r), int(g),int(b);
            br = str(int(round((r+g+b)/3.0)))
            self.pixels[ind:ind+3] = br, br, br;


    #-------------------method which converts image to Flatten Red----------------
    def flattenRed(self):
        # makes red pixel as zero
        #range will make ind variable go from 0 to len(self.pixels)-1 with step of 3
        for ind in range(0, len(self.pixels), 3):
            self.pixels[ind] = str(0);
    
    
    #-------------------method which converts image to Flatten Green----------------
    def flattenGreen(self):
        # makes green pixel as zero
        #range will make ind variable go from 0 to len(self.pixels)-1 with step of 3
        for ind in range(0, len(self.pixels), 3):
            self.pixels[ind+1] = str(0);  
     
     
    #-------------------method which converts image to Flatten Blue----------------
    def flattenBlue(self):
        # makes blue pixel as zero
        #range will make ind variable go from 0 to len(self.pixels)-1 with step of 3
        for ind in range(0, len(self.pixels), 3):
            self.pixels[ind+2] = str(0); 
     
           
    #-------------------method which converts image to Flip vertical----------------    
    def flipVertical(self):
        # self.revert list will store reversed list of pixels     
        self.revert = self.pixels[::-1];
        
        #range will make ind variable go from 0 to len(self.pixels)-1 with step of 3
        for ind in range(0, len(self.revert), 3):
            #self.revert has r= b, g = g, and b = r so
            #reverse r, g, b  again in self.revert list 
            r,g,b = str(self.revert[ind+2]), str(self.revert[ind+1]), str(self.revert[ind]);
            self.pixels[ind:ind+3] = r,g,b;
     
    #-------------------method which converts image to Flip Horizontal----------------                      
    def flipHorizontal(self):
        #range will make ind variable go from 1 to len(self.pixels)+1 with step of 3
        for ind in range(1, len(self.pixels)+1, self.columns*3):
            self.horizontal = self.pixels[ind-1:ind+self.columns*3-1];
            self.horizontal=self.horizontal[::-1]
            for i in range(0, len(self.horizontal), 3):    
                r,g,b = str(self.horizontal[i+2]), str(self.horizontal[i+1]), str(self.horizontal[i]);
                self.horizontal[i:i+3] = r,g,b;  
            self.pixels[ind-1:ind+self.columns*3-1] = self.horizontal;
                           
    #-------------------method which inverts image-------------------------------           
    def invertImage(self):
        #invert image is negate all r, g, b values
        for ind in range(0, len(self.pixels), 3):
            r, g, b = self.pixels[ind:ind+3]
            r, g, b =str(255-int(r)), str(255-int(g)),str(255-int(b));
            self.pixels[ind:ind+3]= r,g,b;
     
                   
    #-------------------method which converts image to Extreme Contrast----------------
    #------------------bonus filter
    def extremeContrast(self):
        #takes mid point of 0 and 255 
        mid = (self.colour/2); 
        for ind in range(0,len(self.pixels)):
            #if pixel is greater than mid it is converted to 255
            if(int(self.pixels[ind]) > mid):
                self.pixels[ind] = str(self.colour);
            #if pixel is less than equals to mid it is converted to 0
            else:
                self.pixels[ind] =str(0);
    
    
    #-------------------method which converts image to Horizontal Blur----------------
    #------------------bonus filter
    def horizontalBlur(self):
        if(len(self.pixels)%9 == 0): #if columns=3 and row =3 
            for ind in range(0, len(self.pixels), 9):
                #values of the red, green and blue of three adjacent pixels are averaged sepeartely 
                #then all three red or three green or three blue adjacent pixels are replaced with respective average values 
                r= int(round((int(self.pixels[ind])+int(self.pixels[ind+3])+int(self.pixels[ind+6]))/3));
                g= int(round((int(self.pixels[ind+1])+int(self.pixels[ind+4])+int(self.pixels[ind+7]))/3));
                b= int(round((int(self.pixels[ind+2])+int(self.pixels[ind+5])+int(self.pixels[ind+8]))/3));
                r, g, b =str(r), str(g),str(b);
                self.pixels[ind:ind+9] = r, g, b, r, g, b, r, g, b;
        elif(len(self.pixels)%9 == 3): #if columns=4 and rows=4  
            for ind in range(0, len(self.pixels), 9+3):
                r= int(round((int(self.pixels[ind])+int(self.pixels[ind+3])+int(self.pixels[ind+6]))/3));
                g= int(round((int(self.pixels[ind+1])+int(self.pixels[ind+4])+int(self.pixels[ind+7]))/3));
                b= int(round((int(self.pixels[ind+2])+int(self.pixels[ind+5])+int(self.pixels[ind+8]))/3));
                r, g, b =str(r), str(g),str(b);
                self.pixels[ind:ind+9] = r, g, b, r, g, b, r, g, b;
        elif(len(self.pixels)%9 == 6): # if columns=5 and rows=5  
            for ind in range(0, len(self.pixels), 9+6): 
                r= int(round((int(self.pixels[ind])+int(self.pixels[ind+3])+int(self.pixels[ind+6]))/3));
                g= int(round((int(self.pixels[ind+1])+int(self.pixels[ind+4])+int(self.pixels[ind+7]))/3));
                b= int(round((int(self.pixels[ind+2])+int(self.pixels[ind+5])+int(self.pixels[ind+8]))/3));
                r, g, b =str(r), str(g),str(b);
                self.pixels[ind:ind+9] = r, g, b, r, g, b, r, g, b;
        else:
                print("not valid");
                
                
    #------------------method which writes output file------------------------------            
    def write_to_file(self):
        # opens output file and writes to that file which is stored in current directory
        #w means write  
        self.dataout= open(self.path+ "/" +self.oFile, "w")
        
        self.dataout.write(str(self.type)+'\n'+ str(self.columns) +' '+ str(self.rows)+'\n'+str(self.colour)+'\n');
        
        for data in self.pixels:
            self.dataout.write(str(data)+' ')
        
        print(self.oFile + " file is created ")

###-----------------------function UserInput ----------
def UserInput(iName, oName, cpath):
    print("Here are your choices: \n [1] Grayscale [2] Flatten red \n [3] Flatten green [4] Flatten Blue\n [5] Invert Image [6] Extreme Contrast\n [7] Horizontal Blur [8] Vertical Flip \n [9] Horizontal Flip  ");
    userChoice=[] 
    for i in range(0,9):
        
        #while loop is to verify input is y/n or Y/N
        #thus anything else will print message and will again ask input for same choice
        while(True):
            userInput = raw_input("Do you want [" + str(i+1) + "]? (y/n) ")
            
            if(userInput == 'n' or userInput == 'N' or userInput == 'y' or userInput == 'Y'):
                userChoice.append(userInput);
                break;
            else:
                print("Input is invalid. Please type y or Y or n or N.");
                continue;
                    
    #call to class ppmReader 
    # sends input file name, output file name and current path to class.
    ppmImage = ppmReader(iName, oName, cpath);

    # all if statements will call different methods in class ppmReader if user enters y/Y to that choice
    if(userChoice[0] == 'y' or userChoice[0] == 'Y'):
        ppmImage.greyScale();
    if(userChoice[1] == 'y' or userChoice[1] == 'Y'):
        ppmImage.flattenRed();
    if(userChoice[2] == 'y' or userChoice[2] == 'Y'):
        ppmImage.flattenGreen();
    if(userChoice[3] == 'y' or userChoice[3] == 'Y'):
        ppmImage.flattenBlue();
    if(userChoice[4] == 'y' or userChoice[4] == 'Y'):
        ppmImage.invertImage();
    if(userChoice[5] == 'y' or userChoice[5] == 'Y'):
        ppmImage.extremeContrast();
    if(userChoice[6] == 'y' or userChoice[6] == 'Y'):
        ppmImage.horizontalBlur();
    if(userChoice[7] == 'y' or userChoice[7] == 'Y'):
        ppmImage.flipVertical();
    if(userChoice[8] == 'y' or userChoice[8] == 'Y'):
        ppmImage.flipHorizontal();
        
    ppmImage.write_to_file();
    


###---------------------main function------------------------------------------------
def main():
    #path where current .py script is will be retrived
    cpath = os.path.dirname(os.path.abspath(__file__));     
    
    #takes user input for input file name and output file name
    iName = raw_input("Enter name of the input image File: ");
    oName = raw_input("Enter name of the output File: ");
    
    #exception handling is done if input file name is not in directory
    try:
        data= open(cpath + "/" + iName,"r")
    except IOError:
        print('Unable to open this file ' + iName)
    else:
        data.close();
        UserInput(iName, oName, cpath);


#-----------call to main function------------------------------------------------
main();