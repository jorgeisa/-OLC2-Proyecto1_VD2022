from flask_wtf import FlaskForm
from flask_codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField
from flask import Flask, render_template
from flask_codemirror import CodeMirror
# from src.Interprete.grammar.Grammar import *

SECRET_KEY = 'secret!'
CODEMIRROR_THEME = 'liquibyte'
CODEMIRROR_ADDONS = (('display','autorefresh'),)
CODEMIRROR_LANGUAGES = ['javascript', 'python', 'sql']

app = Flask(__name__)
app.config.from_object(__name__)
codemirror = CodeMirror(app)

# Variables
analyzer = ""
data_error = []
table_simbol = ""
report_ast = ""

class CODEMIRROR_MY_FORM(FlaskForm):
    source_code = CodeMirrorField(
        language = 'python', 
        config = {
            'lineNumbers'    : 'true', 
            'identWhithTabs' : 'true',
            'electricChars'  : 'true',
            'autocorrect'    : 'true'
            })
    submit = SubmitField('Submit')

@app.route('/')
def Home():
    return render_template('Home.html')
    
@app.route('/analisis', methods = ['GET', 'POST'])
def index():
    source_form = CODEMIRROR_MY_FORM()
    out = ""
    text = source_form.source_code.data
    # variables globales
    global analyzer
    global data_error
    global table_simbol
    if text != None:
        try:
            analyzer = "Obtener el arbol"
            data_error = []
            out = "Salida del compilador\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\na"
            # analyzer = execute(text) # Metodo para analizar el codigo
            # data_error = analyzer.get_exception() # Metodo para obtener errores
            # out = analyzer.get_console() # Obtener salida del analizador         
            # table_simbol = analyzer.Table

        except Exception as e:
            out = f"WARNING!!! ({e})"
            data_error = None
    else:
        out = ""
    return render_template('index.html', source_form=source_form, out=out, data_error=data_error)

@app.route('/Reporte')
def Reporte():
    return render_template('Reporte.html')


if __name__ == "__main__":
    app.run(debug=True)
