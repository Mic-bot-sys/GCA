import base64

try:
    with open('/media/service-rendered/owen-beard-K21Dn4OVxNw-unsplash.jpg', "rb")  as my_image_file:
        image_data = base64.b64encode(my_image_file.read()).decode('utf-8')
        print(image_data)
except Exception as ex:
    print(ex)