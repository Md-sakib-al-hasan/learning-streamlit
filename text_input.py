import streamlit as st

st.title("My first streamlit web apps", anchor=False)
st.header("This is my second header", anchor=False, divider=True)
st.subheader("This is my third header", anchor=False, divider=True)
st.text("hello world")
st.markdown("**Hello** World")

st.divider()

# ==========================================
# 1. Image Uploader & Viewer
# ==========================================
st.header("🖼️ Image Uploader", anchor=False)

uploaded_image = st.file_uploader(
    "Choose an image file",
    type=["jpg", "jpeg", "png", "webp"]
)

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image Preview", use_container_width=True)
else:
    # Fallback default image preview if no file is uploaded yet
    st.info("Upload an image above or see the default preview below:")
    st.image("https://picsum.photos/800/400", caption="Default Sample Image", use_container_width=True)

st.divider()

# ==========================================
# 2. Video Uploader & Player
# ==========================================
st.header("🎥 Video Uploader", anchor=False)

uploaded_video = st.file_uploader(
    "Choose a video file",
    type=["mp4", "mov", "avi", "webm"]
)

if uploaded_video is not None:
    st.video(uploaded_video)
else:
    # Fallback default sample video
    st.info("Upload a video above or preview the sample below:")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

st.divider()

# ==========================================
# 3. Audio Uploader & Player
# ==========================================
st.header("🎵 Audio Uploader", anchor=False)

uploaded_audio = st.file_uploader(
    "Choose an audio file",
    type=["mp3", "wav", "ogg"]
)

if uploaded_audio is not None:
    st.audio(uploaded_audio)
else:
    # Fallback default sample audio
    st.info("Upload an audio file above or preview the sample below:")
    st.audio("https://www.w3schools.com/html/horse.mp3")