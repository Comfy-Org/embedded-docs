# Pruna P-Video-2 Görüntüden Videoya

Pruna'nın P-Video-2 modeliyle bir görüntüyü videoya canlandırır. İlk kare zorunludur ve çıktının en-boy oranını sabitler; isteğe bağlı son kare, videonun kendisine doğru enterpolasyon yapacağı bir bitiş noktası sağlar. İstem, sahnenin nasıl hareket ettiğini açıklar ve düğüm ya kendi ses parçasını üretir ya da hareketi yönlendiren bir ses klibi alır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Pruna video modeli. Bir model seçildiğinde aşağıda kendi girdileri görünür. | DYNAMIC_COMBO | Evet | `"p-video-2"` |

### P-Video-2 Girdileri

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model.first_frame` | Videonun başladığı görüntü. Çıktı, bu görüntünün en-boy oranını korur. | IMAGE | Evet | - |
| `model.last_frame` | Videonun bittiği görüntü. En-boy oranı ilk kareninkine yakın olmalıdır. | IMAGE | Hayır | - |
| `istem` | Sahnenin nasıl hareket ettiğini ve seslendiğini açıklar. En az bir boşluk olmayan karakter içermelidir, en fazla 5000 karakter (varsayılan: boş). | STRING | Evet | En fazla 5000 karakter |
| `süre` | Videonun saniye cinsinden uzunluğu. `"auto"` modelin uzunluğu istemden seçmesini sağlar. `model.audio` bağlandığında yok sayılır: video bu durumda ses uzunluğunu izler, tam saniyeye yukarı yuvarlanır, en fazla 20 saniye (varsayılan: `"5"`). | COMBO | Evet | `"auto"`<br>`"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `çözünürlük` | Çıktı çözünürlüğü. 720p yaklaşık 0,9 megapiksel (16:9'da 1280x704), 1080p yaklaşık 2 megapiksel (16:9'da 1920x1088) oluşturur (varsayılan: `"720p"`). | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `fps` | Saniyedeki kare sayısı. 1080p'de draft ile 48 fps kullanılamaz (varsayılan: `"24"`). | COMBO | Evet | `"24"`<br>`"48"` |
| `taslak` | Daha hızlı, daha az ayrıntılı render; standart bir render'dan daha düşük ücretlendirilir (varsayılan: False). | BOOLEAN | Evet | True/False |
| `generate_audio` | Video için bir ses parçası üret. `model.audio` bağlandığında yok sayılır; bunun yerine o ses parçası olur (varsayılan: True). | BOOLEAN | Evet | True/False |
| `enhance_prompt` | Oluşturmadan önce istemi daha fazla ayrıntıyla yeniden yaz; kısa istemler buna ihtiyaç duyar. Aynı seed ile bir sonucu tam olarak yeniden üretmek için kapatın (varsayılan: True). Gelişmiş ayar. | BOOLEAN | Evet | True/False |
| `model.audio` | Hareketi yönlendiren ve ses parçası hâline gelen ses. En az 1 saniye uzunluğunda olmalıdır; 20 saniyeden uzun sesler kesilir. `model.duration` yerine video uzunluğunu belirler. | AUDIO | Hayır | - |
| `tohum` | Üretim için seed. Aynı seed, bir sonucu yalnızca `model.enhance_prompt` kapalıyken tam olarak yeniden üretir (varsayılan: 42). | INT | Evet | 0 - 2147483647 |

**Notlar:**

- `model.first_frame` zorunludur ve çıktının en-boy oranını sabitler, bu nedenle bu düğümde en-boy oranı girdisi yoktur.
- `model.last_frame` isteğe bağlıdır, ancak en-boy oranı ilk kareninkine yakın olmalıdır; aksi hâlde düğüm bir hata verir.
- `model.prompt` zorunludur ve 5000 karakterle sınırlıdır.
- 1080p'de draft, 48 fps ile birleştirilemez: düğüm bir hata verir, bu nedenle ya draft'ı kapatın ya da 24 fps kullanın.
- Bağlanan ses en az 1 saniye uzunluğunda olmalıdır; 20 saniyeyi aşan her şey yok sayılır.
- `model.audio` bağlıyken ses, video uzunluğunu belirler; bu nedenle `model.duration` ve `model.generate_audio` etkisizdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Oluşturulan video, ses parçasıyla birlikte. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `da8952e478eee593543fa7ae1aa329ad5bd5078024f905cdba185d18e76db130`
