# Google Gemini Decision (Yes/No)

Bağladığınız metin, görüntü, ses veya video hakkında evet/hayır sorusu sorun ve yönlendirme için bir boolean elde edin. Çalıştırmayı iki yoldan birine göndermek için `result` çıktısını bir If/Else Switch düğümüne bağlayın; modelin neden bu şekilde yanıt verdiğini görmek istediğinizde `answer` ve `probability` çıktılarını okuyun.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model (varsayılan: `"gemini-decision-1"`). | COMBO | Evet | `"gemini-decision-1"` |
| `soru` | Bağlanan içerikle ilgili evet/hayır sorusu, 5000 karaktere kadar. Soruyu, "yes"in üzerinde işlem yapacağınız durum olacağı şekilde sorun (varsayılan: "Is there a person in the image?"). | STRING | Evet | 1 ile 5000 karakter arası |
| `eşik` | `result` değerinin true olacağı "yes" olasılığı. Belirgin "yes" yanıtları yaklaşık 0.85 ile 0.92 arasında puan alır; bu nedenle 0.9 veya daha yüksek bir değer bunların çoğunu reddeder (varsayılan: 0.5). | FLOAT | Evet | 0.01 ile 0.99 arası (adım: 0.01) |
| `görseller` | Hakkında soru sorulacak görüntüler; büyütülebilir yuvalar (`image_1` ... `image_16`) boyunca en fazla 16 adet. Toplu görüntü, her görüntü için bir kez sayılır. | IMAGE | Hayır | 16 görsele kadar |
| `ses` | Hakkında soru sorulacak ses klibi. | AUDIO | Hayır | - |
| `video` | Hakkında soru sorulacak video klibi. | VIDEO | Hayır | - |
| `metin` | Sorunun hakkında olduğu metin; istem veya bir LLM yanıtı gibi, 20000 karaktere kadar. | STRING | Hayır | 20000 karaktere kadar |

`text`, `images`, `audio` veya `video` girdilerinden en az birini bağlayın; bakılacak bir şey yoksa düğüm hata verir. Birden fazla görüntü varsa, bunları soru içinde `image_1`, `image_2` vb. şeklinde adlandırın: bir toplu iş kare kare genişletilir; böylece numaralar, bağlantı sırasına göre yuvalar genelinde tek tek kareleri sayar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `result` | "yes" olasılığı `threshold` değerine ulaştığında true, aksi halde false. | BOOLEAN |
| `answer` | `result` ile aynı `threshold` değerini izleyen, `"yes"` veya `"no"` dizesi olarak karar. | STRING |
| `probability` | "yes" olasılığı, 0 ile 1 arasında. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/tr.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`
