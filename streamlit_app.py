# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_staw: Cup with straw:cup_with_staw:")

st. write(
    "Choose the fruit you want to custome smoothie"
)
name_of_order = st.text_input('name_of_smoothee')
st.write('The Name of Smoothie :', name_of_order) 
cx=st.connection("snowflake")
session = cx.session()
#get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('fruit_name'))

#st.dataframe(data=my_dataframe, use_container_width=True)
ingredent_list=st.multiselect('choose 5 ingredent',my_dataframe);
if ingredent_list:
    #st.write(ingredent_list)
    #st.text(ingredent_list)

    ingredents_string=''
    for fruit_choosen in ingredent_list:
        ingredents_string+=fruit_choosen+' ';

    st.write(ingredents_string);

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredents_string + """','""" + name_of_order + """' )"""
    
    time_to_insert=st.button("submit order" )
    #st.write(my_insert_stmt)
    #st.stop();
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your smoothie is ordered!  ' + name_of_order ,icon='✅')
    
   # st.write(my_insert_stmt)

    #if ingredents_string:
        
  
