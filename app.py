import streamlit as st
import calculator

st.set_page_config(
    page_title="Streamlit Apps & Demos",
    page_icon="🚀",
    layout="wide",
)

st.sidebar.title("🧭 Navigation")
st.sidebar.caption("Explore learning modules and interactive applications.")

selected_page = st.sidebar.radio(
    "Select an Application:",
    (
        "🧮 Calculator App",
        "📝 Input Elements Demo",
        "🖼️ Text & Media Demo",
    ),
    index=0,
)

st.sidebar.divider()
st.sidebar.info("💡 **Tip:** Switch between modules anytime using the menu above.")

if selected_page == "🧮 Calculator App":
    calculator.run_calculator_app()

elif selected_page == "📝 Input Elements Demo":
    st.title("Streamlit Widgets: Input Elements")
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("What is your name? :house:", placeholder="Enter your name")
        number = st.number_input("Enter your age", min_value=0, max_value=120, value=25)
    with col2:
        st.subheader("Live Output")
        if name:
            st.success(f"Hello, **{name}**!")
        st.info(f"You are **{number}** years old.")

elif selected_page == "🖼️ Text & Media Demo":
    st.title("My Streamlit Web App - Text & Media Demo", anchor=False)
    st.markdown("Showcasing headers, markdown, image, audio, and video uploaders.")
    st.divider()

    tab_img, tab_vid, tab_aud = st.tabs(["🖼️ Image Uploader", "🎥 Video Uploader", "🎵 Audio Uploader"])

    with tab_img:
        st.subheader("🖼️ Image Uploader & Viewer")
        uploaded_image = st.file_uploader(
            "Choose an image file",
            type=["jpg", "jpeg", "png", "webp"],
            key="app_img_uploader",
        )
        if uploaded_image is not None:
            st.image(uploaded_image, caption="Uploaded Image Preview", use_container_width=True)
        else:
            st.info("Upload an image above or see the default preview below:")
            st.image("https://picsum.photos/800/400", caption="Default Sample Image", use_container_width=True)

    with tab_vid:
        st.subheader("🎥 Video Uploader & Player")
        uploaded_video = st.file_uploader(
            "Choose a video file",
            type=["mp4", "mov", "avi", "webm"],
            key="app_vid_uploader",
        )
        if uploaded_video is not None:
            st.video(uploaded_video)
        else:
            st.info("Upload a video above or preview the sample below:")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")

    with tab_aud:
        st.subheader("🎵 Audio Uploader & Player")
        uploaded_audio = st.file_uploader(
            "Choose an audio file",
            type=["mp3", "wav", "ogg"],
            key="app_aud_uploader",
        )
        if uploaded_audio is not None:
            st.audio(uploaded_audio)
        else:
            st.info("Upload an audio file above to listen to it.")
