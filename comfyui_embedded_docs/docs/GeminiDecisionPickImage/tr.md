# Google Gemini Decision (Pick Image)

Bir gruptan en iyi görüntüyü seçin. Seçilen görüntüyü korumak için `index` çıktısını Get Image from Batch düğümüne bağlayın; böylece iş akışının geri kalanı yalnızca seçilen görüntü üzerinde çalışır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model` | Kullanılacak model (varsayılan: `"gemini-decision-1"`). | COMBO | Evet | `"gemini-decision-1"` |
| `question` | Hangi görüntünün seçileceği (varsayılan: "Which image best matches the prompt in text? If there is no text, which image has the best quality?"). | STRING | Evet | 1 ile 5000 karakter arası |
| `images` | Aralarından seçim yapılacak görüntüler; bir grup veya tek bir kare grubu olarak. | IMAGE | Evet | 2 ile 64 görüntü arası |
| `text` | Sorunun hakkında olduğu metin; örneğin görüntülerin oluşturulduğu istem, en fazla 20000 karakter. | STRING | Hayır | 20000 karaktere kadar |

Düğüm 2 ile 64 görüntü arası gerektirir ve tek bir görüntüde hata verir. Seçimin yalnızca görüntü kalitesine göre değil de bir isteme göre yapılması gerektiğinde `text` girişini bağlayın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `index` | Seçilen görüntünün gruptaki konumu, 0'dan başlar. | INT |
| `confidence` | Seçime ilişkin güven, 0 ile 1 arasında. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionPickImage/tr.md)

---
**Source fingerprint (SHA-256):** `55eb604923cb66b42f23f37d0c710a97033cc2c5d95880d45397bba10e44dab0`
