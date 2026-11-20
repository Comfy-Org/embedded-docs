# Google Gemini Decision (Yes/No)

Bağladığınız metin, görseller, ses veya video hakkında evet/hayır sorusu sorun ve yönlendirme için bir boolean değer alın. Çalışmayı iki yoldan birine göndermek için `result` değerini bir If/Else Switch düğümüne bağlayın; modelin neden bu şekilde yanıt verdiğini görmek istediğinizde `answer` ve `probability` değerlerini okuyun.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model (varsayılan: `"gemini-decision-1"`). | COMBO | Evet | `"gemini-decision-1"` |
| `question` | Bağlı olan şey hakkında evet/hayır sorusu, en fazla 5000 karakter. "Evet"in üzerinde işlem yapacağınız durum olacak şekilde sorun (varsayılan: "Is there a person in the image?"). | STRING | Evet | 1 ile 5000 karakter arası |
| `threshold` | `result` değerinin true olduğu "evet" olasılığı. Net evet yanıtları yaklaşık 0.85 ile 0.92 arasında puan alır; bu nedenle 0.9 veya daha yüksek bir değer bunların çoğunu reddeder (varsayılan: 0.5). | FLOAT | Evet | 0.01 ile 0.99 arası (adım: 0.01) |
| `images` | Hakkında soru sorulacak görseller, büyütülebilir yuvalar genelinde en fazla 16 tane (`image_1` ... `image_16`). Toplu bir görsel, görsel başına bir kez sayılır. | IMAGE | Hayır | En fazla 16 görsel |
| `audio` | Hakkında soru sorulacak ses klibi. | AUDIO | Hayır | - |
| `video` | Hakkında soru sorulacak video klibi. | VIDEO | Hayır | - |
| `text` | Sorunun hakkında olduğu metin; örneğin bir istem veya bir LLM yanıtı, en fazla 20000 karakter. | STRING | Hayır | En fazla 20000 karakter |

`text`, `images`, `audio` veya `video` değerlerinden en az birini bağlayın; bakılacak hiçbir şey olmadığında düğüm hata verir. Birden fazla görsel varsa, soru içinde bunları `image_1`, `image_2` vb. olarak adlandırın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `result` | Yanıtın boolean olarak karşılığı: "evet" için true, "hayır" için false. | BOOLEAN |
| `answer` | `"yes"` veya `"no"` dizesi olarak yanıt. | STRING |
| `probability` | 0 ile 1 arasında "evet" olasılığı. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/tr.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`
