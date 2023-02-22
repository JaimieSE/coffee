import streamlit as st 

with st.form(key="form2"):
  st.subheader("This one gives opinions on your coffee taste:")
  name = st.text_input("How may I address you today?")
  coffepref = st.selectbox("Coffee Preferences",["##","Latte", "Espresso", "Americano", "Macchiato", "Mocha", "Frappecino"])
  if coffepref == "Macchiato":
     st.write("You", name, "have an **exceptional, phenomenal, professional, amazing** taste")
  if coffepref == "Latte":
    st.write("You're taking the safest option, can't blame you, the world is too unpredictable these days, stay safe", name)
  if coffepref == "Espresso":
    st.write("I think you're overworked or sleep deprived. I refuse to believe that there are people who genuinely enjoys the taste of pure raw coffee beans. Go get some sleep", name)
  submit = st.form_submit_button(label = "Get judged today!")
  if coffepref == "Americano":
    st.write("Okay, you're not too bad. You are a just very neutral person", name, "and there is absolutely nothing wrong with that.")
  if coffepref == "Mocha":
    st.write(name, "just get milo.")
  if coffepref == "Frappecino":
    st.write(name, "I hope you know how disappointed I am. I was hoping no one chose this option but you just had to be special. No further comment, I wish you happiness.")
  if coffepref == "##":
    st.write("##")
st.write("**_THIS IS A JOKE, I RESPECT ALL COFFEE PREFERENCES!_** :gray[except for frappecino enjoyers]")


