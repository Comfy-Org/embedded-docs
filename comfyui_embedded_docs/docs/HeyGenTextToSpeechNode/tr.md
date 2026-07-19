# HeyGenTextToSpeechNode

Metin kullanarak HeyGen'in Starfish TTS motoru ile konuşma sesi oluşturun. Bu düğüm, HeyGen'in 17 dildeki en popüler seslerini içerir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `text` | Sentezlenecek metin (en fazla 5000 karakter). Oluşturulan konuşma en az 1 saniye uzunluğunda olmalıdır. | STRING | Evet | 1 ila 5000 karakter |
| `voice` | Kullanılacak ses (HeyGen'in en popüler Starfish uyumlu sesleri arasından seçilmiştir). | STRING | Evet | Birden çok seçenek mevcut |
| `custom_voice_id` | İsteğe bağlı HeyGen ses kimliği. Ayarlandığında, yukarıda seçilen sesi geçersiz kılar. Sesin Starfish motorunu desteklemesi gerekir. | STRING | Hayır | Geçerli herhangi bir HeyGen ses kimliği |
| `speed` | Konuşma hızı çarpanı (varsayılan: 1.0). | FLOAT | Hayır | 0.5 ila 2.0 (adım: 0.05) |
| `ssml` | Metni SSML işaretlemesi olarak ele al (duraklamalar, vurgu ve telaffuz kontrolü için) (varsayılan: Yanlış). | BOOLEAN | Hayır | Doğru / Yanlış |
| `seed` | HeyGen'e gönderilmez; yeniden çalıştırmayı zorlamak için değiştirin (varsayılan: 42). | INT | Hayır | 0 ila 2147483647 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `AUDIO` | Girdi metninden oluşturulan sentezlenmiş konuşma sesi. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTextToSpeechNode/tr.md)

---
**Source fingerprint (SHA-256):** `82300626657db8ab16e96ae96b7dfe3291b77bf75efec35971dc772e5123cce7`
