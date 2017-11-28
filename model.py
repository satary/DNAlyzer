from wtforms import Form, StringField, validators

class InputForm(Form):
    PDB_index = StringField(label='PDB index', validators=[validators.InputRequired(), validators.length(4)])
    
