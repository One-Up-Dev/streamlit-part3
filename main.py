import pandas as pd
import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu


# ===================================================================================
#   AUTHENTIFICATION A PARTIR D'UN FICHIER CSV
# ===================================================================================
df = pd.read_csv("usernames.csv")

lesDonneesDesComptes = {
    "usernames": df.set_index("name").to_dict(orient="index")
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()

# ===================================================================================
#   SESSION APRES LOGIN
# ===================================================================================

if st.session_state["authentication_status"]:
    # ===================================================================================
    #   SIDEBAR
    # ===================================================================================
    with st.sidebar:
        authenticator.logout("Déconnexion")
        st.write(f"Bienvenue {st.session_state['username']}")
        with st.container():
            selection = option_menu(
                    menu_title=None,
                    options = ["Accueil", "Photos"],
                    icons= ['house', 'camera']
                )
        st.page_link("https://github.com/One-Up-Dev/streamlit-part2", label="Code Source", icon=":material/code_blocks:")


# ===================================================================================
#   GESTION DES PAGES
# ===================================================================================
    if selection == "Accueil":
            st.title(f"Ma page d'accueil")
            st.image('images/ONEUP.png')
    elif selection == "Photos":
            st.title(f"Mon album photos")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.header("A cat")
                st.image("https://static.streamlit.io/examples/cat.jpg")
            with col2:
                st.header("A dog")
                st.image("https://static.streamlit.io/examples/dog.jpg")
            with col3:
                st.header("An owl")
                st.image("https://static.streamlit.io/examples/owl.jpg")
               

# ===================================================================================
#   GESTION D'aUTHENTIFICATION - CONDITION D'ERREUR
# ===================================================================================

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')




