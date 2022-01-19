import streamlit as st
import camelot as cam
import subprocess
from subprocess import STDOUT, check_call
import os
import base64


#  Enable at the time of Hosting in any Linux based server


@st.cache
def gh():
    proc = subprocess.Popen('apt-get install -y ghostscript', shell=True, stdin=None,
                            stdout=open(os.devnull, "wb"), stderr=STDOUT, executable="/bin/bash")
    proc.wait()


gh()


st.title("Table Extractor form PDF")
st.subheader("Upload any non-scanned PDF for better result")


input_pdf = st.file_uploader(label="Upload your PDF here...", type='pdf')

st.markdown("### Page Number")

page_number = st.text_input(
    "Enter thr Page from where you want to extract in the PDF eg:2 ", value=1)

if input_pdf is not None:
    with open("input.pdf", "wb") as f:
        base64_pdf = base64.b64encode(input_pdf.read()).decode('utf-8')
        f.write(base64.b64encode(base64_pdf))
    f.close()

    table = cam.read_pdf("input.pdf, pages = page_number", flavor='stream')

    st.markdown("### Number of Tables")

    st.write(table)

    if len(table) > 0:
        option = st.slectbox(
            lable="select the Table to be displayed", option=range(len(table)+1))

        st.markdown('### Output Table')
        st.dataframe(table[int(option)-1].df)
    else:
        pass
