> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/tr.md)

Bu düğüm, ByteDance'in Seedance 2.0 API'sini kullanarak bir metin açıklamasından video oluşturur. İsteğinizi seçilen modele gönderir, videonun işlenmesini bekler ve nihai sonucu döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Evet | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | Video oluşturma için kullanılacak model. Bir model seçmek, istem, çözünürlük, en boy oranı, süre ve ses oluşturma için ek zorunlu girdileri ortaya çıkarır. "Seedance 2.0" maksimum kalite içindir; "Seedance 2.0 Fast" hız optimizasyonu içindir. |
| `seed` | INT | Hayır | 0 ile 2147483647 arası | Bir tohum değeri (varsayılan: 0). Bu değer değişirse düğüm yeniden çalışır, ancak tohumdan bağımsız olarak sonuçlar deterministik değildir. |
| `watermark` | BOOLEAN | Hayır | True / False | Videoya filigran eklenip eklenmeyeceği (varsayılan: False). Bu gelişmiş bir ayardır. |

**Not:** `model` parametresi dinamik bir birleşik giriştir. Bir model seçtiğinizde, metin istemi, çözünürlük, en boy oranı, süre ve ses oluşturma dahil olmak üzere doldurulması gereken birkaç zorunlu alt parametreyi ortaya çıkarır. İstem metni, boşluklar kaldırıldıktan sonra en az 1 karakter uzunluğunda olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Oluşturulan video dosyası. |

---
**Source fingerprint (SHA-256):** `f8552e47667ff4b1ad3c8c1c074d70bdc45227b79b026b4b3c06986443655473`
