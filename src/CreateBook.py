from Translating import *
from ImageProcessing import *
import os
from fpdf import FPDF
from os import listdir
from CreatingPaths import *
from Main import *

#adding some random comments uwu


def CreateBook(bookArray, firstImageFilePath, language):
    translatedbookarray, englishbookarray = translate_book(bookArray, language)
    # translatedbookarray, englishbookarray = ['Ilali yam yayineengxaki ezininzi. Senza umgca omde wokukha amanzi etephini enye. ', ' Salinda ukutya okwanikelwa ngabanye.', 'Satshixa izindlu zethu kwangethuba ngenxa yamasela.',  'Abantwana abaninzi baye basishiya isikolo. ',  'Amantombazana aselula ayesebenza njengezicakakazi kwezinye iidolophana. ' , ' Amakhwenkwe aselula ayezula-zula elalini ngoxa amanye esebenza kwiifama zabantu. ', ' Xa kwakuvuthuza umoya, amaphepha amdaka ajinga emithini nasezintangweni. ', 'Abantu babesikwa yiglasi eyaphukileyo eyaphoswa ngokungakhathali. ', ' Kwathi ngenye imini, itephu yoma yaye nezikhongozelo zethu zazingenamntu. ', ' Utata wayesiya kwindlu ngendlu ecela abantu ukuba baye kwiintlanganiso zelali. ', ' Abantu bahlanganisana phantsi komthi omkhulu baza baphulaphula. ', 'Ubawo waphakama wathi, Kufuneka sisebenzisane ukucombulula iingxaki zethu. ', 'UJuma oneminyaka esibhozo ubudala, ehleli phezu kwetranki wakhwaza esithi, ndingancedisa ekucoceni.' , 'Omnye umfazi wathi, Abafazi banokundithelela ukulima ukutya.', 'Kwaphakama enye indoda yathi, Amadoda aya kwemba iqula.'], ['My village had many problems. We made a long line to fetch water from one tap.',  'We waited for food donated by others.',  'We locked our houses early because of thieves.',  'Many children dropped out of school.', 'Young girls worked as maids in other villages.',  'Young boys roamed around the village while others worked on peoples farms.', 'When the wind blew, waste paper hung on trees and fences.', 'People were cut by broken glass that was thrown carelessly.', 'Then one day, the tap dried up and our containers were empty.',  'My father walked from house to house asking people to attend a village meeting.', 'People gathered under a big tree and listened.', 'My father stood up and said, We need to work together to solve our problems.', 'Eight-year-old Juma, sitting on atree trunk shouted, I can help with cleaning up.',  'One woman said, The women can join me to grow food.',  'Another man stood up and said, The men will dig a well.']
    print("length of the tranlsated book:", len(translatedbookarray))
    filename_out_final = "./images/translated-book2/page"
    output_file_list, input_file_list = createImagePath(firstImageFilePath, filename_out_final, 8)
    print("Output file list: ", output_file_list,  "Input file list", input_file_list)

    for i in range(0,len(englishbookarray)-1):
        processTranslatedImage(input_file_list[i], englishbookarray[i], translatedbookarray[i], output_file_list[i])
 

    return output_file_list

if __name__ == "__main__":
    friendsBook = "'My village had many problems. We made a long line to fetch water from one tap.  () We waited for food donated by others.  () 'We locked our houses early because of thieves.  () 'Many children dropped out of school.  () 'Young girls worked as maids in other villages.  () Young boys roamed around the village while others worked on people's farms.  () When the wind blew, waste paper hung on trees and fences.  () 'People were cut by broken glass that was thrown carelessly.  () Then one day, the tap dried up and our containers were empty.  () My father walked from house to house asking people to attend a village meeting.  () People gathered under a big tree and listened.  () 'My father stood up and said, We need to work together to solve our problems.  () 'Eight-year-old Juma, sitting on atree trunk shouted, I can help with cleaning up.  () 'One woman said, The women can join me to grow food.  () 'Another man stood up and said, The men will dig a well.  ()"
    pdf_list = CreateBook(friendsBook, "./images/decision-book-images/image-", "xh")
    dirname = "./images/translated-book2"
    list_images = (listdir(dirname))


    new_list = []

    for i in range (0,len(list_images)-1):
        new_list.append("./images/translated-book2/" + list_images[i])

    print(new_list)

    pdf = FPDF('L', 'mm', 'A4')
    # imagelist is the list with all image filenames
    for image in pdf_list:
        pdf.add_page()
        pdf.image(image,0,0,300,225)
    pdf.output("yourfile2.pdf", "F")
