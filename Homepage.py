import streamlit as st

st.set_page_config(
    page_title="Engineering Horizons",
    layout="wide",
    page_icon="💻",
)

with open("main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open("index.html") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

st.markdown("---")
st.subheader("About the Blog")
st.write("""
Hi, I’m Louie Abao, a 20-year-old Computer Engineering student at Surigao State University. 
This blog is my space to share the exciting, sometimes overwhelming, and always rewarding journey of navigating technology, innovation, 
and the challenges of being a young engineer.  

Growing up close to nature, I’ve always been fascinated by how technology can harmonize with the environment to create sustainable solutions. 
Here, I’ll share personal stories, projects I’m working on, and insights on balancing the drive to achieve with the need to stay grounded. 
Let’s learn, innovate, and grow together!
""")

st.markdown("---")
st.subheader("Latest Post: 'Why Every Engineer Needs to Take a Break (And How to Do It)'")
st.markdown("**December 2, 2024**")
st.write("""
If you’re anything like me, you’ve probably spent countless late nights debugging code, tweaking projects, or researching for that next big idea. 
But somewhere along the way, we forget that rest isn’t just a luxury—it’s a necessity.  

In this post, I’m diving into:  
1. The science of why rest makes us better engineers  
2. Practical tips for unplugging when your mind won’t stop racing  
3. How nature inspired some of my favorite ideas (spoiler: stepping outside works wonders)  

Take it from someone who’s been there: you’re not slacking off by taking a break. You’re recharging to come back stronger.  
""")

st.markdown("---")
st.subheader("Reader Comments:")

comments = [
    ("Minnie", "Dec 2, 2024", "This resonates with me so much, Louie. Nature always helps me reset too!"),
    ("Alex", "Dec 2, 2024", "I needed to hear this today. Time to step away from my screen for a bit."),
    ("Jamie", "Dec 2, 2024", "Please write more about balancing tech and life—I love your insights!")
]

for name, date, comment in comments:
    st.write(f"**{name}** ({date}): {comment}")

st.sidebar.success("Select pages above")
