# ByteDance Metinden Videoya

ByteDance Metinden Videoya düğümü, metin istemlerine dayalı olarak bir API aracılığıyla ByteDance modellerini kullanarak videolar oluşturur. Giriş olarak bir metin açıklaması ve çeşitli video ayarlarını alır, ardından sağlanan özelliklerle eşleşen bir video oluşturur. Düğüm, API iletişimini yönetir ve oluşturulan videoyu çıktı olarak döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Oluşturma için kullanılacak ByteDance modeli (varsayılan: `"seedance-1-0-pro-fast-251015"`). | STRING | Evet | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-t2v-250428"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | Videoyu oluşturmak için kullanılan metin istemi. | STRING | Evet | - |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. | STRING | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `en_boy_oranı` | Çıktı videosunun en-boy oranı. | STRING | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `süre` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 3 ila 12 |
| `tohum` | Oluşturma için kullanılacak tohum değeri (varsayılan: 0). | INT | Hayır | 0 ila 2147483647 |
| `sabit_kamera` | Kameranın sabitlenip sabitlenmeyeceğini belirtir. Platform, isteminize kamerayı sabitlemek için bir talimat ekler ancak gerçek etkiyi garanti etmez (varsayılan: False). | BOOLEAN | Hayır | - |
| `filigran` | Videoya "AI tarafından oluşturuldu" filigranı eklenip eklenmeyeceği (varsayılan: False). | BOOLEAN | Hayır | - |
| `ses_oluştur` | Bu parametre, `seedance-1-5-pro-251215` dışındaki tüm modeller için yok sayılır (varsayılan: False). | BOOLEAN | Hayır | - |

**Parametre Kısıtlamaları:**

- `prompt` parametresi, boşluklar kaldırıldıktan sonra en az 1 karakter içermelidir.
- `prompt` parametresi şu metin parametrelerini içeremez: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- `duration` parametresi 3 ile 12 saniye arasındaki değerlerle sınırlıdır. `seedance-1-5-pro-251215` modeli için desteklenen minimum süre 4 saniyedir.
- `seed` parametresi 0 ile 2.147.483.647 arasında değerler kabul eder.
- `generate_audio` parametresi yalnızca `model` `seedance-1-5-pro-251215` olarak ayarlandığında etkilidir; diğer tüm modeller için yok sayılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Oluşturulan video dosyası | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `44ea3e40b99b337340cc39be1c5b6c903680591f1de49b1f2e82f398979355c5`
