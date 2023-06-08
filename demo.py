from pathlib import Path 
import streamlit as st


wavFiles = []
wavFiles.append('77d369396a6a567cc0f3059670d1f7ab.wav')
wavFiles.append('sample4.wav')
wavFiles.append('sample3.wav')
wavFiles.append('sample5.wav')
wavFiles.append('9d76cc4b9340b217152540be8afedbb7.wav')
wavFiles.append('0fe4fd7f8b394c863269bc87f81b9e7b.wav')
wavFiles.append('affed74c3b93602385f6d52ba9076dee.wav')
wavFiles.append('cadc501bf659b6c487aa6f692552e317.wav')
wavFiles.append('sample9.wav')
wavFiles.append('002db9b7bcb5f07f783de39d04cdd479.wav')

GT = []
GT.append('the vehicle does start and drive')
GT.append('would you like cream and sugar')
GT.append('okay and what\'s the code')
GT.append('uh no not just regular')
GT.append('people love me')
GT.append('the covid pandemic it reiterated to me')
GT.append('today only about eleven percent of federal it systems are running in the cloud')
GT.append('even nuclear weapons are only about one percent efficient chemical weapons are a tiny fraction of a percent in terms of their efficiency')
GT.append('i know what that is i just don\'t know what items you wanted')
GT.append('he said jim your company')

PT = []
PT.append(':red[it\'ll be a good bus store] and drive')
PT.append('the :red[gds why you make sure]')
PT.append('okay and :red[wolstter] code')
PT.append('uh no no :red[that\'s very go]')
PT.append(':red[ple birthday]')
PT.append('the :red[coid] pandemic it reiterated to me')
PT.append(':red[to day] only about eleven :red[per cent] of federal it :red[t] systems are running in the cloud')
PT.append('even nuclear weapons are only about :red[oneer] efficient chemical weapons are a tiny fraction of a :red[perc] in terms of their efficiency')
PT.append('i know what that is i just don\'t know what :red[ei dont] you :red[want it]')
PT.append(':red[it\'s a] jam your company')

FT = []
FT.append('the vehicle does start and drive')
FT.append('would you like cream and sugar')
FT.append('okay and what\'s the code')
FT.append(':red[(uh)] no not just regular')
FT.append('people love me')
FT.append('the covid pandemic it reiterated to me')
FT.append('today only about eleven percent of federal it systems are running in the cloud')
FT.append('even nuclear weapons are only about one percent efficient chemical weapons are a tiny fraction of a percent in terms of their efficiency')
FT.append('i know what that is i just don\'t know what items you wanted')
FT.append('he said jim your company')



st.set_page_config(layout='wide')

logo_image = "logo.png"
st.image(logo_image, width=200)

st.markdown("<h3 style='text-align: center;'>Demo of fine-tuning Nvidia ASR model</h3>", unsafe_allow_html=True)
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()
intro_markdown = read_markdown_file("introduction.md")
st.markdown(intro_markdown, unsafe_allow_html=True)

st.markdown('---')
col1, col2, col3, col4 = st.columns(4)


col1.markdown("<h4 style='text-align: center;'>Audio</h4>", unsafe_allow_html=True)
col2.markdown("<h4 style='text-align: center;'>Ground Truth</h4>", unsafe_allow_html=True)
col3.markdown("<h4 style='text-align: center;'>Nvidia Pre-trained Model\n\n (WER=7.8%)</h4>", unsafe_allow_html=True)
col4.markdown("<h4 style='text-align: center;'>Fine-tuned with Appen Dataset \n\n (WER=6.5%)</h4>", unsafe_allow_html=True)
st.markdown("___")

for ind in range(len(wavFiles)):
    col1, col2, col3, col4 = st.columns(4)
    col1.audio('samples/'+ wavFiles[ind], format='audio/wav')
    col2.markdown(GT[ind], unsafe_allow_html=True)
    col3.markdown(PT[ind], unsafe_allow_html=True)
    col4.markdown(FT[ind], unsafe_allow_html=True)
    st.markdown("---")

