
import streamlit as st



wavFiles = []
wavFiles.append('77d369396a6a567cc0f3059670d1f7ab.wav')
wavFiles.append('90b4fb9ce4042d84b8ddc6e0c8bf39fe.wav')
wavFiles.append('affed74c3b93602385f6d52ba9076dee.wav')
wavFiles.append('cadc501bf659b6c487aa6f692552e317.wav')
wavFiles.append('f50a5868f19fed8e867dd3983ff784d4.wav')
wavFiles.append('sample4.wav')
wavFiles.append('sample7.wav')

GT = []
GT.append('the vehicle does start and drive')
GT.append("always forgive your enemies nothing annoys them so much")
GT.append('today only about eleven percent of federal it systems are running in the cloud')
GT.append('even nuclear weapons are only about one percent efficient chemical weapons are a tiny fraction of a percent in terms of their efficiency')
GT.append('we\'re gonna come over here and there it is scale')
GT.append('would you like cream and sugar')
GT.append('the hot and spicy mcchickens')

PT = []
PT.append(':red[it\'ll be a good bus store] and drive')
PT.append("always forgive :red[their] enemies nothing annoys them so much")
PT.append(':red[to day] only about eleven :red[per cent] of federal it :red[t] systems are running in the cloud')
PT.append('even nuclear weapons are only about :red[oneer] efficient chemical weapons are a tiny fraction of a :red[perc] in terms of their efficiency')
PT.append('we\'re :red[going to] come over here and there it is scale')
PT.append('would you like :red[frem chergen]')
PT.append('the :red[gds why you make sure]')


FT = []
FT.append('the vehicle does start and drive')
FT.append('always forgive your enemies nothing annoys them so much')
FT.append('today only about eleven percent of federal it systems are running in the cloud')
FT.append('even nuclear weapons are only about one percent efficient chemical weapons are a tiny fraction of a percent in terms of their efficiency')
FT.append('we\'re gonna come over here and there it is scale')
FT.append('would you like cream and sugar')
FT.append('the high and spicy mchchickens')
st.set_page_config(layout='wide')
col1, col2, col3, col4 = st.columns(4)

st.markdown(
    """
    <style>
    textarea {
        font-size: 3rem !important;
    }
    input {
        font-size: 1rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
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

