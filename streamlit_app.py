import streamlit as st

# Set the title of the app
st.title('Basic Streamlit App')

# Add a header
st.header('Welcome to My Streamlit App!')

# Add a subheader
st.subheader('This is a subheader')

# Add some text
st.text('This is a basic Streamlit app to demonstrate its features.')

# Add a markdown
st.markdown('**This is bold text**')

# Add a widget: slider
age = st.slider('Select your age:', 0, 100, 25)

# Add a widget: text input
name = st.text_input('Enter your name:')

# Add a button
if st.button('Submit'):
    st.write(f'Hello, {name}! You are {age} years old.')

# Add a checkbox
if st.checkbox('Show secret message'):
    st.write('This is a secret message!')

# Add a selectbox
favorite_color = st.selectbox('Choose your favorite color:', ['Red', 'Green', 'Blue'])

# Display the selected value
st.write(f'Your favorite color is {favorite_color}.')

# Add an image
#st.image('https://via.placeholder.com/150', caption='Sample Image')

# Add a dataframe
import pandas as pd
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
})
st.dataframe(df)

# Add a plot
st.line_chart(df['Column 1'])

# Add a map
st.map(pd.DataFrame({
    'lat': [37.7749, 40.7128, 34.0522],
    'lon': [-122.4194, -74.0060, -118.2437]
}))
