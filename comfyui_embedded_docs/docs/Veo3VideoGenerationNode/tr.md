# Google Veo 3 Video Oluşturma

Google'ın Veo 3 API'sini kullanarak metin istemlerinden videolar üretir. Bu düğüm; fast ve lite varyantları dahil birden fazla Veo 3 modelini destekler ve video çözünürlüğü, süresi ve ses üretimini belirlemenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | Videonun metin açıklaması (varsayılan: "") | STRING | Evet | - |
| `en_boy_oranı` | Çıktı videosunun en-boy oranı (varsayılan: "16:9") | COMBO | Evet | "16:9"<br>"9:16" |
| `çözünürlük` | Çıktı video çözünürlüğü. 4K, veo-3.1-lite modeli için kullanılamaz. (varsayılan: "720p") | COMBO | Hayır | "720p"<br>"1080p"<br>"4k" |
| `negatif_istem` | Videoda nelerden kaçınılacağını belirleyen negatif metin istemi (varsayılan: "") | STRING | Hayır | - |
| `süre_saniye` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 8) | INT | Hayır | 4 - 8 (adım 2) |
| `istem_geliştir` | Bu parametre kullanımdan kaldırılmıştır ve yok sayılır. (varsayılan: True) | BOOLEAN | Hayır | - |
| `kişi_oluşturma` | Videoda kişi üretimine izin verilip verilmeyeceği (varsayılan: "ALLOW") | COMBO | Hayır | "ALLOW"<br>"BLOCK" |
| `tohum` | Video üretimi için tohum (0 rastgele demektir) (varsayılan: 0) | INT | Hayır | 0 - 4294967295 |
| `görsel` | Video üretimini yönlendirmek için isteğe bağlı referans görseli | IMAGE | Hayır | - |
| `model` | Video üretimi için kullanılacak Veo 3 modeli (varsayılan: "veo-3.1-generate") | COMBO | Hayır | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite" |
| `ses_oluştur` | Video için ses üretin. Tüm Veo 3 modelleri tarafından desteklenir. (varsayılan: False) | BOOLEAN | Hayır | - |

**Not:** `enhance_prompt` parametresi kullanımdan kaldırılmıştır ve değeri yok sayılır. Düğüm, istemi her zaman dahili olarak geliştirir. veo-3.1-lite modeli ile "4k" çözünürlük seçerseniz düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Üretilen video dosyası | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/tr.md)

---
**Source fingerprint (SHA-256):** `5320736448ad854e2f93e08ccaa870e977e06497666cb305f314bc76ff917740`
