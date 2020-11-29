from FacialAuthentication_package import facematch

#need to check the 3.5 mb, need for a compressor

#try with the same face
target_img = "data/test/check.jpg"
check_img = "data/test/check.jpg"
facematch.match_image(target_img,check_img)

#try with same person but different image
target_img = "data/test/same_face_with_sg.jpg"
check_img = "data/test/check.jpg"
facematch.match_image(target_img,check_img)

#try with same person but different image and with sunglass
target_img = "data/test/same_face_with_sg.jpg"
check_img = "data/test/check.jpg"
facematch.match_image(target_img,check_img)

#try a photo with 2 person which one of these is the same of target_img
target_img = "data/test/same_face_with_sg.jpg"
check_img = "data/test/check.jpg"
facematch.match_image(target_img,check_img)

#try with different person 
target_img = "data/test/same_face_with_sg.jpg"
check_img = "data/test/check.jpg"
facematch.match_image(target_img,check_img)




