from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', prediksi_tbc="")

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    batuk, sesaknafas, nyeridada, demam, nafsumakan, lemas  = [x for x in request.form.values()]

    data = []

    if batuk == 'batuk_0':
        data.append(0)
    elif batuk == 'batuk_1':
        data.append(0.25)
    elif batuk == 'batuk_2':
        data.append(0.5)
    elif batuk == 'batuk_3':
        data.append(0.75)
    else:
        data.append(1)

    if sesaknafas == 'sesaknafas_0':
        data.append(0)
    elif sesaknafas == 'sesaknafas_1':
        data.append(0.5)
    else:
        data.append(1)

    if nyeridada == 'nyeridada_0':
        data.append(0)
    elif nyeridada == 'nyeridada_1':
        data.append(0.5)
    else:
        data.append(1)

    if demam == 'demam_0':
        data.append(0)
    elif demam == 'demam_1':
        data.append(0.5)
    else:
        data.append(1)

    if nafsumakan == 'nafsumakan_0':
        data.append(0)
    else:
        data.append(1)

    if lemas == 'lemas_0':
        data.append(0)
    else:
        data.append(1)

    
    nama = {0 : 'Negatif', 1 : 'Positif'}

    prediction = model.predict([data])
    output = nama[prediction[0]]

    return render_template('index.html', prediksi_tbc=output, batuk=batuk, sesaknafas=sesaknafas, nyeridada=nyeridada, demam=demam, nafsumakan=nafsumakan, lemas=lemas)


if __name__ == '__main__':
    app.run(debug=True)