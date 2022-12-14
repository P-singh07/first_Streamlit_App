import streamlit
import pandas
import requests
#import Snowflake.connector
#from urllib.error import URLERROR

streamlit.title("My Parents New Healthy Dinner!!")

streamlit.header("Breakfast Menu")
streamlit.text("🥣Omega 3 blueberry oat meal")
streamlit.text("🥗Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔Hard-Boiled free Range EGG")
streamlit.text("🥑🍞 Avacado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avacado','Straberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(fruits_to_show)
#streamlit.text("I selected 'Avacado','Straberries'")

streamlit.header("Fruityvice Fruit Advice!")
#try:
fruit_choice = streamlit.text_input('What fruit would you like information about?')
#  if not fruit_choice:
streamlit.write('The user entered ', fruit_choice)
    #streamlit.text(fruityvice_response.json())
#  else:
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
#except URLerror as e:
 #   streamlit.error(e)

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.header("the list fruit_load_list contains")
#streamlit.dataframe(my_data_rows)
#my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('From Streamlit')")
