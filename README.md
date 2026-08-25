# Kitap & Film Öneri Chatbotu

Kullanıcının ilgi alanlarına ve sohbet sırasında verdiği yanıtlara göre film ve kitap önerileri sunan Flask tabanlı bir web uygulamasıdır.

Uygulama; Google Gemini API, OMDb API ve Google Books API entegrasyonlarını kullanarak önerileri dinamik olarak oluşturur ve kullanıcıyla doğal bir sohbet akışı üzerinden etkileşim kurar.

## Projenin Amacı

Projenin temel amacı, kullanıcıların film veya kitap ararken yalnızca sabit listelerle karşılaşması yerine, tercihlerini dikkate alan daha etkileşimli bir öneri deneyimi sunmaktır.

Kullanıcı istediği türü, ilgilendiği konuları veya daha önce tükettiği içerikleri belirtebilir. Chatbot, konuşmanın bağlamını dikkate alarak buna uygun yeni öneriler üretir.

## Kullanılan Teknolojiler

* **Python 3.10** — Uygulamanın temel programlama dili
* **Flask** — Web uygulamasının backend yapısı ve HTTP isteklerinin yönetimi
* **Google Gemini API** — Kullanıcı mesajlarının yorumlanması ve doğal dilde yanıt oluşturulması
* **OMDb API** — Film bilgilerinin alınması
* **Google Books API** — Kitap bilgilerinin alınması

## Özellikler

* Film ve kitap önerileri sunma
* Kullanıcının tercihlerini sohbet üzerinden anlayabilme
* Önceki mesajları dikkate alarak konuşma bağlamını koruma
* Daha önce önerilen veya kullanıcının izlediğini/okuduğunu belirttiği içeriklere göre yeni alternatifler sunma
* Kullanıcının iletişim biçimine uygun daha doğal yanıtlar oluşturma
* Film bilgilerini OMDb API üzerinden dinamik olarak alma
* Kitap bilgilerini Google Books API üzerinden dinamik olarak alma
* Mobil cihazlarla uyumlu sade web arayüzü

## Örnek Kullanım

**Kullanıcı:** Gerilim filmi öner.

**Chatbot:**
Gone Girl, Prisoners ve Se7en gibi gerilim ağırlıklı filmler önerebilir.

**Kullanıcı:** Bunları daha önce izledim.

**Chatbot:**
Konuşmanın önceki kısmını dikkate alarak farklı filmler önerir.

Benzer şekilde kullanıcı kitap önerisi istediğinde, tercihleri doğrultusunda Google Books API üzerinden elde edilen bilgiler kullanılarak uygun kitaplar sunulur.

## Nasıl Çalışır?

Uygulamada kullanıcıdan alınan mesaj Flask backend'e gönderilir. Mesajın içeriği ve mevcut konuşma bağlamı değerlendirilerek kullanıcının film mi yoksa kitap mı aradığı ve nasıl bir öneri istediği belirlenir.

İhtiyaca göre:

1. Gemini API ile kullanıcının isteği yorumlanır.
2. Film içerikleri için OMDb API kullanılır.
3. Kitap içerikleri için Google Books API kullanılır.
4. Elde edilen bilgiler sohbet bağlamıyla birleştirilir.
5. Sonuç kullanıcıya doğal bir sohbet yanıtı olarak sunulur.

## Geliştirme

Proje, Flask kullanılarak geliştirilen web arayüzü ile API entegrasyonlarını tek bir uygulama içerisinde bir araya getirir.

Geliştirme sürecinde özellikle:

* dış servislerle API entegrasyonu,
* kullanıcı girdilerinin işlenmesi,
* sohbet bağlamının yönetilmesi,
* dinamik içerik oluşturulması,
* sade ve kullanılabilir bir arayüz tasarlanması

üzerine odaklanılmıştır.

## Canlı Demo

Uygulamanın yayınlanmış sürümüne Hugging Face Spaces üzerinden erişilebilir:

[Chatbot'u Deneyin](https://huggingface.co/spaces/Berk-0/ChatBot)

