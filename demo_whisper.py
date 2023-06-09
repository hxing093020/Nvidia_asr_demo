from pathlib import Path 
import streamlit as st


wavFiles = []
wavFiles.append('DCA_se2_ag1_f_02_1_1141.5556_1142.7307_concat.wav')
wavFiles.append('DCA_se2_ag1_f_02_1_1289.9732_1290.4721_concat.wav')
wavFiles.append('DCA_se2_ag1_f_03_1_591.811_592.8715_concat.wav')
wavFiles.append('DCA_se2_ag1_m_01_1_637.5601_639.6211_concat.wav')
wavFiles.append('DCA_se2_ag1_m_01_1_863.5791_866.7312_concat.wav')
wavFiles.append('CH112_35.adc.wav')
wavFiles.append('CH112_43.adc.wav')
wavFiles.append('CH113_44.adc.wav')
wavFiles.append('CH115_53.adc.wav')
wavFiles.append('CH119_49.adc.wav')

GT = []
GT.append('and right in the middle, i forgot where that one was from')
GT.append('i mean they got all this you know they do not know they do not know what to do with it')
GT.append('huh, the principal or the teacher, the teacher. oh, we used to talk a lot, and one  one of our teachers you know')
GT.append('you know jumps up in the window on the screen, runs back down you know, runs all the time')
GT.append('what about the best teacher you ever had can you remember who that would be')
GT.append('美国前参议员米切尔和谈主席')
GT.append('阿拉伯首脑会议在即')
GT.append('大多数代表认为在北约东扩的情况下必须向所有国家提供平等的安全保障')
GT.append('哥伦比亚谴责美干涉其内政')
GT.append('今后两国关系还将继续向前发展')

PT = []
PT.append('and right in the middle, :red[and] got one :red[of them]')
PT.append(':red[amen (they got)] all this you know :red[(they do not know)] they do not know what to do with it')
PT.append(':red[thank you, i will take a little nap. the future, out,] we used to talk a lot, and :red[when i am about to teach it no]')
PT.append('you know :red[jabs] up in the window on the screen, runs back down :red[(you know), he reminds me a lot of] time')
PT.append('what about the best teacher you ever had :red[(can you remember who that would be)]')
PT.append('美国:red[千菜园]米切尔:red[河潭]主席')
PT.append('阿拉伯:red[松]脑会议再:red[见]')
PT.append('大:red[的时候]代表认为在北约:red[灯阔]的情况下必须向所有国家提供平等的安全保障')
PT.append('哥伦比亚谴责美:red[甘塞]其内政')
PT.append('今后两:red[个]关系还:red[在]继续向前发展')

FT = []
FT.append('and right in the middle, i forgot where that one was from')
FT.append('i mean they got all :red[is] you know they do not know they do not know what to do with it')
FT.append('huh, the principal or the teacher, the teacher, oh, we used to talk a lot, and one  one of :red[the my] teachers you know')
FT.append('you know jumps up in the window on the screen, runs back down you know, runs all the time')
FT.append('what about the best teacher you ever had can you remember who that would be')
FT.append('美国前参议员米切尔和谈主席')
FT.append('阿拉伯首脑会议在即')
FT.append('大:red[致上]代表:red[论]为在北约东扩的情况下必须向所有国家提供平等的安全保障')
FT.append('哥伦比亚谴责美干涉其内政')
FT.append('今后两国关系还将继续向前发展')

LAN = []
LAN.append('AAE')
LAN.append('AAE')
LAN.append('AAE')
LAN.append('AAE')
LAN.append('AAE')
LAN.append('Chinese')
LAN.append('Chinese')
LAN.append('Chinese')
LAN.append('Chinese')
LAN.append('Chinese')
st.set_page_config(layout='wide')

logo_image = "logo.png"
st.image(logo_image, width=200)

st.markdown("<h3 style='text-align: center;'>Demo of fine-tuning  Whisper ASR model</h3>", unsafe_allow_html=True)
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()
intro_markdown = read_markdown_file("introduction_whisper.md")
st.markdown(intro_markdown, unsafe_allow_html=True)

st.markdown('---')
col1, col2, col3, col4, col5 = st.columns(5)


col1.markdown("<h5 style='text-align: center;'>Audio</h5>", unsafe_allow_html=True)
col2.markdown("<h5 style='text-align: center;'>Ground Truth</h5>", unsafe_allow_html=True)
col3.markdown("<h5 style='text-align: center;'>Whisper Pre-trained Model</h5>", unsafe_allow_html=True)
col4.markdown("<h5 style='text-align: center;'>Appen Fine-tuned Model</h5>", unsafe_allow_html=True)
col5.markdown("<h5 style='text-align: center;'>Language/Accent</h5>", unsafe_allow_html=True)
st.markdown("___")

for ind in range(len(wavFiles)):
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.audio('samples_whisper/'+ wavFiles[ind], format='audio/wav')
    col2.markdown(GT[ind], unsafe_allow_html=True)
    col3.markdown(PT[ind], unsafe_allow_html=True)
    col4.markdown(FT[ind], unsafe_allow_html=True)
    col5.markdown(LAN[ind], unsafe_allow_html=True)
    st.markdown("---")

