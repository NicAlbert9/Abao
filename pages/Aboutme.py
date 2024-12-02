import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Overthinking Out Loud",
    page_icon="📜",
)

img=Image.open('./assets/Ky.png')

col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(img, width=230)

with col2:
    st.title('Louie Abao', anchor=False)
    st.write('I am Louie Abao 20 y/o, I am currently studying in SNSU as a Computer Engineering Student.')


st.write("\n\n")
st.subheader("Short Discription About me:")
st.write(
    """
    Hi, I’m Louie Abao, a 20-year-old Computer Engineering student at Surigao State University. Passionate about technology and problem-solving, I’m dedicated to mastering the intricacies of computer systems and software development.

I’ve always loved exploring the intersection of innovation and creativity, whether it’s programming web applications, delving into research projects, or tackling real-world challenges. Growing up close to nature, I also appreciate the harmony between technology and the environment, and I strive to develop solutions that are sustainable and impactful.

In my free time, I enjoy learning new skills, diving into thought-provoking anime, and creating meaningful connections with others. My goal is to contribute to advancements in the tech world while making a positive difference in the lives of people and the planet.

""")

st.sidebar.success("Select pages above")