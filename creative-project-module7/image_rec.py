import requests
import os

api_key = 'acc_584bfdcc678f660'
api_secret = 'efc88efd77cbe8382eb82075ee2ffbdb'

class Image_Finder:

    def image(self):
        image_path = self.find_image_path()
        if not image_path:
            raise ValueError("Image file not found in 'static/files' directory.")

        response = requests.post(
            'https://api.imagga.com/v2/tags',
            auth=(api_key, api_secret),
            files={'image': open(image_path, 'rb')})
        result = response.json()
        data = result['result']['tags'][0]['tag']['en']
        return data

 
    def find_image_path(self):
        image_extensions = ['.jpg', '.png', '.jpeg']
        image_files = [os.path.join('static/files', 'image' + ext) for ext in image_extensions]
        image_files = [f for f in image_files if os.path.exists(f)]
        if not image_files:
            return None

        # Sort the image files by their modification time (most recent first)
        image_files.sort(key=lambda f: os.path.getmtime(f), reverse=True)

        return image_files[0]


