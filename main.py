from website import create_app

#Metodo que inicia el programa 

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)