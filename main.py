from FacialAuthentication_package import facematch
from FacialAuthentication_package import image_manager

#need to check the 3.5 mb, need for a compressor

#try with the same face and same image
target_img = image_manager.comprime_image("data/test/check_image.jpg")
check_img = image_manager.comprime_image("data/test/check_image.jpg")
result = facematch.match_image(target_img,check_img)
print(result)

#try with the same face1
target_img = image_manager.comprime_image("data/test/check.jpg")
result = facematch.match_image(target_img,check_img)
print(result)

#try with the same face2
target_img = image_manager.comprime_image("data/test/same_face.jpg")
result = facematch.match_image(target_img,check_img)
print(result)

#try with same person but different image and with sunglass
target_img = image_manager.comprime_image("data/test/same_face_with_sg.jpg")
result = facematch.match_image(target_img,check_img)
print(result)

#try a photo with 2 person which one of these is the same of target_img
target_img = image_manager.comprime_image("data/test/two_faces.png")
result = facematch.match_image(target_img,check_img)
print(result)

#try with different person 
target_img = image_manager.comprime_image("data/test/totti.jpg")
result = facematch.match_image(target_img,check_img)
print(result)




