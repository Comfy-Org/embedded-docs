# Google Gemini Decision (Choice)

Bağladığınız metin, görüntüler, ses veya video için kendi seçeneklerinizden birini seçin ve seçilen seçeneği, konumunu ve güven değerini geri alın. `choice` çıktısını, girdileri aynı seçenek adlarını taşıyan bir Branch düğümüne bağlayın veya bir Branch düğümü yoksa `option_index` üzerinden yönlendirin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model (varsayılan: `"gemini-decision-1"`). | COMBO | Evet | `"gemini-decision-1"` |
| `question` | Seçeneklerin yanıtladığı soru, en fazla 5000 karakter (varsayılan: "What style is the image?"). | STRING | Evet | 1 ile 5000 karakter arası |
| `options` | Her satırda bir seçenek, tam olarak yazıldığı gibi kullanılır, her biri en fazla 128 karakter. Bunların hiçbirine uymayan girdiler için `other` gibi bir seçenek ekleyin (varsayılan: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Evet | 2 ile 255 seçenek arası |
| `images` | Sınıflandırılacak görüntüler; büyütülebilir yuvalar (`image_1` ... `image_16`) genelinde en fazla 16 adet. Toplu işlenen bir görüntü kümesindeki her görüntü ayrı ayrı sayılır. | IMAGE | Hayır | En fazla 16 görüntü |
| `audio` | Sınıflandırılacak ses klibi. | AUDIO | Hayır | - |
| `video` | Sınıflandırılacak video klibi. | VIDEO | Hayır | - |
| `text` | Sorunun hakkında olduğu metin; bir istem veya bir LLM yanıtı gibi, en fazla 20000 karakter. | STRING | Hayır | En fazla 20000 karakter |

En az 2, en fazla 255 seçenek girin ve hiçbirini iki kez listelemeyin; aksi takdirde düğüm hata verir. `text`, `images`, `audio` veya `video` girdilerinden en az birini bağlayın; birden çok görüntü kullanıyorsanız bunları soru içinde `image_1`, `image_2` vb. şekilde adlandırın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `choice` | Seçilen seçenek, `options` içinde yazıldığı şekliyle tam olarak. | STRING |
| `option_index` | Seçilen seçeneğin `options` içindeki konumu, 0'dan başlar. | INT |
| `confidence` | Seçime duyulan güven, 0 ile 1 arasında. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionChoice/tr.md)

---
**Source fingerprint (SHA-256):** `200c63a9197cd95ba0a21da88c5f3117014b37b0651541094a775219381afe43`
