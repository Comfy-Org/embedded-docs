# HeyGen Decision (Choice)

Metin, görüntü, ses veya video için kendi seçeneklerinizden birini seçin ve seçilen seçeneği, konumunu ve bir güven değerini alın. `choice` çıktısını, girdileri aynı seçenek adlarını taşıyan bir Branch düğümüne bağlayın veya `option_index` üzerinden yönlendirin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. `heygen-decision-1-turbo`, `heygen-decision-1`'den daha hızlıdır ve daha az maliyetlidir (varsayılan: `"heygen-decision-1"`). | COMBO | Evet | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | Seçeneklerin yanıtladığı soru, en fazla 5000 karakter (varsayılan: "What style is the image?"). | STRING | Evet | 1 ile 5000 karakter arası |
| `options` | Her satırda bir seçenek, tam olarak yazıldığı gibi kullanılır, her biri en fazla 128 karakter. Hiçbirine uymayan girdiler için `other` gibi bir seçenek ekleyin (varsayılan: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Evet | 2 ile 255 seçenek arası |
| `images` | Sınıflandırılacak görüntüler, toplamda en fazla 4 adet, bir partinin her karesi sayılır. Soketler boyunca sırayla `image_1` ile `image_4` arasında numaralandırılırlar. | IMAGE | Hayır | En fazla 4 görüntü |
| `audio_1` | Sınıflandırılacak ses, en fazla 30 dakika. | AUDIO | Hayır | En fazla 30 dakika |
| `video_1` | Sınıflandırılacak video, en fazla 60 saniye. | VIDEO | Hayır | En fazla 60 saniye |
| `text` | Sorunun hakkında olduğu metin, örneğin bir istem veya bir LLM yanıtı, en fazla 20000 karakter. | STRING | Hayır | En fazla 20000 karakter |

2 ile 255 arasında seçenek verin, hiçbiri iki kez olmasın ve hiçbiri yalnızca harf büyüklüğü/küçüklüğü açısından farklı olmasın, aksi takdirde düğüm hata verir. Sınıflandırmak için en az bir girdi bağlayın ve bunları sorunun içinde soket adıyla belirtin, örneğin "image_1'de hangi mevsim gösteriliyor?".

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `choice` | Seçilen seçenek, `options` içinde yazıldığı şekliyle. | STRING |
| `option_index` | Seçilen seçeneğin `options` içindeki konumu, 0'dan başlar. | INT |
| `confidence` | Seçime duyulan güven, 0 ile 1 arasında. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionChoice/tr.md)

---
**Source fingerprint (SHA-256):** `dd21b3b8021b8917e7ee4d120471974634ae6771ff17b0f49e9460f82a2fbe78`
