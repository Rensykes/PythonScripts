'''requires
brew zbar
pip install pyzbar
pip install opencv-python
'''

from pyzbar.pyzbar import decode #import decode module from zbar
import cv2 #and openCv
import requests

filename = "img.jpg" 
img = cv2.imread(filename) #read and store the image in img

def get_barcode_info(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #turn it grey trough openCv
    barcodes = decode(gray_img) #read barcodes in the image -> contains a list with all the barcodes
    print(barcodes) #print infos on the screen

	#Assuming there is just one barcode, using Open Food Facts API retrive informations
    if len(barcodes) == 1:
        code = barcodes[0].data
        url = "https://it.openfoodfacts.org/api/v0/product/{}.json".format(code)
        data = requests.get(url).json()
        if data["status"] == 1: #if the product is in the Open Food Facts DB then...
			#...Retrieve informations about it
            product = data["product"]
            #brand = product["brands"]
            #print("Producer:", product["brands"])
            print("Name:", product["product_name"])
            #return "Producer: {}    Name: {}".format(product["brands"], product["product_name"])
            return "Name: {}".format(product["product_name"])
        else:
            return "Product Not Found!"
    else:
        return "Barcode Not Found!"

cap = cv2.VideoCapture(0) #read stream video from webcam #0 (front 1)
while(True):
  ret, frame = cap.read() #save the image from webcam in frame
  info = get_barcode_info(frame) #pass it to get_barcode_info
  cv2.putText(frame, info, (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2) #add informations from get_barcode_info on the image as text
  #putText parameters: image where you want to insert text, text to insert, position (in pixels) where to insert text, font used, text dimension, RGB color, thickness of the line

  cv2.imshow('Barcode', frame) #creates a window named "Barcode" that displays image contained in frame
  code = cv2.waitKey(30) #cv2.imshow always need cv2.waitKey that renderize the image (without it you wouldnt see anything) and stops the program for 30s. Return -1 unless a key is pressed
  if code == ord('q'): #if q key is pressed then exit
      break
