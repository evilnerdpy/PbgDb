from PIL import Image
import numpy as np

class PngDb():
    def __init__(self):
        self.x_resolution =600
        self.y_resolution =500 
        self.f_content = bytes()

    def encode(self ,file_path, name):

        """ encode your file into png database 
            1 arg - file path
            2 arg - png database name (without extention)
        """
        with open(file_path , "rb") as f:
            f_content = f.read()
            self.f_content = f_content
            data = []
            for i in range(len(f_content)):
                data.append(f_content[i])
            
            if ((self.x_resolution * self.y_resolution) <= len(data)):
                is_not_long_enough = True
                while is_not_long_enough:
                    self.x_resolution +=100
                    self.y_resolution +=100
                    if ((self.x_resolution * self.y_resolution) - len(data) > 1000):
                        is_not_long_enough = False

            array_to_write = []
            
            for i in range(len(data)):
                array_to_write.append([data[i],0,0])
            
                
            t =(self.y_resolution , self.x_resolution,3)
            image_array = np.zeros(t,dtype=np.uint8)

            data_index=0
            for i in range(self.y_resolution):
                for j in range(self.x_resolution):
                    if data_index == len(array_to_write):
                        image_array[i,j] = [0,0,12]
                    else:
                        image_array[i,j] = array_to_write[data_index]
                        data_index+=1
            img = Image.fromarray(image_array, "RGB")
            img.save(name + ".png")
            print("done")

    def decode(self,file,name):
        """
            encode png database back into oroginal file
            1 arg - png database path 
            2 arg - decoded filename (WITH EXTENTION)
        """
        with Image.open(file) as pngdb:
            data = np.asarray(pngdb)
            colors_data = []
            for i in range(len(data)):
                for j in range(len(data[i])):
                    cur_item = [0,0,0]
                    cur_item = [data[i,j,0],data[i,j,1],data[i,j,2]]
                    colors_data.append(cur_item)
            
            array_to_decode = []
            ext =""
            is_getting_extention = False
            
            for pixel in  colors_data:
                if pixel[2] == 12:
                    break
                else:
                    array_to_decode.append(int(pixel[0]))
                  
            a = bytes(array_to_decode)
              
            with open(name , "wb") as encoded_file:
                encoded_file.write(a)
                encoded_file

            print("done")

            
                
         
                    
            
       
                
            
    
                    
           


             


        

    
            





