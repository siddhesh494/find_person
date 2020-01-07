import face_recognition
from PIL import Image, ImageDraw

image_of_sid = face_recognition.load_image_file("image/sid.jpeg")
sid_face_encodings = face_recognition.face_encodings(image_of_sid)[0]

image_of_nik = face_recognition.load_image_file("image/nik.jpeg")
nik_face_encodings = face_recognition.face_encodings(image_of_nik)[0]

image_of_rahul = face_recognition.load_image_file("image/rahul.jpeg")
rahul_face_encodings = face_recognition.face_encodings(image_of_rahul)[0]

image_of_ut = face_recognition.load_image_file("image/utkarsh.jpeg")
ut_face_encodings = face_recognition.face_encodings(image_of_ut)[0]

# image_of_shraddha = face_recognition.load_image_file("image/shraddha.jpeg")
# shraddha_face_encodings = face_recognition.face_encodings(image_of_shraddha)[0]

image_of_akshata = face_recognition.load_image_file("image/akshata.jpeg")
akshata_face_encodings = face_recognition.face_encodings(image_of_akshata)[0]


known_face_encodings = [
	sid_face_encodings,
	nik_face_encodings,
	rahul_face_encodings,
	ut_face_encodings,
	# shraddha_face_encodings,
	akshata_face_encodings
]

know_face_name = [
	"Siddhesh",
	"nikhil",
	"rahul",
	"utkarsh",
	# "shraddha",
	"alien"
]
# print(know_face_name)
#load test image to find faces in
test_image = face_recognition.load_image_file("image/group/team1.jpeg")

#find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

#convert to PIL format
pil_image = Image.fromarray(test_image)


#Create a image draw instance
draw = ImageDraw.Draw(pil_image)

#loop throught faces in the test image
for(top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
	matches = face_recognition.compare_faces(known_face_encodings, face_encodings)
	# print(matches)
	name = "Unknown Person"

# 	#if match
	if True in matches:
		first_match_index = matches.index(True)
		# print(first_match_index)
		name = know_face_name[first_match_index]
		# print(name)
	#Draw Box
	draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

	#Draw label
	text_width, text_height = draw.textsize(name)
	draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0),outline=(0,0,0))
	draw.text((left + 6, bottom-text_height - 5), name, fill=(255, 255, 255))

del draw

pil_image.show()
