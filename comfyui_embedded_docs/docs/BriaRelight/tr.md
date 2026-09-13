# BriaRelight

Bu düğüm, Bria kullanarak bir görüntünün ışık atmosferini ve yönünü değiştirir. Görüntü Bria tarafından yeniden oluşturulur, bu nedenle sonuç girdiyle piksel hizalı değildir; tüm kare yaklaşık 1 megapikselde yeniden üretilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Işığı değiştirilecek görüntü. Görüntü yüklenmeden önce varsa alfa kanalı kaldırılır. | IMAGE | Evet | - |
| `light_type` | Uygulanacak ışık atmosferi. | COMBO | Evet | `"midday"`<br>`"blue hour light"`<br>`"low-angle sunlight"`<br>`"sunrise light"`<br>`"spotlight on subject"`<br>`"overcast light"`<br>`"soft overcast daylight lighting"`<br>`"cloud-filtered lighting"`<br>`"fog-diffused lighting"`<br>`"moonlight lighting"`<br>`"starlight nighttime"`<br>`"soft bokeh lighting"`<br>`"harsh studio lighting"` |
| `light_direction` | Işığın nereden geldiği. midday, spotlight on subject ve harsh studio lighting gibi sert ışık atmosferleri buna en çok tepki verir. | COMBO | Evet | `"front"`<br>`"side"`<br>`"bottom"`<br>`"top-down"` |
| `moderation` | Moderasyon ayarları. Moderasyon seçeneklerini göstermek için `"true"` seçin veya moderasyon olmadan çalıştırmak için `"false"` seçin. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |

### Moderasyon Girdileri

Bu seçenekler `moderation` `"true"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Girdi görüntüsünde içerik moderasyonunu etkinleştirir. Varsayılan: false. | BOOLEAN | Hayır | `true`<br>`false` |
| `visual_output_moderation` | Oluşturulan çıktı görüntüsünde içerik moderasyonunu etkinleştirir. Varsayılan: false. | BOOLEAN | Hayır | `true`<br>`false` |

Not: Bria tüm kareyi yaklaşık 1 megapikselde yeniden işler, bu nedenle sonuç girdiyle piksel hizalı değildir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Bria tarafından döndürülen yeniden ışıklandırılmış görüntü. | IMAGE |
| `structured_prompt` | Düzenlenen görüntünün yapılandırılmış açıklaması; Bria FIBO Image Edit ile sonraki bir düzenleme için. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRelight/tr.md)

---
**Source fingerprint (SHA-256):** `21fbe2186c99a7e8d99d5659ac25c3ab1a757492916dba4135487d4b293cb4f6`
