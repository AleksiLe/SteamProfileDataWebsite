from website import create_app, dp


app = create_app()

def create_tables():
    dp.create_all()
if __name__ == '__main__':
    app.run(debug=True)