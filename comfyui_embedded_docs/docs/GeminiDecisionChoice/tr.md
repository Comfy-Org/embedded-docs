# Google Gemini Decision (Choice)

Bağladığınız metin, görsel, ses veya video için kendi seçeneklerinizden birini seçin; seçilen seçeneği, konumunu ve bir güven değerini geri alın. `choice` çıktısını, girdileri aynı seçenek adlarını taşıyan bir Branch düğümüne bağlayın veya `option_index` üzerinden yönlendirin. Bir Branch düğümü en fazla 32 girdi kabul eder; bu nedenle daha büyük seçenek kümelerini `option_index` ile yönlendirin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model (varsayılan: `"gemini-decision-1"`). | COMBO | Evet | `"gemini-decision-1"` |
| `question` | Seçeneklerin yanıtladığı soru, en fazla 5000 karakter (varsayılan: "What style is the image?"). | STRING | Evet | 1 ile 5000 karakter arası |
| `options` | Her satırda bir seçenek, tam olarak yazıldığı gibi kullanılır, her biri en fazla 128 karakter. Hiçbirine uymayan girdiler için `other` gibi bir seçenek ekleyin (varsayılan: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Evet | 2 ile 255 seçenek arası |
| `images` | Sınıflandırılacak görseller; büyütülebilir yuvalar (`image_1` ... `image_16`) boyunca en fazla 16 görsel. Toplu işlenmiş bir görsel, her görsel için bir kez sayılır. | IMAGE | Hayır | 16 görsele kadar |
| `audio` | Sınıflandırılacak ses klibi. | AUDIO | Hayır | - |
| `video` | Sınıflandırılacak video klibi. | VIDEO | Hayır | - |
| `text` | Sorunun hakkında olduğu metin; istem veya LLM yanıtı gibi, en fazla 20000 karakter. | STRING | Hayır | 20000 karaktere kadar |

En az 2, en fazla 255 seçenek verin ve hiçbirini iki kez listelemeyin; aksi halde düğüm bir hata verir. `text`, `images`, `audio` veya `video` girdilerinden en az birini bağlayın ve soru içinde birden fazla görseli `image_1`, `image_2` vb. şekilde adlandırın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `choice` | Seçilen seçenek, tam olarak `options` içinde yazıldığı gibi. | STRING |
| `option_index` | Seçilen seçeneğin `options` içindeki konumu, 0'dan başlayarak. | INT |
| `confidence` | Seçime ilişkin güven değeri, 0 ile 1 arasında. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionChoice/tr.md)

---
**Source fingerprint (SHA-256):** `200c63a9197cd95ba0a21da88c5f3117014b37b0651541094a775219381afe43`
