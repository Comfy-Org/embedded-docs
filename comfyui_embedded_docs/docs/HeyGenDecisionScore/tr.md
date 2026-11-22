# HeyGen Decision (Score)

Bağladığınız metni, görüntüleri, sesi veya videoyu 1 ile 10 arasında puanlayın; puanı ve belirlediğiniz eşikte değişen bir boolean değerini alın. Çıktıları filtrelemek veya sıralamak için kullanın ve puana göre işlem yapmak için `result` çıktısını bir If/Else Switch düğümüne bağlayın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. `heygen-decision-1-turbo`, `heygen-decision-1`'e göre daha hızlıdır ve daha az maliyetlidir (varsayılan: `"heygen-decision-1"`). | COMBO | Evet | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `soru` | Neyin puanlanacağı; 1 ve 10'un ne anlama geldiğini belirtin (varsayılan: "Rate the technical quality of the image from 1 (worst) to 10 (best)."). | STRING | Evet | 1 ile 5000 karakter arası |
| `eşik` | `result`, puan en az bu değer olduğunda true olur. Temiz, keskin görüntüler yaklaşık 7 puan alır; ciddi şekilde hasar görmüş olanlar yaklaşık 3 ila 5 puan alır (varsayılan: 6.0). | FLOAT | Evet | 1.0 ile 10.0 arası (adım: 0.1) |
| `görüntüler` | Puanlanacak görüntüler; bir toplu işlemin her karesi sayıldığında toplamda en fazla 4 görüntü. Soketler boyunca sırayla `image_1` ile `image_4` arasında numaralandırılırlar. | IMAGE | Hayır | En fazla 4 görsel |
| `audio_1` | Puanlanacak ses; en fazla 30 dakika. | AUDIO | Hayır | En fazla 30 dakika |
| `video_1` | Puanlanacak video; en fazla 60 saniye. | VIDEO | Hayır | En fazla 60 saniye |
| `metin` | Sorunun hakkında olduğu metin; istem veya LLM yanıtı gibi, en fazla 20000 karakter. | STRING | Hayır | En fazla 20000 karakter |

Puanlamak için en az bir girdi bağlayın ve bunları soru içinde soket adlarıyla adlandırın; örneğin "image_1 ne kadar keskin?".

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `result` | Puan en az `threshold` olduğunda true, aksi halde false. | BOOLEAN |
| `score` | 1 ile 10 arasındaki puan. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionScore/tr.md)

---
**Source fingerprint (SHA-256):** `47f7aeab15292a2156b8da23c9911f4155c5b05c9ea9c0c502c30221aa522b58`
