from flask import Flask, jsonify, request 
from flask_cors import CORS


app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")


@app.route('/proba', methods=['GET'])
def proba():
    return("ovo bi trebalo raditi")


RECEPTI = [

    {
        'title':'Kolac od jagoda',
        'vrsta':'desert',
        'kuhar':'Vlatko Masnic',
        'opis':'finooo',
        
    },
     {
        'title':'Rizi bizi',
        'vrsta':'predjelo',
        'kuhar':'Perica Mljackovic',
        'opis':'Riza i grasak',
        
    },
     {
        'title':'Kolac od banana',
        'vrsta':'desert',
        'kuhar':'Banana Man',
        'opis':'ovo je napravio banana men',
        
    },
     {
        'title':'Pecena piletina',
        'vrsta':'Glavno jelo',
        'kuhar':'Ljubica Pilenko',
        'opis':'Purica',
        
    },
    {
        'title':'Pecene kobase',
        'vrsta':'Glavno jelo',
        'kuhar':'Gogo Gogo',
        'opis':'iz najbolje mesnice ikad',
        
    },
]
    
@app.route('/recepti', methods=['GET', 'POST'])
def all_recepti():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        RECEPTI.append({
            'title': post_data.get('title'),
            'vrsta': post_data.get('vrsta'),
            'kuhar': post_data.get('kuhar'),
            'opis': post_data.get('opis')})
        response_object['message'] =  'Vas recept je uspjesno dodan!'
    else:
        response_object['recepti'] = RECEPTI
    return jsonify(response_object)
   


if __name__ == "__main__":
    app.run(debug=True)