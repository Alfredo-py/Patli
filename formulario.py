from flask import Flask, make_response, request, render_template, send_file, send_from_directory, safe_join,current_app
from werkzeug.utils import secure_filename
import os
from docx import Document


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './Archivos_Docx'
app.config['DOWNLOAD_FOLDER'] = 'recetas'

@app.route('/descargar/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    descargar = os.path.join(current_app.root_path, app.config['DOWNLOAD_FOLDER'])
    print(descargar)
    return send_from_directory(directory=descargar, filename=filename)
if __name__ == "__main__":
    server_name = app.config['SERVER_NAME']
    if server_name and ':' in server_name:
        host, port = server_name.split(":")
        port = int(port)
    else:
        port = 4000
        host = "0.0.0.0"
    app.run(host=host, port=port,debug=True)
