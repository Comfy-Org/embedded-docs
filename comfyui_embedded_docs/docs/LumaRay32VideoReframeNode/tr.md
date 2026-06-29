# LumaRay32VideoReframeNode

Bu düğüm, Luma Ray 3.2 kullanarak mevcut bir videonun en boy oranını değiştirir ve yeni açılan tuval alanlarını oluşturulan içerikle doldurur. Kaynak video en fazla 30 saniye uzunluğunda olabilir ve faturalandırma çıktının saniyesi başına yapılır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|--------|
| `video` | Yeniden çerçevelenecek kaynak video. En fazla 30 saniye. | VIDEO | Evet | - |
| `prompt` | Yeni açılan tuval alanlarının nasıl doldurulması gerektiğini açıklar. | STRING | Evet | - |
| `aspect_ratio` | Yeniden çerçevelenen video için hedef en boy oranı (varsayılan: "16:9"). | STRING | Evet | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9" |
| `resolution` | Yeniden çerçevelenen videonun çıktı çözünürlüğü (varsayılan: "720p"). | STRING | Evet | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `seed` | Tekrarlanabilir üretim için tohum değeri. | INT | Evet | - |

**Not:** Yeniden çerçeveleme sırasında dikey en boy oranları (`9:16` ve `3:4`) için `1080p` çözünürlüğü kullanılamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `generation_id` | Yeni en boy oranına ve doldurulmuş tuval alanlarına sahip yeniden çerçevelenmiş video. | VIDEO |
| `generation_id` | Üretim isteği için benzersiz tanımlayıcı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoReframeNode/tr.md)

---
**Source fingerprint (SHA-256):** `d35ff5b63a850e4e44a40857188918ab5cde00b9159e3720a189a81807cfa7cb`
