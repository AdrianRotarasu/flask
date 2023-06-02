from flask import Flask, render_template, request
import os 
import base64
from PIL import Image
from io import BytesIO
from deeplearning import modify
# webserver gateway interface
app = Flask(__name__)

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH,'static/upload/')


@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        modified_image = modify(upload_file)
       # Convert the uploaded image to base64 string
        upload= image = Image.open(upload_file)
        buffered = BytesIO()
        upload.save(buffered, format='PNG')  # Save as PNG format
        upload_image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        # Convert the modified image to base64 string
        buffered = BytesIO()
        modified_image.save(buffered, format='PNG')  # Save as PNG format
        modified_image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return render_template('index.html', upload=True, upload_image=upload_image_base64, modified=modified_image_base64)
    return render_template('index.html', upload=False)




if __name__ =="__main__":
    app.run(debug=True)
