# Reve Görsel Remix

Reve Image Remix düğümü, Reve API'sini kullanarak yeni bir görüntü oluşturur. Bir veya daha fazla referans görüntüyü bir metin istemiyle birleştirerek, sağlanan açıklamaya dayalı yeni, yeniden karıştırılmış bir görüntü oluşturur.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `referans_görseller` | Remix için temel olarak kullanılacak bir veya daha fazla referans görüntü. 1 ile 6 arasında görüntü ekleyebilirsiniz. | IMAGE | Evet | 1 ila 6 görüntü |
| `prompt` | İstenen görüntünün metin açıklaması. Belirli görüntülere indeksleriyle başvurmak için XML `<img>` etiketleri ekleyebilirsiniz (örneğin, `<img>0</img>`, `<img>1</img>`). (varsayılan: boş) | STRING | Evet | 1 ila 2560 karakter |
| `model` | Remix için kullanılacak model sürümü. Her model seçeneği, yapılandırılabilir en boy oranları ve test zamanı ölçeklendirme içerir. | COMBO | Evet | `reve-remix@20250915`<br>`reve-remix-fast@20251030` |
| `upscale` | Oluşturulan görüntünün yükseltilip yükseltilmeyeceğini kontrol eder. Etkinleştirildiğinde, bir yükseltme faktörü seçebilirsiniz. | COMBO | Hayır | `"disabled"`<br>`"enabled"` |
| `remove_background` | Etkinleştirildiğinde, oluşturulan görüntüden arka planı kaldırmaya çalışır. | BOOLEAN | Hayır | `true`<br>`false` |
| `seed` | Bir tohum değeri. Bu değeri değiştirmek düğümün yeniden çalışmasına neden olur, ancak tohumdan bağımsız olarak sonuçlar deterministik değildir. (varsayılan: 0) | INT | Hayır | 0 ila 2147483647 |

**Not:** `model` parametresi, `aspect_ratio` (seçenekler: "auto", "16:9", "9:16", "3:2", "2:3", "4:3", "3:4", "1:1") ve `test_time_scaling` için iç içe ayarlar içeren dinamik bir kombinasyondur. `upscale` parametresi "enabled" olarak ayarlandığında, iç içe bir `upscale_factor` ayarını ortaya çıkarır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Reve remix işlemi tarafından oluşturulan yeni görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/tr.md)

---
**Source fingerprint (SHA-256):** `e64dccddfd55ebaa7e28bf17c2a5ff1a0c130db1475e307940b75106c788f687`
