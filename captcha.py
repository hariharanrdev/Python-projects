from PIL import Image, ImageDraw, ImageFont
import random
import string
import streamlit as st
from io import BytesIO

def generate_captcha(text, font_path='arial.ttf', font_size=36):
    width, height = 200, 100
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(image)

    # Randomize the position and angle
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(position, text, font=font, fill=(0, 0, 0))

    # Add some random noise (dots)
    for _ in range(random.randint(100, 1000)):
        draw.point((random.randint(0, width), random.randint(0, height)), fill=(0, 0, 0))

    return image

def generate_random_text(length=5):
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

# Streamlit Application
st.title("CAPTCHA Generator")

# Initialize CAPTCHA text in session state
if 'captcha_text' not in st.session_state:
    st.session_state['captcha_text'] = generate_random_text()

# Generate the CAPTCHA image
captcha_image = generate_captcha(st.session_state['captcha_text'])

# Convert the image to bytes
buffered = BytesIO()
captcha_image.save(buffered, format="PNG")
img_bytes = buffered.getvalue()

# Display the CAPTCHA image on the webpage
st.image(img_bytes, caption="Generated CAPTCHA", use_column_width=True)

# Button to regenerate CAPTCHA
if st.button('Refresh CAPTCHA'):
    st.session_state['captcha_text'] = generate_random_text()

# Display the CAPTCHA text
st.write(f"Generated CAPTCHA text: {st.session_state['captcha_text']}")

# Custom CSS for the button
st.markdown("""
    .stButton button {
        background-color: green;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton {
        display: flex;
        justify-content: center;
    }
""", unsafe_allow_html=True)