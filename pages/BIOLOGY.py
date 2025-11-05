import streamlit as st
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

from Bio.Seq import Seq


st.markdown(
    """
    <style>
   .stApp {
        background-color: rgba(54, 88, 97,0.3);
        color: rgb(0,0,0);

    }

    header[data-testid="stHeader"] {
    background: transparent;
    }


    
    </style>""",unsafe_allow_html=True)

st.markdown("""

        <h1 style="background: rgba(255, 230, 150, 0.2); border-radius:20px; padding:15px; text-align:center">🧬 BIO Page 🔬</h1>

    """,unsafe_allow_html=True)


tab1,tab2,tab3=st.tabs(["Tab_1","Tab_2","tab_3"])
with tab1:

    check_letters={"A","C","T","G"}

    seq_1=st.text_area("Enter the first seq").strip()
    seq_2=st.text_area("Enter the second seq").strip()

    if st.button("Click Here",type="primary"):
        if seq_1.strip() and seq_2.strip():

            if not set(seq_1).issubset(check_letters):
                st.markdown(f"""
                <div style="
                    background-color: rgba(255, 230, 150, 0.2);
                    border: 2.6px solid #FFD700;
                    border-radius:27px;
                    color: #FFD700;
                    font-weight:bold;
                    font-size:23px;
                        ">


                <h5 style=" margin-left:20px; margin-top:6px; color:black;">⚠️ Invalid Sequance of DNA</h5>
    

                        
                </div>""",unsafe_allow_html=True)
            elif not set(seq_2).issubset(check_letters):
                st.markdown(f"""
                <div style="
                    background-color: rgba(255, 230, 150, 0.2);
                    border: 2.6px solid #FFD700;
                    border-radius:27px;
                    color: #FFD700;
                    font-weight:bold;
                    font-size:23px;
                        ">


                <h5 style=" margin-left:20px; margin-top:6px; color:black;">⚠️ Invalid Sequance of DNA</h5>
    

                        
                </div>""",unsafe_allow_html=True)
            else:

                st.markdown("""
    <h1>Result</h1>
    """,unsafe_allow_html=True)
                
                alignments=pairwise2.align.globalxx(seq_1.strip(),seq_2.strip())
                best=alignments[0]




                st.text(format_alignment(*best))

                st.write(f"Length: {len(best.seqA)}")
                




with tab2:

    big_seq=st.text_area(" Enter the Sequance of the DNA").strip()
    if not set(big_seq).issubset(check_letters):
        st.markdown(f"""
                <div style="
                    background-color: rgba(255, 230, 150, 0.2);
                    border: 2.6px solid #FFD700;
                    border-radius:27px;
                    color: #FFD700;
                    font-weight:bold;
                    font-size:23px;
                        ">


                <h5 style=" margin-left:20px; margin-top:6px; color:black;">⚠️ Invalid Sequance of DNA</h5>""",unsafe_allow_html=True)
    else:
        dna_seq=Seq(big_seq)
        dna_comp=dna_seq.complement()
        rev_comp=dna_seq.reverse_complement()

        

        if st.button("Click here",type="primary"):

            st.markdown(f"""
        <h6 style="text-align:center; padding:15px; background:rgba(120,120,120,0.5);margin-bottom:15px; border-radius:20px"> Input : --->  {dna_seq}</h6>

    """,unsafe_allow_html=True)

            st.markdown(f"""

        <h6 style="text-align:center; padding:15px; background:rgba(120,120,120,0.5); margin-bottom:15px; border-radius:20px">Complementry DNA : -----> {dna_comp}</h6>

    """,unsafe_allow_html=True)

            st.markdown(f"""

        <h6 style="text-align:center; padding:15px; background:rgba(120,120,120,0.5); margin-bottom:15px; border-radius:20px">Complementry DNA rEVERSE : -----> {rev_comp}</h6>

    """,unsafe_allow_html=True)



