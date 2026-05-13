> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/tr.md)

Reve Image Remix düğümü, Reve API'sini kullanarak yeni bir görüntü oluşturur. Bir veya daha fazla referans görüntüyü bir metin istemiyle birleştirerek, sağlanan açıklamaya dayalı yeni, yeniden karıştırılmış bir görüntü oluşturur.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `reference_images` | IMAGE | Evet | 1 ila 6 görüntü | Remix için temel olarak kullanılacak bir veya daha fazla referans görüntü. 1 ile 6 arasında görüntü ekleyebilirsiniz. |
| `prompt` | STRING | Evet | 1 ila 2560 karakter | İstenen görüntünün metin açıklaması. Belirli görüntülere indeksleriyle başvurmak için XML `<img>` etiketleri ekleyebilirsiniz (örneğin, `<img>0</img>`, `<img>1</img>`). (varsayılan: boş) |
| `model` | COMBO | Evet | `reve-remix@20250915`<br>`reve-remix-fast@20251030` | Remix için kullanılacak model sürümü. Her model seçeneği, yapılandırılabilir en boy oranları ve test zamanı ölçeklendirme içerir. |
| `upscale` | COMBO | Hayır | `"disabled"`<br>`"enabled"` | Oluşturulan görüntünün yükseltilip yükseltilmeyeceğini kontrol eder. Etkinleştirildiğinde, bir yükseltme faktörü seçebilirsiniz. |
| `remove_background` | BOOLEAN | Hayır | `true`<br>`false` | Etkinleştirildiğinde, oluşturulan görüntüden arka planı kaldırmaya çalışır. |
| `seed` | INT | Hayır | 0 ila 2147483647 | Bir tohum değeri. Bu değeri değiştirmek düğümün yeniden çalışmasına neden olur, ancak tohumdan bağımsız olarak sonuçlar deterministik değildir. (varsayılan: 0) |

**Not:** `model` parametresi, `aspect_ratio` (seçenekler: "auto", "16:9", "9:16", "3:2", "2:3", "4:3", "3:4", "1:1") ve `test_time_scaling` için iç içe ayarlar içeren dinamik bir kombinasyondur. `upscale` parametresi "enabled" olarak ayarlandığında, iç içe bir `upscale_factor` ayarını ortaya çıkarır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Reve remix işlemi tarafından oluşturulan yeni görüntü. |

---
**Source fingerprint (SHA-256):** `e64dccddfd55ebaa7e28bf17c2a5ff1a0c130db1475e307940b75106c788f687`
