import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import random

def mathe_aufgabe():
    zahl1 = random.randint(1, 10)
    zahl2 = random.randint(1, 10)
    loesung = zahl1 + zahl2

    print(f"Was ist {zahl1} + {zahl2}?")
    antwort = input("Deine Antwort: ")

    try:
        if int(antwort) == loesung:
            print("✅ Richtig!")
        else:
            print(f"❌ Falsch. Die richtige Antwort ist {loesung}.")
    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")

# Aufruf der Funktion
mathe_aufgabe()
