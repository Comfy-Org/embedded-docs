# Google Gemini Decision (Score)

Bağladığınız metni, görüntüleri, sesi veya videoyu 1'den 10'a kadar puanlayın ve puanla birlikte belirlediğiniz eşik değerinde değişen bir boolean değeri alın. Bunu çıktıları filtrelemek veya sıralamak için kullanın; örneğin yalnızca en az 7 puan alan görüntüleri tutmak için ve `result` çıktısını bir If/Else Switch düğümüne bağlayarak işlem yapmak için. Tek bir çalıştırma, bağladığınız şeyin tamamını puanlar, bu nedenle tek tek görüntüleri filtrelemek için onları birer birer puanlamanız gerekir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model (varsayılan: `"gemini-decision-1"`). | COMBO | Evet | `"gemini-decision-1"` |
| `question` | Neyin puanlanacağı; 1 ve 10'un ne anlama geldiğini belirtin (varsayılan: "Rate the technical quality of the image from 1 (worst) to 10 (best)."). | STRING | Evet | 1 ile 5000 karakter arası |
| `threshold` | `result`, puan en az bu değer olduğunda true olur. Temiz, keskin görüntüler yaklaşık 7 ila 8 puan alır, ciddi şekilde hasar görmüş olanlar yaklaşık 3 ila 5 (varsayılan: 6.0). | FLOAT | Evet | 1.0 ile 10.0 arası (adım: 0.1) |
| `images` | Puanlanacak görüntüler, büyütülebilir yuvalar (`image_1` ... `image_16`) boyunca en fazla 16 adet. Toplu bir görüntü, her görüntü için bir kez sayılır. | IMAGE | Hayır | 16 görsele kadar |
| `audio` | Puanlanacak ses klibi. | AUDIO | Hayır | - |
| `video` | Puanlanacak video klibi. | VIDEO | Hayır | - |
| `metin` | Sorunun hakkında olduğu metin; bir istem veya LLM yanıtı gibi, en fazla 20000 karakter. | STRING | Hayır | 20000 karaktere kadar |

`text`, `images`, `audio` veya `video`'dan en az birini bağlayın; puanlanacak bir şey olmadığında düğüm hata verir. Birden çok görüntü varsa, bunları soru içinde `image_1`, `image_2` vb. olarak adlandırın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `result` | Puan en az `threshold` olduğunda true, aksi halde false. | BOOLEAN |
| `score` | 1'den 10'a kadar puan. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionScore/tr.md)

---
**Source fingerprint (SHA-256):** `9b0a68cc7f29b1d4d23e23e051a008f34932aac6d1fe1a16e45a0e70b4df412f`
