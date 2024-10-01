import re
import streamlit as st

def find_unique_words(text, word_length):
    # Using regular expressions to find words of specified length
    words = re.findall(rf'\b\w{{{word_length}}}\b', text)
    
    # Using a set to store unique words of specified length
    unique_words = set(words)
    
    # Returning the found unique words in uppercase
    return [word.upper() for word in unique_words]

def main():
    
    st.set_page_config(page_title='Find Words', page_icon='🇯🇵')

    st.header(':blue[Words Finder Application] :sunglasses:', divider='rainbow')
    
    text = st.text_area("Input Text", height=300)
    word_length = st.number_input("Word Length", min_value=1, max_value=20, value=7, step=1)
    
    if st.button("Generate", use_container_width=True):
        if text:
            unique_words = find_unique_words(text, word_length)
            if unique_words:
                st.write(word_length, "Letters Words " ,":")
                styled_words = ''.join(f'<span style="background-color: #FFFF00; color: #D50000; padding: 5px; margin: 5px; display: inline-block; border-radius: 5px;">{word}</span>' for word in unique_words)
                st.markdown(styled_words, unsafe_allow_html=True)
            else:
                st.write(f"{word_length} Letters Word is not Found.")
        else:
            st.write("Please Input some text.")

    footer = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}   
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: blue;
            text-align: center;
            padding: 10px;
        }
        [data-testid="stElementToolbar"] {
            display: none;
        }
        </style>
    """

    st.markdown(footer, unsafe_allow_html=True)
            
if __name__ == "__main__":
    main()