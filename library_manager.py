import streamlit as st

# Initialize the book list if not already
if "library" not in st.session_state:
    st.session_state.library = []

st.set_page_config(page_title="📚 Personal Library Manager", layout="centered")
st.title("📚 Command-Line Personal Library Manager")
st.caption("Type commands like in a terminal: `add <book>`, `remove <book>`, `list`, `search <keyword>`, `help`")

# Command input
command = st.text_input(">>>", placeholder="Type a command and press Enter")

# Process command
def handle_command(cmd):
    parts = cmd.strip().split(" ", 1)
    action = parts[0].lower()

    if action == "add" and len(parts) > 1:
        book = parts[1].strip()
        if book in st.session_state.library:
            st.warning(f"'{book}' is already in your library.")
        else:
            st.session_state.library.append(book)
            st.success(f"Added '{book}' to your library.")
    
    elif action == "remove" and len(parts) > 1:
        book = parts[1].strip()
        if book in st.session_state.library:
            st.session_state.library.remove(book)
            st.success(f"Removed '{book}' from your library.")
        else:
            st.error(f"'{book}' not found in your library.")

    elif action == "list":
        if st.session_state.library:
            st.subheader("📚 Your Library:")
            for i, book in enumerate(st.session_state.library, start=1):
                st.markdown(f"{i}. {book}")
        else:
            st.info("Your library is empty.")

    elif action == "search" and len(parts) > 1:
        keyword = parts[1].strip().lower()
        matches = [book for book in st.session_state.library if keyword in book.lower()]
        if matches:
            st.subheader(f"🔍 Results for '{keyword}':")
            for book in matches:
                st.markdown(f"- {book}")
        else:
            st.warning("No matches found.")

    elif action == "help":
        st.markdown("""
        **Available commands**:
        - `add <book name>`: Add a book to your library  
        - `remove <book name>`: Remove a book from your library  
        - `list`: Show all books  
        - `search <keyword>`: Find books  
        - `help`: Show this help  
        """)
    else:
        st.error("Invalid command. Type `help` to see available commands.")

if command:
    handle_command(command)
