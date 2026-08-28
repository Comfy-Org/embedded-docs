# Topaz Video Enhance

**Topaz Video Enhance V2** düğümü, güçlü büyütme ve kurtarma teknolojisiyle videoya yeni bir soluk getirir. Farklı Topaz büyütme modellerini kullanarak videonun çözünürlüğünü artırabilir, kare enterpolasyonu ile kare hızını ayarlayabilir ve yaratıcı veya gerçekçi iyileştirme ayarları uygulayabilir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `video` | İşlenecek giriş videosu. MP4 kapsayıcı formatında olmalıdır. | VIDEO | Evet | - |
| `yükseltici_model` | Videoyu büyütmek için kullanılan yapay zeka modeli. Kullanılabilir alt parametreler seçilen modele bağlıdır. `"Disabled"` seçeneği büyütmeyi devre dışı bırakır. | DYNAMIC_COMBO | Evet | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` |
| `enterpolasyon_modeli` | Kare enterpolasyonu için kullanılan yapay zeka modeli. Kullanılabilir alt parametreler seçilen modele bağlıdır. `"Disabled"` seçeneği enterpolasyonu devre dışı bırakır. | DYNAMIC_COMBO | Evet | `"Disabled"`<br>`"apo-8"` |
| `dinamik_sıkıştırma_seviyesi` | Video sıkıştırma için kullanılan CQP seviyesi (varsayılan: `"Low"`). | COMBO | Hayır | `"Low"`<br>`"Mid"`<br>`"High"` |

Aşağıdaki bölümler, `upscaler_model` ve `interpolation_model` seçicilerinin her seçeneği için görünen alt parametreleri açıklar. `"Disabled"` seçenekleri ek parametre göstermez.

### Astra 2 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Büyütmenin hedef çıktı çözünürlüğü. | COMBO | Evet ("Astra 2" seçildiğinde) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | Büyütmenin yaratıcılık gücü (varsayılan: 0.5). | FLOAT | Hayır | 0.0 ile 1.0 (step 0.1) |
| `upscaler_model.prompt` | İsteğe bağlı tanımlayıcı (talimat içermeyen) sahne istemi. Ayarlandığında girişi 450 kareyle (~15s @ 30fps) sınırlar (varsayılan: boş). | STRING | Hayır | - |
| `upscaler_model.sharp` | Geliştirme öncesi keskinlik: 0.0=Gauss bulanıklığı, 0.5=doğrudan geçiş (varsayılan), 1.0=USM keskinleştirme. | FLOAT | Hayır | 0.0 ile 1.0 (step 0.01) |
| `upscaler_model.realism` | Çıktıyı fotoğrafik gerçekçiliğe çeker. Model varsayılanı için 0'da bırakın (varsayılan: 0.0). | FLOAT | Hayır | 0.0 ile 1.0 (step 0.01) |

### Starlight (Astra) Fast Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Büyütmenin hedef çıktı çözünürlüğü. | COMBO | Evet (bu model seçildiğinde) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### Starlight (Astra) Creative Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Büyütmenin hedef çıktı çözünürlüğü. | COMBO | Evet (bu model seçildiğinde) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | Büyütmenin yaratıcılık gücü (varsayılan: `"low"`). | COMBO | Hayır | `"low"`<br>`"middle"`<br>`"high"` |

### Starlight Precise 2.5 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Büyütmenin hedef çıktı çözünürlüğü. | COMBO | Evet (bu model seçildiğinde) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### apo-8 Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `interpolation_model.interpolation_frame_rate` | Çıktı kare hızı (varsayılan: 60). | INT | Evet ("apo-8" seçildiğinde) | 15 ile 240 |
| `interpolation_model.interpolation_slowmo` | Giriş videosuna uygulanan ağır çekim faktörü. Örneğin, 2 çıktıyı iki kat daha yavaş yapar ve süreyi ikiye katlar (varsayılan: 1). | INT | Hayır | 1 ile 16 |
| `interpolation_model.interpolation_duplicate` | Girişi yinelenen kareler için analiz eder ve bunları kaldırır (varsayılan: False). | BOOLEAN | Hayır | True<br>False |
| `interpolation_model.interpolation_duplicate_threshold` | Yinelenen kareler için algılama hassasiyeti (varsayılan: 0.01). | FLOAT | Hayır | 0.001 ile 0.1 (step 0.001) |

**Önemli Kısıtlamalar:**

- `upscaler_model` veya `interpolation_model` öğelerinden en az biri etkinleştirilmelidir. Her ikisi de `"Disabled"` olarak ayarlanırsa, işlenecek bir şey olmadığı için düğüm hata verir.
- Giriş `video` değeri MP4 kapsayıcı formatında olmalıdır.
- `"Astra 2"` modeli 9000 giriş karesiyle sınırlıdır. Bir `prompt` ayarlandığında sınır 450 giriş karesidir (~30 fps'de 15 saniye). Video geçerli sınırı aşarsa düğüm hata verir.
- `"Disabled"` dışında bir büyütme modeli seçildiğinde `upscaler_model.upscaler_resolution` gereklidir. `"FullHD (1080p)"` 1080p sonucu hedefler ve `"4K (2160p)"` 2160p sonucu hedefler; tam çıktı genişliği ve yüksekliği, giriş en-boy oranından hesaplanır, sırasıyla maksimum 1920 veya 3840 piksel uzun kenarla sınırlandırılır ve çift sayıya yuvarlanır.
- `interpolation_model` `"apo-8"` olduğunda `interpolation_model.interpolation_frame_rate` gereklidir.
- Çok büyük dosyalar şu anda desteklenmemektedir; yüklemeler tek parçayla sınırlıdır, aksi takdirde düğüm hata verir.
- Birkaç parametre (`sharp`, `realism`, `interpolation_slowmo`, `interpolation_duplicate`, `interpolation_duplicate_threshold`) arayüzde gelişmiş olarak işaretlenmiştir ve varsayılan olarak gizlenebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Seçilen büyütme ve/veya enterpolasyon filtreleri uygulandıktan sonra geliştirilmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/tr.md)

---
**Source fingerprint (SHA-256):** `14627dc772a6a46a645517bd34b545e0986a84561e24bdfe810b67f791ee47e3`
