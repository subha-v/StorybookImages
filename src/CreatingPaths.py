from tracemalloc import start
from CreateBook import *
from Translating import * 

def createImagePath(startingPath, endingPath, bookArrayLength): 
    filename_out_final = endingPath
    
    output_file_list = []
    input_file_list = []


    for i in range (0,bookArrayLength-1):

        if(i > 9):
            filename_in = startingPath + f"0{i}"
            
        else:
            filename_in = startingPath + f"00{i}"


        filename_out = filename_out_final + f'{i}.jpg'
        output_file_list.append(filename_out)

        str_appended_digits = filename_in[-3:]
    
        int_appended_digits = int(str_appended_digits)
        int_appended_digits+=1
        str_appended_digits = str(int_appended_digits)
        
        if(int_appended_digits > 9):
            new_str_appended_digits = "0" + str_appended_digits
            
        else:
            new_str_appended_digits = "00" + str_appended_digits
        
        filename_in_new = filename_in[:-3]
       # print("new filename in"  + filename_in_new)
        filename_in_new += new_str_appended_digits
       # print(filename_in_new)
        filename_in_new += ".jpg"
        input_file_list.append(filename_in_new)

    return output_file_list, input_file_list

if __name__ == "__main__":
    print(createImagePath("./images/book-friends/image-", "./images/translated-book/page", 18))
