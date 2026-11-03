# ByteDance Metinden Videoya

ByteDance Text to Video düğümü, ByteDance modellerini kullanarak bir API aracılığıyla metin istemine dayalı bir video oluşturur. Bir istem sağlarsınız ve model, çözünürlük, en boy oranı ve süre gibi ayarları seçersiniz; düğüm, üretim isteğini gönderir ve oluşturulan videoyu döndürür.

**Not:** BytePlus, Seedance 1.5 Pro modelini 11 Kasım 2026'da kapatıyor; bu nedenle bu düğüm artık onu sunmuyor ve onunla kaydedilen iş akışları çalışmayı durduruyor. Bunun yerine `seedance-1-0-pro-250528`, `seedance-1-0-pro-fast-251015` veya [Seedance 2.5 iş ortağı düğümü](https://docs.comfy.org/tr/tutorials/partner-nodes/bytedance/seedance-2-5) kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Videoyu oluşturmak için kullanılan ByteDance modeli (varsayılan: `"seedance-1-0-pro-fast-251015"`). | COMBO | Evet | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | Videoyu oluşturmak için kullanılan metin istemi. | STRING | Evet | - |
| `çözünürlük` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `en_boy_oranı` | Çıktı videosunun en boy oranı. | COMBO | Evet | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `süre` | Çıktı videosunun süresi (saniye cinsinden) (varsayılan: 5). | INT | Evet | 3 ila 12 |
| `tohum` | Üretim için kullanılacak tohum (varsayılan: 0). | INT | Hayır | 0 ila 2147483647 |
| `sabit_kamera` | Kameranın sabitlenip sabitlenmeyeceğini belirtir. Platform, isteminize kamerayı sabitlemek için bir talimat ekler ancak gerçek etkiyi garanti etmez (varsayılan: False). | BOOLEAN | Hayır | - |
| `filigran` | Videoya "AI generated" filigranı eklenip eklenmeyeceğini belirtir (varsayılan: False). | BOOLEAN | Hayır | - |
| BOOLEAN | Hayır | - |

**Parametre Kısıtlamaları:**

- `prompt` parametresi, boşluk karakterleri kaldırıldıktan sonra en az 1 karakter içermelidir.
- `prompt` parametresi şu metin parametrelerini içeremez: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- Düğüm, son istemi, seçilen `resolution`, `aspect_ratio`, `duration`, `seed`, `camera_fixed` ve `watermark` ayarlarını istem metnine ekleyerek oluşturur.
- `duration` parametresi 3 ila 12 saniye arasındaki değerlerle sınırlıdır.
- `seed` parametresi 0 ile 2,147,483,647 arasındaki değerleri kabul eder.
- `generate_audio` parametresi uyumluluk için kabul edilir, ancak kalan modeller onu yok sayar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dosyası | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `83b805b63e59a76cae378b0407b409e1bfe900677ef1e01fc836fede47283eee`
