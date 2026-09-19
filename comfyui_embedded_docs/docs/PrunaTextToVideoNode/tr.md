# Pruna P-Video-2 Metinden Videoya

Pruna'nın P-Video-2 modeliyle bir metin prompt'undan video üretir. Prompt; sahneyi, hareketini ve sesini tanımlar; düğüm ya kendi ses parçasını üretir ya da hareketi yönlendiren ve ses parçası hâline gelen bir ses klibi alır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak Pruna video modeli. Bir model seçmek, aşağıda kendi girdilerini gösterir. | DYNAMIC_COMBO | Evet | `"p-video-2"` |

### P-Video-2 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Videoyu, hareketini ve sesini tanımlar. En az bir boşluk dışı karakter içermelidir, en fazla 5000 karakter (varsayılan: boş). | STRING | Evet | En fazla 5000 karakter |
| `aspect_ratio` | Çıktı videosunun en-boy oranı (varsayılan: `"16:9"`). | COMBO | Evet | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"1:1"` |
| `süre` | Videonun saniye cinsinden uzunluğu. `"auto"`, modelin uzunluğu prompt'tan seçmesini sağlar. `model.audio` bağlıyken yok sayılır: video bu durumda ses uzunluğunu izler, tam saniyeye yukarı yuvarlanır, en fazla 20 saniye (varsayılan: `"5"`). | COMBO | Evet | `"auto"`<br>`"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `çözünürlük` | Çıktı çözünürlüğü. 720p yaklaşık 0,9 megapiksel (16:9'da 1280x704), 1080p yaklaşık 2 megapiksel (16:9'da 1920x1088) render eder (varsayılan: `"720p"`). | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `fps` | Saniyedeki kare sayısı. 1080p'de taslak ile 48 fps kullanılamaz (varsayılan: `"24"`). | COMBO | Evet | `"24"`<br>`"48"` |
| `taslak` | Daha hızlı, daha az ayrıntılı render; standart bir render'dan daha düşük ücretlendirilir (varsayılan: False). | BOOLEAN | Evet | True/False |
| `generate_audio` | Video için bir ses parçası üret. `model.audio` bağlıysa yok sayılır; bunun yerine o ses parçası olur (varsayılan: True). | BOOLEAN | Evet | True/False |
| `enhance_prompt` | Üretimden önce prompt'u daha fazla ayrıntıyla yeniden yaz; kısa prompt'lar buna ihtiyaç duyar. Aynı seed ile bir sonucu tam olarak yeniden üretmek için kapatın (varsayılan: True). Gelişmiş ayar. | BOOLEAN | Evet | True/False |
| `model.audio` | Hareketi yönlendiren ve ses parçası hâline gelen ses. En az 1 saniye uzunluğunda olmalıdır; 20 saniyeden uzun sesler kesilir. Video uzunluğunu `model.duration` yerine belirler. | AUDIO | Hayır | - |
| `tohum` | Üretim için seed. Aynı seed, yalnızca `model.enhance_prompt` kapalıyken bir sonucu tam olarak yeniden üretir (varsayılan: 42). | INT | Evet | 0 - 2147483647 |

**Notlar:**

- `model.prompt` gereklidir ve 5000 karakterle sınırlıdır.
- 1080p'de taslak, 48 fps ile birleştirilemez: düğüm bir hata verir; bu nedenle ya taslağı kapatın ya da 24 fps kullanın.
- Bağlanan ses en az 1 saniye uzunluğunda olmalıdır; 20 saniyeyi aşan kısım yok sayılır.
- `model.audio` bağlıyken video uzunluğunu ses belirler; bu nedenle `model.duration` ve `model.generate_audio` etkisizdir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Ses parçasıyla birlikte üretilen video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `bb7bacf2591618220c72525c1e32382174abe3a55069720adbc84fc1d8081718`
