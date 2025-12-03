from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# fungsi chatbot sederhana
def bot_reply(msg):
    return f"Saya menerima pesan: {msg}"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.form.get("message")
    reply = bot_reply(user_msg)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
