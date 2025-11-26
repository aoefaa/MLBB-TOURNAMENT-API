import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
import os

cloudinary.config(
    cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key = os.getenv('CLOUDINARY_API_KEY'),
    api_secret = os.getenv('CLOUDINARY_API_SECRET'),
    secure = True
)

class StorageClient:
    def __init__(self):
        pass

    def upload_file(self, file_obj, folder="mlbb_tournament/uploads"):
        """
        Upload file ke Cloudinary dan return URL publiknya.
        :param file_obj: Object file dari Flask (request.files['image'])
        :param folder: Folder tujuan di Cloudinary (misal: 'mlbb_tournament/heroes')
        :return: Public URL (String)
        """
        if not file_obj:
            return None

        try:
            upload_result = cloudinary.uploader.upload(
                file_obj,
                folder=folder,
                resource_type="auto" 
            )

            return upload_result.get('secure_url')

        except Exception as e:
            print(f"Cloudinary Upload Error: {str(e)}")
            raise e