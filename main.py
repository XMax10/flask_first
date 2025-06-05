from flask import Flask, render_template, request
import json
import sqlite3

app = Flask(__name__)

@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/feedback", methods=['GET', "POST"])
def form():
    if request.method == 'POST':
        user_title = request.form.get("title")
        user_description = request.form.get("desckripshen")
        user_question = request.form.get("quation")
        user_email = request.form.get("E_Mail")

        # зберігаємо дані в базу даних
        con = sqlite3.connect("data.db") # створить базу або підключиться до неї
        cursor = con.cursor()

        cr_table = """
        CREATE TABLE IF NOT EXISTS contact (
            title text,
            description text,
            question text,
            email text
        );

        """

        cursor.execute(cr_table) # створить табличку в базі або нічого не робить якщо така існує

        save_data = f"""
        INSERT INTO contact (title, description, question, email)
        VALUES ('{user_title}', '{user_description}', '{user_question}', '{user_email}');
        """

        cursor.execute(save_data) # відправляємо дані з форми в табличку
        con.commit()
        con.close()
        
        
    return render_template("feedback.html")



app.run(host='localhost', port=8000)



