import webbrowser
import pyimgur

CLIENT_ID  = '8590338971a3af7'
SECRET = '9c939ebb5bda20fdb021e549ac503f747ba3f2c1'

def load_images_from_imgur():

    result = {}

    im = pyimgur.Imgur(CLIENT_ID, SECRET)

    try:
        images = im.get_user('jmpark6846').get_images(limit=30)
    except Exception:

        auth_url = im.authorization_url('pin')
        webbrowser.open(auth_url)
        pin = input("What is the pin? ") # Python 3x
        im.exchange_pin(pin)
        images = im.get_user('jmpark6846').get_images()

    for img in images:
        print(f'{img.name} - {img.link_large_thumbnail}')
        result[img.name]=img.link_large_thumbnail


    return result

