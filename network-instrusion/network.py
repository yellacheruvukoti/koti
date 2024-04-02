import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
Networkinstrusion_model = pickle.load(open('C:/Users/Dodda.Madhu/Downloads/network-instrusion/network-instrusion/network.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Network intrusion detection using ML',
                          ['Home'],
                          default_index=0)

# Network intrusion detection Page
if selected == 'Home':
    # page title
    st.title('Network intrusion detection using ML')
    st.image("download1.jpg")

    # getting the input data from the user
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

    with col1:
        Destination_Port = st.text_input('Destination Port')

    with col2:
        Flow_Duration = st.text_input('Flow Duration')

    with col3:
        Total_Fwd_Packets = st.text_input('Total Fwd Packets')

    with col4:
        FIN_Flag_Count = st.text_input('FIN Flag Count')

    with col5:
        SYN_Flag_Count = st.text_input('SYN Flag Count')

    with col6:
        RST_Flag_Count = st.text_input('RST Flag Count')

    with col7:
        PSH_Flag_Count = st.text_input('PSH Flag Count')

    with col8:
        ACK_Flag_Count = st.text_input('ACK Flag Count')

    with col9:
        URG_Flag_Count = st.text_input('URG Flag Count')

    with col1:
        CWE_Flag_Count = st.text_input('CWE Flag Count')

    with col2:
        ECE_Flag_Count = st.text_input('ECE Flag Count')

    with col3:
        Down_Up_Ratio = st.text_input('Down/Up Ratio')

    with col4:
        Average_Packet_Size = st.text_input('Average Packet Size')

    with col5:
        Active_Std = st.text_input('Active Std')

    with col6:
        Active_Max = st.text_input('Active Max')

    with col7:
        Active_Min = st.text_input('Active Min')

    with col8:
        Idle_Mean = st.text_input('Idle Mean')

    with col9:
        Idle_Std = st.text_input('Idle Std')

    with col1:
        Idle_Max = st.text_input('Idle Max')

    with col2:
        Idle_Min = st.text_input('Idle Min')

    # code for Prediction
    Networkinstrusion_prediction = ''

    # creating a button for Prediction
    if st.button('Network intrusion detection Result'):
        # Use the user input for model prediction
        user_input = [Destination_Port, Flow_Duration, Total_Fwd_Packets, FIN_Flag_Count, SYN_Flag_Count, RST_Flag_Count,
                      PSH_Flag_Count, ACK_Flag_Count, URG_Flag_Count, CWE_Flag_Count, ECE_Flag_Count, Down_Up_Ratio,
                      Average_Packet_Size, Active_Std, Active_Max, Active_Min, Idle_Mean, Idle_Std, Idle_Max, Idle_Min]
        Networkinstrusion_prediction = Networkinstrusion_model.predict([user_input])
        st.success('The output is {}'.format(Networkinstrusion_prediction))

if st.button("About"):
    st.text("Let's Learn")
    st.text("Built with Streamlit")
