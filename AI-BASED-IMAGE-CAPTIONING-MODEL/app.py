from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import openai
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = "Enter_api_key"

# Set up upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    # Add allowed file extensions here
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['jpg', 'jpeg', 'png']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Get user input for number of captions and hashtags
            num_captions = int(request.form['num_captions'])
            num_hashtags = int(request.form['num_hashtags'])

            # Resize the image to a smaller size (e.g., 512x512)
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as file:
                image = Image.open(file)
                image.thumbnail((512, 512))
                image_bytes = BytesIO()
                image.save(image_bytes, format='JPEG')
                image_bytes.seek(0)

            image_base64 = base64.b64encode(image_bytes.getvalue()).decode('utf-8')

            # Use a different prompt format that doesn't involve repetitive patterns
            prompt = "Generate {} captions and {} hashtags for an image of a {}".format(num_captions, num_hashtags, request.form['mood'])

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            captions = []
            hashtags = []
            for i in range(min(num_captions, len(response['choices']))):
                captions.append(response['choices'][i]['message']['content'])
            for i in range(min(num_hashtags, len(response['choices']) - num_captions)):
                hashtags.append(response['choices'][num_captions + i]['message']['content'])

            mood = request.form['mood']
            emoji = request.form['emoji']
            number = request.form['number']
            return render_template('index.html', captions=captions, hashtags=hashtags, mood=mood, emoji=emoji, number=number)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)