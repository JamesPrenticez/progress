# Bit Bot
https://www.youtube.com/playlist?list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX

### Run (Windows)
0. python -m venv venv
1. . venv/Scripts/activate
2. pip install -r requirements.txt
3. flask run || python app.py
4. http://localhost:5000/

5. bash bin/server-debug.sh

### Requirements File
- To create a requirement file using pipreqs run the following command:
  - ``` pip install pipreqs ```
  - ``` pipreqs /path/to/project ``` (or . for root directory)
  - ``` pipreqs . --force ``` (rewrite exisiting)

## Flask
  - Deploy static files with flask backend
  - You may need to set enviroment variable "export FLASK_DEBUG=True" for "flask run" to work in debug mode
  - To get auto reloading of static files working we need "export FLASK_RUN_EXTRA_FILES="templates/index.html""


## Threading 
https://stackoverflow.com/questions/24251898/flask-app-update-progress-bar-while-function-runs