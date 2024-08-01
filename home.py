import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import requests


st.set_page_config(layout= 'wide')


with st.container():
    col_1, col_2, col_3, col_4, col_5 = st.columns([0.5, 1, 0.1, 2, 0.3], vertical_alignment="center")

    # # Anime Logo image ID
    # file_id = "1orIXAljsXcfTUM9qAoM54t58awgLb-L6"

    # # URL
    # url = f"https://drive.google.com/uc?export=view&id={file_id}"

    # response = requests.get(url)
    # col_2.image(response.content)

    col_2.image('Images/Anime_Profile_Logo.png')

    with col_4:
        st.write("""
    # My Portfolio Website
    ## Isaac Samuel
    ### Civil Engineer & Data Analyst
    """)


# Horizontal Bar Container
# -----------------------------------------------------------------------------------------------------------------------------------------------

with st.container():
    selected = option_menu(
        menu_title=None,
        options= ['About', 'Projects', 'Contacts'],
        icons= ['file-person', 'wrench-adjustable-circle', 'person-lines-fill'],
        orientation= 'horizontal'
    )

#  Selecting About Options 
# ------------------------------------------------------------------------------------------------------------------------------------------
if selected == 'About':
    col_1, col_2, col_3, col_4, col_5 = st.columns([0.5, 1, 0.1, 2, 0.3], vertical_alignment="top")

    with col_1:
        # st.image('https://drive.google.com/file/d/1eWUshUiePeYndhcbEZFjw2a0_lgflvGB/view?usp=sharing', use_column_width=True)
        st.image('Images/Anime_Profile_Logo.png')
    
    with col_2:

        with st.container():
            selected = option_menu(
                menu_title= None,
                options= ['Professional Bio', 'Education', 'Skills', 'Experience', 'Achievements', 'Future Plans'],
                icons= ['info-square-fill', 'backpack-fill', 'tools', 'stars', 'award-fill', 'lightbulb-fill']
            )
            # Professional Bio
            # ---------------------------------------------------------------------------------------------------
        if selected == 'Professional Bio':
            with col_4:
                col_x, col_xx, col_xxx = st.columns([1,2, 1])
                col_xx.subheader(':red[Professional Bio]') 
            with st.container():
                with col_4:
                    st.write("""
###### Isaac Samuel is a skilled web3 data analyst and reviewer at Flipside Crypto. With three years of experience in the field, he possesses professional-level skills in SQL, Python, and Microsoft Office tools, along with basic skills in Power BI, project management (DEXA certified), HTML, and CSS.
###### Isaac has achieved significant milestones in his career, including winning top place in an Arbitrum data analytics grant program challenge, where he showcased his comprehensive Streamlit analytics dashboard against several top web3 analysts. He has also secured top place in Uniswap's analytics monthly contest and has earned multiple top 3 rankings. His expertise and contributions have led to him being appointed as a reviewer at Flipside Crypto, a leading web3 analytics and data provider.
###### Currently enrolled in the ALX data analytics program, Isaac's ambition to enhance his analytical skills continues to grow. He is also pursuing a Master's in Data Analytics and aspires to work on innovative projects like Seoul's Brain project, an AI model designed to solve traffic congestion problems.
###### Isaac Samuel is dedicated to leveraging his data expertise to drive impactful solutions and is always eager to embrace new challenges in the ever-evolving field of data analytics.
""")
            # Education
            # ---------------------------------------------------------------------------------------------------
        if selected == 'Education':                
            with col_4:
                col_x, col_xx, col_xxx = st.columns([1,2, 1])
                col_xx.subheader(':red[INSTITUTIONS]')

                st.write("""

#### :blue[B.Eng, Federal University of Technology, Minna]
##### 2023, Second Class (Upper Division)  
                         
""")
                
                col_x, col_xx, col_xxx = st.columns([1,2, 1])
                col_xx.subheader(':red[PROFESSIONAL COURSES]')
                st.write("""

#### :blue[DEXA Project Management Course]
                         
""")
                
            # Skills
            # ---------------------------------------------------------------------------------------------------
        if selected == 'Skills':                
            with col_4:
                col_x, col_xx, col_xxx = st.columns([1,2, 1])
                col_xx.subheader(':red[SKILLS]')

                st.write("""

- SQL
- Python
- Microsoft Office Tools (Excel, Word, PowerPoint)
- Google Office Tools
- Power BI
- Basic knowledge of HTML, CSS, and project management 
                         
""")
                
            # Experience
            # ---------------------------------------------------------------------------------------------------
        if selected == 'Experience':   
            with col_4:
                st.write("""

### 👨🏻‍💻:blue[Data Analyst]
##### Flipside Crypto, 🚩Remote
##### 📅2022 - Present
- Shipped high-quality analytics using advanced SQL skills to query datasets, clean data, create visualizations, and represent findings in dashboards.
- Reviewed the work of new and veteran analysts to ensure quality and adherence to company standards.
- Participated in several contests, earning top places.

### 👷🏻‍♂️:blue[Civil Engineer (Internship)]
##### Ministry of Works, 🚩Minna
##### 📅2021 - 2022
- Supervised daily site activities and ensured adherence to standards and specifications.
- Managed the construction project of a road, overseeing tasks from land clearing to subbase laying.

                         
""")
                
            # Achievements
            # ---------------------------------------------------------------------------------------------------
        if selected == 'Achievements':   
            with col_4:
        # Google Slide Presentation
                components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vTG84OHSDxfiI5lupByc-gDRLOGgnVJMQi97035v_zjvsrywpUkMjh4FoRaZsg4GGC4v5Bmw0cjtvx6/embed?start=true&loop=true&delayms=5000", height=430)

            # Future Plans
            # ---------------------------------------------------------------------------------------------------
        if selected == 'Future Plans': 
            with col_4:
                col_x, col_xx, col_xxx = st.columns([1,2, 1])
                col_xx.subheader(':red[GOALS AND ASPIRATIONS]')  
            with col_4:
                st.write("""

- Currently enrolled in the ALX data analytics program to enhance analytics skills.
- Pursuing a Master's in Data Analytics.
- Aspires to work on innovative projects like Seoul's Brain, an AI model designed to solve traffic congestion problems.

""")


#  Selecting Projects Options 
# ------------------------------------------------------------------------------------------------------------------------------------------
if selected == 'Projects':
    st.write("""
## Projects
""")



#  Selecting Contacts Options 
# ------------------------------------------------------------------------------------------------------------------------------------------
if selected == 'Contacts':
    st.write("""
## Contacts
""")
    with st.container():
    # col_1, col_2, col_3, col_4, col_5 = st.columns([2, 0.1, 2, 0.1, 2], vertical_alignment= 'top')
        col_1, col_2, col_3 = st.columns(3, gap= 'medium', vertical_alignment= 'top')
        col_1.write("""
    #### 📧Email: 234isaacsamuel@gmail.com
    """)
        col_1.write("""
    ### ☎️ Phone No: 07087212243
    """)
        
        col_2.write("""
    ### ⬢ [Flipsidecrypto](https://flipsidecrypto.xyz/zackmendel/dashboards)
    """)
        col_2.write("""
    ### 🇮🇳 [Linkedin](https://www.linkedin.com/in/zackmendel/)
    """)
        
        col_3.write("""
    ### ✖ Twitter(X): [@zackmendel_](https://x.com/Zackmendel_)
    """)
        col_3.write("""
    ### 🧊 Medium: [Isaacsamuel](https://medium.com/@samuelisaac1995/tracking-the-impact-of-eip-4844-a-deep-dive-into-blob-transactions-on-ethereum-2902b4d096da)
    """)
        

        
