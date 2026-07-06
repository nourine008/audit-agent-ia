import os 
import streamlit as st 
from agent_audit import agent_executor

st.set_page_config(
   page_icon="🛡️",
   page_title="agent audit",
   layout="centered",
)

st.title('Agent IA "RAG" de Cybersécurité et Audit de Code')
st.subheader("Analyse de vulnérabilités OWASP par Agent ReAct et RAG")
st.write("Téléversez un script Python pour lancer un audit de sécurité profond basé sur les standards OWASP.")

st.divider()

fichier_upload=st.file_uploader("deposer votre fichier python à analyser ",type=["py"])

if fichier_upload is not None:
    code_a_auditer=fichier_upload.read().decode("utf-8")
    with st.expander("Voir le code source soumis"):
        st.code(code_a_auditer, language="python")
#boutton de lancement de l'agent 
if st.button("Lancer l'Audit Sécurité"):
    with st.spinner("Analyse en cours ..... veuillez patienter.... "):
        try:
            # Appel de l'Agent Executor 
            resultat = agent_executor.invoke({"input": code_a_auditer})
            # Zone d'affichage du rapport final
            st.success("Audit terminé avec succès !")
            st.subheader(" Rapport d'Audit Sécurité Final (Conforme BRD)")
                
            # st.markdown permet d'afficher proprement le format en puces et le code corrigé
            st.markdown(resultat["output"])

        except Exception as e:
            st.error(f"Une erreur est survenue lors de l'analyse : {e}")

    