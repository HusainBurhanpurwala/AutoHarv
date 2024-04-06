import streamlit as st
from pathlib import Path
import PIL
import streamlit as st
import settings
import helper

# Define functions
def home_page():
    # Sidebar
    st.sidebar.markdown(
        "<h1 style='color: #9BCF53;'>Model Tuning</h1>",
        unsafe_allow_html=True
    )

    # Model Options
    model_type = 'Detection'
    #st.sidebar.radio(
    #     "Select Task", ['Detection', 'Segmentation'])

    confidence = float(st.sidebar.slider(
        "Select Model Confidence", 25, 100, 40)) / 100

    # Selecting Detection Or Segmentation
    if model_type == 'Detection':
        model_path = Path(settings.DETECTION_MODEL)
    # elif model_type == 'Segmentation':
    #     model_path = Path(settings.SEGMENTATION_MODEL)

    # Load Pre-trained ML Model
    try:
        model = helper.load_model(model_path)
    except Exception as ex:
        st.error(f"Unable to load model. Check the specified path: {model_path}")
        st.error(ex)

    st.sidebar.header("Image/Video Config")
    source_radio = st.sidebar.selectbox(
        "Select Source", settings.SOURCES_LIST)

    source_img = None
    # If image is selected
    if source_radio == settings.IMAGE:
        source_img = st.sidebar.file_uploader(
            "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

        col1, col2 = st.columns(2)

        with col1:
            try:
                if source_img is None:
                    default_image_path = str(settings.DEFAULT_IMAGE)
                    default_image = PIL.Image.open(default_image_path)
                    st.image(default_image_path, caption="Default Image",
                             use_column_width=True)
                else:
                    uploaded_image = PIL.Image.open(source_img)
                    st.image(source_img, caption="Uploaded Image",
                             use_column_width=True)
            except Exception as ex:
                st.error("Error occurred while opening the image.")
                st.error(ex)

        with col2:
            if source_img is None:
                default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
                default_detected_image = PIL.Image.open(
                    default_detected_image_path)
                st.image(default_detected_image_path, caption='Detected Image',
                         use_column_width=True)
            else:
                if st.sidebar.button('Detect Objects'):
                    res = model.predict(uploaded_image,
                                        conf=confidence
                                        )
                    boxes = res[0].boxes
                    res_plotted = res[0].plot()[:, :, ::-1]
                    st.image(res_plotted, caption='Detected Image',
                             use_column_width=True)
                    try:
                        with st.expander("Detection Results"):
                            for box in boxes:
                                st.write(box.data)
                    except Exception as ex:
                        # st.write(ex)
                        st.write("No image is uploaded yet!")

    elif source_radio == settings.VIDEO:
        video_options = list(settings.VIDEOS_DICT.keys())
        video_options.append("Upload Custom Video")

        selected_video = st.sidebar.selectbox("Select Video", video_options)

        if selected_video == "Upload Custom Video":
            custom_video = st.sidebar.file_uploader("Upload Custom Video", type=["mp4"])
            if custom_video is not None:
                # Save the uploaded custom video to the videos directory
                custom_video_path = settings.VIDEO_DIR / custom_video.name
                with open(custom_video_path, "wb") as f:
                    f.write(custom_video.getvalue())
                st.sidebar.success("Custom video uploaded successfully!")
                selected_video_path = custom_video_path
        else:
            selected_video_path = settings.VIDEOS_DICT[selected_video]

        if 'selected_video_path' in locals():
            if selected_video_path:
                helper.play_stored_video(confidence, model, selected_video_path)
        else:
            st.warning("Please select a video.")

    elif source_radio == settings.WEBCAM:
        helper.play_webcam(confidence, model)

    elif source_radio == settings.RTSP:
        helper.play_rtsp_stream(confidence, model)

    elif source_radio == settings.YOUTUBE:
        helper.play_youtube_video(confidence, model)

    else:
        st.error("Please select a valid source type!")

def about_page():
    st.title("About Auto-Harv")
    st.markdown(
        """
        Auto-Harv: An Automated Tomato Ripeness Detection System
        Auto-Harv is an advanced automated system designed to revolutionize tomato harvesting through cutting-edge technology. By integrating sophisticated algorithms and computer vision, Auto-Harv streamlines the process of identifying and harvesting ripe tomatoes based on their color, size, and texture. This innovative system enhances efficiency, reduces waste, and ensures optimal quality in tomato production.
        
        **Features:**
        - Tomato Detection: Utilizing state-of-the-art YOLOv8 object detection, Auto-Harv accurately identifies and locates tomatoes within a crop.
        - Ripeness Analysis: The system employs intricate color, size, and texture analysis to determine the ripeness of each detected tomato.
        - Automated Harvesting: Ripe tomatoes are swiftly and precisely harvested, enhancing productivity and reducing manual labor.
        - Efficient Workflow: With real-time processing, Auto-Harv optimizes the harvesting process, ensuring timely collection of ripe tomatoes.
        
        **Benefits:**
        - Enhanced Efficiency: Auto-Harv streamlines the tomato harvesting process, improving overall efficiency and reducing operational costs.
        - Reduced Waste: By selectively harvesting only ripe tomatoes, the system minimizes wastage and maximizes yield.
        - Improved Quality: Ripe tomatoes are harvested at the peak of freshness, maintaining superior quality and taste.
        - Data Insights: Auto-Harv provides valuable insights into crop ripeness trends, aiding in better decision-making for farmers.
        """
    )
    
# Setting page layout
st.set_page_config(
    page_title="AutoHarv",
    page_icon="🍅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
title_html = """
    <style>
    .title {
        text-align: center;
        color: #9BCF53; /* Custom color code */
    }
    </style>
    <h1 class="title">AutoHarv</h1>
    """

# Render the title with custom CSS
st.markdown(title_html, unsafe_allow_html=True)

# Create a dictionary to hold the pages

pages = {
    "Home": home_page,
    "About": about_page
}

# Sidebar navigation with dropdown
selected_page = st.sidebar.selectbox("Menu", list(pages.keys()))

# Render the selected page
pages[selected_page]()
