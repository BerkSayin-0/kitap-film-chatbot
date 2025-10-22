# 🎬 Kitap & Film Öneri Chatbotu

Bu proje, Flask tabanlı bir web uygulamasıdır.  
Kullanıcıdan aldığı girdiye göre Google Gemini API, OMDb ve Google Books API’lerini kullanarak dinamik film veya kitap önerileri sunar.

---

## 🚀 Teknolojiler
- Python 3.10  
- Flask (web framework)  
- Google Gemini 2.0 API  
- OMDb API (film verileri)  
- Google Books API (kitap verileri)  

---

## 🧠 Projenin Amacı
Kullanıcıya kişisel zevklerine göre film ve kitap önerileri sunan bir akıllı sohbet sistemi geliştirmek.

---

## 💬 Örnek Kullanım Diyalogları

**Sen:** Merhaba  
**Bot:** Merhaba! 🎬 Bugün film mi yoksa kitap mı öneriyim?

**Sen:** Gerilim filmi öner  
**Bot:** Harika! İşte birkaç öneri:  
- *Gone Girl (2014)*  
- *Prisoners (2013)*  
- *Se7en (1995)*  
Karanlık atmosferi seviyorsan bu filmler tam senlik! 

**Sen:** Teşekkürler  
**Bot:** Rica ederim! Başka bir tür ister misin?

**Sen:** Kitap öner  
**Bot:** Tabii! İşte birkaç popüler kitap:  
- *Hayvan Çiftliği – George Orwell*  
- *1984 – George Orwell*  
- *Cesur Yeni Dünya – Aldous Huxley*

---

## 🧠 Chatbot’un Özellikleri
- Kullanıcının önceki konuşmalarını hatırlayabilir (örneğin: “ama bunları izledim” derse yeni öneriler verir)
- Sohbet tonunu otomatik olarak değiştirir (samimi / ciddi)
- Hem kitap hem film verilerini dinamik olarak dış API’lerden çeker

---

## 🧩 Geliştirme Notları
- Flask kullanılarak web arayüzü oluşturuldu  
- Gemini API, OMDb ve Google Books API’leri ile entegre edildi  
- Kullanıcı deneyimi sade ve mobil uyumlu olacak şekilde tasarlandı  

## 🌐 Canlı Demo
Proje Hugging Face üzerinde yayınlanmıştır:  
👉 [Chatbot’u Deneyin](https://huggingface.co/spaces/Berk-0/ChatBot)

