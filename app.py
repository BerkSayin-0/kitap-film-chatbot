from flask import Flask, render_template, request, jsonify, session
import requests

app = Flask(__name__)
app.secret_key = "chatbot-secret" 

# === API Keys ===
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"





@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"].strip().lower()

    # ===  Basit sohbet yanıtları ===
    casual_responses = {
        "teşekkür": "Rica ederim 😊 Her zaman yardımcı olmaktan memnuniyet duyarım!",
        "sağ ol": "Ne demek! 😄",
        "merhaba": "Merhaba! 🎬 Bugün film mi yoksa kitap mı öneriyim?",
        "selam": "Selam! 👋 Film mi arıyorsun yoksa kitap mı?",
        "günaydın": "Günaydın! ☀️ Harika bir gün geçirmeni dilerim!",
        "nasılsın": "Gayet iyiyim! Sen nasılsın? 😊",
    }

    for keyword, reply_text in casual_responses.items():
        if keyword in user_input:
            return jsonify({"reply": reply_text})

    # ===  “başka öner” veya “bunları izledim” gibi ifadeler ===
    if any(phrase in user_input for phrase in ["başka", "yenisi", "farklı öner", "bunları izledim"]):
        last_type = session.get("last_type", None)
        if not last_type:
            return jsonify({"reply": "Ne tür istiyorsun? 🎬 Film mi yoksa 📚 kitap mı öneriyim?"})

        prompt = f"Kullanıcı daha önce {last_type} önerileri istemişti. Şimdi yeni {last_type} önerileri istiyor. 3 yeni {last_type} önerisi sun, kısa ve samimi bir şekilde yaz."
        gemini_response = requests.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            json={"contents": [{"parts": [{"text": prompt}]}]},
        ).json()

        if "candidates" in gemini_response:
            reply = gemini_response["candidates"][0]["content"]["parts"][0]["text"]
            return jsonify({"reply": reply})
        else:
            return jsonify({"reply": "Şu anda yeni öneri getiremiyorum 😅 Daha sonra tekrar dener misin?"})

    # === Kullanıcının önceki isteğini hatırlama ===
    content_type = None
    if "film" in user_input:
        content_type = "film"
    elif "kitap" in user_input:
        content_type = "kitap"
    else:
        # Önceki isteği kullan
        content_type = session.get("last_type", None)

    # Eğer hâlâ bilinmiyorsa, yönlendir
    if not content_type:
        return jsonify({"reply": "Ne aradığını anlayamadım 🤔 Film mi yoksa kitap mı öneriyim?"})

    session["last_type"] = content_type  # türü hatırla

    # ===  Arama sorgusunu sadeleştir ===
    query = (
        user_input.replace("film", "")
        .replace("kitap", "")
        .replace("öner", "")
        .replace("bana", "")
        .strip()
    )
    if not query:
        query = "romantik" if content_type == "film" else "popüler"

    # ===  API isteği ===
    if content_type == "film":
        api_url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&s={query}"
    else:
        api_url = f"https://www.googleapis.com/books/v1/volumes?q={query}"

    data = requests.get(api_url).json()

    # === İlk 3 sonucu al veya popüler öneriler ver ===
    if content_type == "film" and "Search" in data:
        items = [f"{i['Title']} ({i['Year']})" for i in data["Search"][:3]]
    elif content_type == "kitap" and "items" in data:
        items = [i["volumeInfo"]["title"] for i in data["items"][:3]]
    else:
        if content_type == "film":
            items = ["Titanic (1997)", "The Notebook (2004)", "La La Land (2016)"]
        else:
            items = ["Pride and Prejudice", "Me Before You", "The Time Traveler’s Wife"]

    # === Gemini prompt ===
    prompt = f"""
Kullanıcı {content_type} istiyor: {user_input}.
Aşağıda {content_type} API'dan gelen öneriler var: {', '.join(items)}.
Eğer liste boşsa, popüler {content_type} önerileri üret.
Kısa, samimi ve doğal bir dille önerilerini yaz.
"""

    # ===  Gemini API isteği ===
    gemini_response = requests.post(
        f"{GEMINI_URL}?key={GEMINI_API_KEY}",
        json={"contents": [{"parts": [{"text": prompt}]}]},
    ).json()

    # ===  Hata kontrolü ===
    if "error" in gemini_response:
        print("❌ Gemini API hatası:", gemini_response["error"])
        return jsonify({"reply": "⚠️ Gemini API yanıt veremedi. API anahtarını veya bağlantını kontrol et."})

    if "candidates" not in gemini_response:
        print("⚠️ Beklenmeyen yanıt:", gemini_response)
        return jsonify({"reply": "⚠️ Gemini beklenmedik bir yanıt gönderdi. API erişimini kontrol et."})

    reply = gemini_response["candidates"][0]["content"]["parts"][0]["text"]
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
