**Model**: the model used for fine-tuning is a pre-trained ASR model (Conformer-CTC) provided by Nvidia, which is  trained on around 24500 hours of english speech. You may find more info on the detail of this model here: [Conformer-CTC Model](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_en_conformer_ctc_large).




**Data**: the dataset used for fine-tuning is Appen ultra-high volume off-the-shelf (UHV-OTS) speech dataset. The UHV-OTS corpora have the advantages of: 1) high quality transcriptions as a result of a fully manual audit, 2) rich and detailed metadata to support the training of models not only for speech recognition, but also speaker diarization, speaker identification, accent and gender detection, 3) highly varied speakers, domains and speaking styles to ensure dataset is representative of complex, real-world environments
