# load json and create model
json_file = open(nome_model, 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights(nome_peso)
print("Loaded model from disk")

predicted_stock_price = loaded_model.predict(dados_teste_X)