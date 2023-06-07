from pathlib import Path 
import streamlit as st


wavFiles = []
wavFiles.append('77d369396a6a567cc0f3059670d1f7ab.wav')
wavFiles.append('sample4.wav')
wavFiles.append('sample8.wav')
wavFiles.append('sample3.wav')
wavFiles.append('sample5.wav')
wavFiles.append('sample1.wav')
wavFiles.append('90b4fb9ce4042d84b8ddc6e0c8bf39fe.wav')
wavFiles.append('affed74c3b93602385f6d52ba9076dee.wav')
wavFiles.append('cadc501bf659b6c487aa6f692552e317.wav')
wavFiles.append('f50a5868f19fed8e867dd3983ff784d4.wav')
wavFiles.append('sample9.wav')

GT = []
GT.append('the vehicle does start and drive')
GT.append('would you like cream and sugar')
GT.append('um can i just get three mcchickens')
GT.append('okay and what\'s the code')
GT.append('uh no not just regular')
GT.append('twenty piece chicken nuggets')
GT.append("always forgive your enemies nothing annoys them so much")
GT.append('today only about eleven percent of federal it systems are running in the cloud')
GT.append('even nuclear weapons are only about one percent efficient chemical weapons are a tiny fraction of a percent in terms of their efficiency')
GT.append('we\'re gonna come over here and there it is scale')
GT.append('i know what that is i just don\'t know what items you wanted')

PT = []
PT.append(':red[it\'ll be a good bus store] and drive')
PT.append('the :red[gds why you make sure]')
PT.append('um can i just get three :red[make check ins]')
PT.append('okay and :red[wolstter] code')
PT.append('uh no :red[no that\'s very go]')
PT.append(':red[pony peace] chicken nuggets')
PT.append("always forgive :red[their] enemies nothing annoys them so much")
PT.append(':red[to day] only about eleven :red[per cent] of federal it :red[t] systems are running in the cloud')
PT.append('even nuclear weapons are only about :red[oneer] efficient chemical weapons are a tiny fraction of a :red[perc] in terms of their efficiency')
PT.append('we\'re :red[going to] come over here and there it is scale')
PT.append('i know what that is i just don\'t know what :red[ei dont] you :red[want it]')


FT = []
FT.append('the vehicle does start and drive')
FT.append('would you like cream and sugar')
FT.append(':red[(um)] can i just get three mcchickens')
FT.append('okay and what\'s the code')
FT.append(':red[(uh)] no not just regular')
FT.append('twenty piece chicken nuggets')
FT.append('always forgive your enemies nothing annoys them so much')
FT.append('today only about eleven percent of federal it systems are running in the cloud')
FT.append('even nuclear weapons are only about one percent efficient chemical weapons are a tiny fraction of a percent in terms of their efficiency')
FT.append('we\'re gonna come over here and there it is scale')
FT.append('i know what that is i just don\'t know what items you wanted')

st.set_page_config(layout='wide')

st.markdown("<h3 style='text-align: center;'>Introduction</h3>", unsafe_allow_html=True)
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()
intro_markdown = read_markdown_file("introduction.md")
st.markdown(intro_markdown, unsafe_allow_html=True)

st.markdown('---')
col1, col2, col3, col4 = st.columns(4)


col1.markdown("<h4 style='text-align: center;'>Audio</h4>", unsafe_allow_html=True)
col2.markdown("<h4 style='text-align: center;'>Ground Truth</h4>", unsafe_allow_html=True)
col3.markdown("<h4 style='text-align: center;'>Pre_trained</h4>", unsafe_allow_html=True)
col4.markdown("<h4 style='text-align: center;'>Fine_tuned</h4>", unsafe_allow_html=True)
st.markdown("___")

for ind in range(len(wavFiles)):
    col1, col2, col3, col4 = st.columns(4)
    col1.audio('samples/'+ wavFiles[ind], format='audio/wav')
    col2.markdown(GT[ind], unsafe_allow_html=True)
    col3.markdown(PT[ind], unsafe_allow_html=True)
    col4.markdown(FT[ind], unsafe_allow_html=True)
    st.markdown("---")

