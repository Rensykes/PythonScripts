'''requires
brew zbar
pip install pyzbar
pip install opencv-python

IN DEPTH BAR CODE READING
https://www.pyimagesearch.com/2014/11/24/detecting-barcodes-images-python-opencv/
'''

from pyzbar.pyzbar import decode #import decode module from zbar
import cv2 #and openCv
import requests

filename = "img.jpg" 
img = cv2.imread(filename) #read and store the image in img
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #turn it grey trough openCv

barcodes = decode(gray_img) #read barcodes in the image -> contains a list with all the barcodes
print(barcodes) #print infos on the screen

#Assuming there is just one barcode, using Open Food Facts API retrive informations
if len(barcodes) == 1:
    code = barcodes[0].data
    url = "https://it.openfoodfacts.org/api/v0/product/{}.json".format(code)
    data = requests.get(url).json()
    if data["status"] == 1: #Check if the barcode is in Open Food Facts DB
        product = data["product"]
        #brand = product["brands"]
        #print("Producer:", product["brands"])
        print("Name:", product["product_name"])
    else:
        print("Product Not Found!")
else:
    print("Barcode Not Found!")