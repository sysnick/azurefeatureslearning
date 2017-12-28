import cognitive_face as CF
KEY = 'b7f92957bb354f96b6907df47895db2d'

CF.Key.set(KEY)

CF.util.Key.get()

print(CF.util.Key.get())

Base_URL = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0'

CF.BaseUrl.set(Base_URL)

print(CF.BaseUrl.get())

img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'

faces = CF.face.detect(img_url)

print(faces)

