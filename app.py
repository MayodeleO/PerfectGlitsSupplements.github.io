from distutils.command.clean import clean
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon="tada:", layout="wide")

def load_lottieur1(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
img_ultraclean = Image.open("images/ultraclean.png")
img_cardiovax = Image.open("images/cardiovax.png")
img_ifocus = Image.open("images/ifocus.png")
img_Longjack = Image.open("images/Longjack.png")
img_Arthrazex = Image.open("images/Arthrazex.png")
img_Normatone = Image.open("images/Normatone.png")
img_Express = Image.open("images/Express.png")
img_Cardioton = Image.open("images/Cardioton.png")
img_Pro = Image.open("images/Pro.png")



# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
  
# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Blessing :wave:")
    st.title("A Supplement agent From Nigeria")
    st.write("We sell organic suppliments to boost your lifestyle.")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Perfect Glits Supplement, we sell natural organic suppliments like:
            - Cardiovax.
            - Arthrazex balm.
            - Normatone.
            - Longjack XXXL.
            - Pro Herbarium.
            - Express fat burner.
            - Cardioton.
            - Ultra clean.
            - Ifocus 
           
            If this sounds interesting to you, please call/chat +2348120087013 or like and follow on jiji.
            """
        )
        st.write("[Jiji Account >](https://jiji.ng/shop/perfectglits.com)")
        st.write(
            """
            Message on whatsapp to buy using the link below
            """
        )
        st.write("[Whatsapp Business>]( https://wa.me/message/CA4BC2R4STPRK1)")
    
# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Supplements")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_ultraclean)
    with text_column:
        st.subheader("Ultraclean Premium detox")
        st.write(
            """
            A breakthrough wellness solution harnessing cutting-edge technology for unparalleled purity.
            Boost your vitality with scientifically refined ingredients, meticulously selected to promote holistic health.
            Experience the transformative power of UltraClean and elevate your well-being to new heights.
            
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_cardiovax)
    with text_column:
        st.subheader("Cardiovax")
        st.write(
            """
            Your path to a healthier heart through advanced cardiovascular support. 
            Harnessing natural ingredients and modern science, Cardiovax offers a holistic solution for maintaining optimal heart function. 
            Experience vitality and well-being as you prioritize your cardiovascular health with Cardiovax's specialized formula. 
            Elevate your heart health journey today."
            
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_ifocus)
    with text_column:
        st.subheader("Ifocus")
        st.write(
            """
            A cutting-edge cognitive support supplement designed to unlock your mental potential. Harnessing a blend of proven ingredients and neuro-optimization, iFocus empowers sharper focus, memory, and mental clarity.
            Elevate your productivity and cognitive vitality with iFocus, your partner in achieving mental brilliance.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_Longjack)
    with text_column:
        st.subheader("Longjack XXXL")
        st.write( 
            """
        A Natural Performance Enhancer.
        Longjack, derived from a traditional herb, offers a boost in stamina, energy, and overall vitality. 
        Harness the power of nature to elevate physical and mental performance. 
        Experience heightened well-being and confidence with Longjack's natural support.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_Arthrazex)
    with text_column:
        st.subheader("Arthrazex Balm")
        st.write(
            """
        Arthrazex balm is a topical solution designed to alleviate joint and muscle discomfort.
        Infused with natural ingredients, it aims to provide soothing relief and improve mobility.
        Its formula targets inflammation and promotes relaxation, offering a potential option for managing minor aches and pains. 
        However, individual results may vary, and consulting a healthcare professional is advised before use.
           """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_Normatone)
    with text_column:
        st.subheader("Normatone")
        st.write(
            """
        Normatone is a dietary supplement claimed to support healthy blood sugar levels. 
        It combines a blend of natural ingredients, including herbs and vitamins, thought to aid in glucose metabolism.         
        The supplement aims to promote insulin sensitivity and overall metabolic wellness. 
        As with any supplement, it's important to consult a healthcare provider before incorporating Normatone into your regimen, especially if you have underlying health conditions or are taking medications.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_Express)
    with text_column:
        st.subheader("Express Fat Burner")
        st.write(
            """
        Express Fat Burner is a dietary supplement aimed at supporting weight management and fat loss. 
        It typically contains a combination of natural ingredients like herbs, vitamins, and minerals that are believed to boost metabolism and energy levels. 
        The supplement may aid in increasing calorie expenditure and promoting the body's fat-burning processes. 
        However, individual results can vary, and it's important to consult a healthcare professional before using any weight loss supplement.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_Cardioton)
    with text_column:
        st.subheader("Cardioton")
        st.write(
            """
    Cardioton is a dietary supplement formulated to potentially support heart health. 
    It often includes a blend of herbs, antioxidants, and nutrients thought to promote cardiovascular wellness. 
    The supplement aims to maintain healthy blood pressure, cholesterol levels, and overall heart function. 
    As with any health product, consulting a medical professional before incorporating Cardioton into your routine is recommended, especially if you have pre-existing heart conditions or are taking medications.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_Pro)
    with text_column:
        st.subheader("Pro Herbarium")
        st.write(
            """
    Pro Herbarium" dietary supplement is a product designed to potentially support overall health and well-being. 
    Infused with a blend of herbal extracts, vitamins, and minerals, it aims to provide nutritional benefits and enhance bodily functions. 
    This supplement may promote various health aspects, such as energy levels, immunity, and digestion. 
    As with any dietary supplement, it's advisable to consult a healthcare professional before use, especially if you have specific health concerns or are taking other medications.
            """
        )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!") 
    st.write("##")

    # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/seuntracey@gmail.com" method="POST">
        <input type="hidden" name"_captcha" value="true">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
