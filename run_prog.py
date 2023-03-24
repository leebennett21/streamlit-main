import os

# os.system('start chrome --app="http://localhost:8501" --max_old_space_size=4096 --args --js-flags="--max_old_space_size=4096"')
os.system('start chrome --app="http://localhost:8501"')

os.system('streamlit run Reg151_main.py --server.port 8501')