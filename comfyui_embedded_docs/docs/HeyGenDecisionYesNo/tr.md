# HeyGen Decision (Yes/No)

Bağladığınız metin, görseller, ses veya video hakkında bir evet/hayır sorusu sorun ve yönlendirme için bir boolean alın. İki yol arasında seçim yapmak için `result` çıktısını bir If/Else Switch düğümüne bağlayın ve yanıtın ne kadar net olduğunu görmek için `answer` ve `probability` çıktılarını okuyun.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. `heygen-decision-1-turbo`, `heygen-decision-1`'den daha hızlıdır ve daha az maliyetlidir (varsayılan: `"heygen-decision-1"`). | COMBO | Evet | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | Bağlı olan şey hakkında evet/hayır sorusu, en fazla 5000 karakter. "yes" üzerine işlem yapacağınız durum olacak şekilde sorun (varsayılan: "Is there a person in the image?"). | STRING | Evet | 1 ile 5000 karakter arası |
| `threshold` | `result` değerinin true olduğu "yes" olasılığı; net yanıtlar 0 veya 1'e yakındır (varsayılan: 0.5). | FLOAT | Evet | 0.01 ile 0.99 arası (adım 0.01) |
| `images` | Hakkında soru sorulacak görseller, bir partinin her karesi sayılarak toplamda en fazla 4 adet. Soketler boyunca sırayla `image_1` ile `image_4` arasında numaralandırılırlar. | IMAGE | Hayır | En fazla 4 görsel |
| `audio_1` | Hakkında soru sorulacak ses, en fazla 30 dakika. | AUDIO | Hayır | En fazla 30 dakika |
| `video_1` | Hakkında soru sorulacak video, en fazla 60 saniye. | VIDEO | Hayır | En fazla 60 saniye |
| `text` | Sorunun hakkında olduğu metin, örneğin bir istem veya bir LLM yanıtı, en fazla 20000 karakter. | STRING | Hayır | En fazla 20000 karakter |

`text`, `images`, `audio_1` veya `video_1` arasından en az birini bağlayın ve soru içinde bunlara soket adıyla başvurun, örneğin "image_2, image_1 ile aynı kişiyi mi gösteriyor?".

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `result` | "yes" olasılığı `threshold` değerine ulaştığında true, aksi halde false. | BOOLEAN |
| `answer` | `"yes"` veya `"no"` dizesi olarak karar, `result` ile aynı `threshold` değerini takip eder. | STRING |
| `probability` | "yes" olasılığı, 0 ile 1 arasında. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionYesNo/tr.md)

---
**Source fingerprint (SHA-256):** `5a6a606d5c6ef62eb3424bd54a0da3dc177da7d0acf4b5c235a62b78ad8d2df1`
