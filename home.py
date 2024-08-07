import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import time
from st_social_media_links import SocialMediaIcons


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

#     with col_5:
#         social_media_links = [
#     "https://www.facebook.com/ThisIsAnExampleLink",
#     "https://www.youtube.com/ThisIsAnExampleLink",
#     "https://www.instagram.com/ThisIsAnExampleLink",
#     "https://www.github.com/jlnetosci/st-social-media-links",
#     "https://x.com/Zackmendel_",
#     "https://flipsidecrypto.xyz/zackmendel/dashboards"
#     "234isaacsamuel@gmail.com"
# ]

#         social_media_icons = SocialMediaIcons(social_media_links)

#         social_media_icons.render()


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

        with st.container(border=True):
            selected = option_menu(
                menu_title= None,
                options= ['Professional Bio', 'Education', 'Skills', 'Experience', 'Achievements', 'Future Plans'],
                icons= ['info-square-fill', 'backpack-fill', 'tools', 'stars', 'award-fill', 'lightbulb-fill']
            )
            # Professional Bio
            # ---------------------------------------------------------------------------------------------------
        if selected == 'Professional Bio':

            with col_4:
                with st.container(border=True):
                    col_x, col_xx, col_xxx = st.columns([1.5, 2, 1])
                    col_xx.subheader(':red[Professional Bio]') 
                    
    #                     st.write("""
    # ###### Isaac Samuel is a skilled web3 data analyst and reviewer at Flipside Crypto. With three years of experience in the field, he possesses professional-level skills in SQL, Python, and Microsoft Office tools, along with basic skills in Power BI, project management (DEXA certified), HTML, and CSS.
    # ###### Isaac has achieved significant milestones in his career, including winning top place in an Arbitrum data analytics grant program challenge, where he showcased his comprehensive Streamlit analytics dashboard against several top web3 analysts. He has also secured top place in Uniswap's analytics monthly contest and has earned multiple top 3 rankings. His expertise and contributions have led to him being appointed as a reviewer at Flipside Crypto, a leading web3 analytics and data provider.
    # ###### Currently enrolled in the ALX data analytics program, Isaac's ambition to enhance his analytical skills continues to grow. He is also pursuing a Master's in Data Analytics and aspires to work on innovative projects like Seoul's Brain project, an AI model designed to solve traffic congestion problems.
    # ###### Isaac Samuel is dedicated to leveraging his data expertise to drive impactful solutions and is always eager to embrace new challenges in the ever-evolving field of data analytics.
    # """)
                        
                    streams = """
    ###### Isaac Samuel is a skilled web3 data analyst and reviewer at Flipside Crypto. With three years of experience in the field, he possesses professional-level skills in SQL, Python, and Microsoft Office tools, along with basic skills in Power BI, project management (DEXA certified), HTML, and CSS.
    ###### Isaac has achieved significant milestones in his career, including winning top place in an Arbitrum data analytics grant program challenge, where he showcased his comprehensive Streamlit analytics dashboard against several top web3 analysts. He has also secured top place in Uniswap's analytics monthly contest and has earned multiple top 3 rankings. His expertise and contributions have led to him being appointed as a reviewer at Flipside Crypto, a leading web3 analytics and data provider.
    ###### Currently enrolled in the ALX data analytics program, Isaac's ambition to enhance his analytical skills continues to grow. He is also pursuing a Master's in Data Analytics and aspires to work on innovative projects like Seoul's Brain project, an AI model designed to solve traffic congestion problems.
    ###### Isaac Samuel is dedicated to leveraging his data expertise to drive impactful solutions and is always eager to embrace new challenges in the ever-evolving field of data analytics.
    """
                        
                    def stream_data():
                            for word in streams.split(" "):
                                yield word + " "
                                time.sleep(0.07)

                    st.write_stream(stream_data)

                    



            # Education
            # ---------------------------------------------------------------------------------------------------
        if selected == 'Education':                
            with col_4:
                with st.container(border=True):
                    col_x, col_xx, col_xxx = st.columns([1,2, 1])
                    col_xx.subheader(':red[INSTITUTIONS]')

                    st.write("""

#### :blue[B.Eng, Federal University of Technology, Minna]
##### 2023, Second Class (Upper Division)  
                         
""")
                with st.container(border=True, height= 300):
                
                    col_x, col_xx, col_xxx = st.columns([1,2, 1])
                    col_xx.subheader(':red[PROFESSIONAL COURSES]')
                    st.write("""

- #### :blue[DEXA Project Management Course], 
    - ######    @:green[DEXA],
- #### :blue[Data Storytelling with Microsoft PowerBI], 
    - ######   @:green[Side Hustle],
- #### :blue[Data Analysis Internship], 
    - ######   @:green[MetricsDAO],
- #### :blue[Data Analysis(Beginners Guide)], 
    - ######   @:green[Flipsidecrypto]

                         
""")
                
            # Skills
            # ---------------------------------------------------------------------------------------------------
        if selected == 'Skills':                
            with col_4:
                with st.container(border=True, height=360):
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
                with st.container(border=True, height=360):
                    col_x, col_xx, col_xxx = st.columns([0.8, 2, 0.5])
                    col_xx.subheader(':red[GOALS AND ASPIRATIONS]')  
            
                    st.write("""

- Currently enrolled in the ALX data analytics program to enhance analytics skills.
- Pursuing a Master's in Data Analytics.
- Aspires to work on innovative projects like Seoul's Brain, an AI model designed to solve traffic congestion problems.

""")


