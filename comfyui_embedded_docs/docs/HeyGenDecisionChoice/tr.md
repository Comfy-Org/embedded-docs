# HeyGen Decision (Choice)

Bağladığınız metin, görseller, ses veya video için kendi seçeneklerinizden birini seçin; seçilen seçeneği, konumunu ve bir güven değerini geri alın. `choice` çıktısını, girdileri aynı seçenek adlarını taşıyan bir Branch düğümüne bağlayın veya `option_index` üzerinden yönlendirin. Bir Branch düğümü en fazla 32 girdi kabul eder, bu nedenle daha büyük seçenek kümelerini `option_index` ile yönlendirin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. `heygen-decision-1-turbo`, `heygen-decision-1`'den daha hızlıdır ve daha düşük maliyetlidir (varsayılan: `"heygen-decision-1"`). | COMBO | Evet | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | Seçeneklerin yanıtladığı soru, en fazla 5000 karakter (varsayılan: "What style is the image?"). | STRING | Evet | 1 ile 5000 karakter arası |
| `options` | Her satırda bir seçenek, tam olarak yazıldığı gibi kullanılır, her biri en fazla 128 karakter. Hiçbirine uymayan girdiler için `other` gibi bir seçenek ekleyin (varsayılan: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Evet | 2 ile 255 seçenek arası |
| `images` | Sınıflandırılacak görseller, toplamda en fazla 4; bir toplu işin her karesi sayılır. Yuvalar boyunca sırayla `image_1` ile `image_4` arasında numaralandırılırlar. | IMAGE | Hayır | En fazla 4 görsel |
| `audio_1` | Sınıflandırılacak ses, en fazla 30 dakika. | AUDIO | Hayır | En fazla 30 dakika |
| `video_1` | Sınıflandırılacak video, en fazla 60 saniye. | VIDEO | Hayır | En fazla 60 saniye |
| `text` | Sorunun ilgili olduğu metin, örneğin bir istem veya bir LLM yanıtı, en fazla 20000 karakter. | STRING | Hayır | En fazla 20000 karakter |

2 ile 255 seçenek verin; hiçbiri iki kez olmasın ve hiçbiri yalnızca harf büyüklüğü/küçüklüğü bakımından farklı olmasın, aksi takdirde düğüm hata verir. Sınıflandırmak için en az bir girdi bağlayın ve soru içinde yuvalarına göre adlandırın, örneğin "image_1'de hangi mevsim gösteriliyor?".

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `choice` | Seçilen seçenek, `options` içinde yazıldığı şekilde. | STRING |
| `option_index` | Seçilen seçeneğin `options` içindeki konumu, 0'dan başlar. | INT |
| `confidence` | Seçime olan güven, 0 ile 1 arasında. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionChoice/tr.md)

---
**Source fingerprint (SHA-256):** `dd21b3b8021b8917e7ee4d120471974634ae6771ff17b0f49e9460f82a2fbe78`