#  Selecting Projects Options 
# ------------------------------------------------------------------------------------------------------------------------------------------
if selected == 'Projects':

    # EIP-4844 Blob Megadashboard
    # -------------------------------------------------------------------------------------------------------------------------------

    with st.container(border= True):
        col_1, col_2, col_3 = st.columns([3, 1.9, 1.7], gap= 'medium', vertical_alignment="top")
        with col_1:
            col_x, col_xx = st.columns([0.5, 3], gap= 'medium', vertical_alignment="top")
            with col_x:
                with st.container(border= True, height=70):
                    st.markdown('### 1️⃣')

            with col_xx:
                with st.container(border= True, height=70):
                    # col_x, col_xx, col_xxx = st.columns([0.4, 4, 1], gap= 'medium', vertical_alignment="top")
                    # col_a.header(':red[1.]')
                    st.markdown('### :red[EIP-4844 Blob Megadashboard] [🔗](https://flipsidecrypto.xyz/zackmendel/eip-4844-blob-megadashboard-1e6Rzd)')

            with st.container(border= True, height=315):
                st.markdown("""
    he recent Dencun upgrade(March 13)to the Ethereum network has ushered in a transformative change with the activation of EIP-4844, also known as Shard Blob Transactions. This Ethereum Improvement Proposal introduces a novel transaction type designed to enhance the scalability and efficiency of the Ethereum blockchain, paving the way for broader adoption and innovation within the ecosystem.

    :blue[This dashboard tracks important metrics about Blobs using on-chain metrics.]
    """)


        with col_2:                      
            with st.container(border= True, height=400):
                help_text = """
    This dashboard tracks important metrics about Blobs using on-chain metrics.
    """
                textt = """
    The recent Dencun upgrade(March 13)to the Ethereum network has ushered in a transformative change with the activation of EIP-4844, also known as Shard Blob Transactions. This Ethereum Improvement Proposal introduces a novel transaction type designed to enhance the scalability and efficiency of the Ethereum blockchain, paving the way for broader adoption and innovation within the ecosystem.

    :blue[This dashboard tracks important metrics about Blobs using on-chain metrics.]
    """
                st.link_button("Flipside Dashboard", "https://flipsidecrypto.xyz/zackmendel/eip-4844-blob-megadashboard-1e6Rzd", help= help_text, use_container_width=True)
                st.image('Images/EIP_4844_Blob Megadashboard_copy.png')
                # with st.expander('Summary'):
                #     st.write(textt)


        with col_3:
            with st.container(border= True, height=400):
                st.link_button("Twitter(X) Thread", "https://x.com/Zackmendel_/status/1800495312651575369", help= help_text, use_container_width=True)
                # Enbed Twitter(X) Thread
                components.html('<blockquote class="twitter-tweet"><p lang="en" dir="ltr">1/ 🧵Analyzing the impact of EIP-4844 blobs on <a href="https://twitter.com/ethereum?ref_src=twsrc%5Etfw">@ethereum</a> Layer 2 solutions! 🚀<br><br>We compared blob submitters (Arbitrum , Base , Blast, Optimism ) with non-blob submitters (Polygon , Avalanche , BSC ).<br><br>Thanks to <a href="https://twitter.com/flipsidecrypto?ref_src=twsrc%5Etfw">@flipsidecrypto</a> for the data! 📊✨<br><br>Here are the key findings. 📊 <a href="https://t.co/N3RLYa6qYS">pic.twitter.com/N3RLYa6qYS</a></p>&mdash; Samuel Isaac (@Zackmendel_) <a href="https://twitter.com/Zackmendel_/status/1800495312651575369?ref_src=twsrc%5Etfw">June 11, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>', scrolling= True, height=300)


    # 🦄 User Behaviour on Fee Changes
    # -------------------------------------------------------------------------------------------------------------------------------

    with st.container(border= True):
        col_1, col_2, col_3 = st.columns([3, 1.9, 1.7], gap= 'medium', vertical_alignment="top")
        with col_1:
            col_x, col_xx = st.columns([0.5, 3], gap= 'medium', vertical_alignment="top")
            with col_x:
                with st.container(border= True, height=70):
                    st.markdown('### 2️⃣')

            with col_xx:
                with st.container(border= True, height=70):
                    # col_x, col_xx, col_xxx = st.columns([0.4, 4, 1], gap= 'medium', vertical_alignment="top")
                    # col_a.header(':red[1.]')
                    st.markdown('### :red[🦄 User Behaviour on Fee Changes] [🔗](https://flipsidecrypto.xyz/zackmendel/user-behaviour-on-fee-changes-bl3gow)')

            with st.container(border= True, height=315):
                st.markdown("""
 In recent months, Uniswap Labs has made significant changes to its fee structure, impacting users of its frontend interface. Initially, in October, a 0.15% fee was introduced for those using the Uniswap frontend (Link). This fee was further increased to 0.25% in April (Link). These changes have sparked discussions and analyses regarding their impact on Uniswap's overall performance and user behavior.

This analysis aims to delve into the effects of these fee changes on Uniswap's trading volume, user base, and swap activity. Key questions include whether the fee introduction and subsequent increase led to a decrease in the usage of the Uniswap Labs frontend, and if so, what alternatives users turned to. Additionally, the analysis will explore any noticeable differences in behavior between different user groups, such as whales versus smaller traders.

The following sections present the findings of this analysis, providing insights into the impact of the fee changes and offering recommendations based on the observed trends and data.

NOTE: The networks used for this analysis are: Ethereum, Polygon, Optimism, Arbitrum One, Base, Avalanche and Blast
    """)


        with col_2:                      
            with st.container(border= True, height=400):
                help_text = """
    The analysis indicates that Uniswap's fee hikes have not significantly deterred user activity, with trading volumes and user retention remaining robust. However, market conditions play a substantial role in user behavior.
    """
                st.link_button("Flipside Dashboard", "https://flipsidecrypto.xyz/zackmendel/user-behaviour-on-fee-changes-bl3gow", help= help_text, use_container_width=True)
                st.image('Images/EIP_4844_Blob Megadashboard_copy.png')


        with col_3:
            with st.container(border= True, height=400):
                st.link_button("Twitter(X) Thread", "https://x.com/Zackmendel_/status/1814316656300011810", help= help_text, use_container_width=True)
                # Enbed Twitter(X) Thread
                components.html('<blockquote class="twitter-tweet"><p lang="en" dir="ltr">🧵 Thread: The Impact of Uniswap&#39;s Fee Changes 🧵<br><br>1/ Uniswap introduced a 0.15% interface fee in October, later increased to 0.25% in April. Since the first hike, Uniswap generated $747.5M from a $370.8B volume with 104.5M swaps on Arbitrum, Avalanche, BSC, Base, Ethereum,… <a href="https://t.co/zRBovn4k8I">pic.twitter.com/zRBovn4k8I</a></p>&mdash; Samuel Isaac (@Zackmendel_) <a href="https://twitter.com/Zackmendel_/status/1814316656300011810?ref_src=twsrc%5Etfw">July 19, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>', scrolling= True, height=300)




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
        

        
