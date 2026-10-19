# Clarity AI Crystal Video Upscale

Clarity AI'nin Crystal Video Upscaler'ı ile videoyu yüksek kalitede büyütün; kaynağa sadık kalan yüksek doğruluklu bir büyütücüdür. Klip yüklenir, belirlediğiniz faktörle büyütülür ve video olarak döndürülür. Çıktı, kare başına 9 megapiksel (örneğin 4000x2250) ve klip başına 360 megapiksel-saniye ile sınırlıdır, bu nedenle büyük veya uzun klipler faktörün istediğinden daha düşük çözünürlükte geri döner.

Bir `model` seçmek, o modele özgü parametreleri ortaya çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. Bir model seçmek, ona özgü parametreleri ortaya çıkarır: `video` ve `scale_factor`. | DYNAMIC_COMBO | Evet | `"crystal-video-upscaler"` |
| `video` | Büyütülecek video. | VIDEO | Evet | N/A |
| `scale_factor` | Video genişliğini ve yüksekliğini çarpmak için faktör. Çıktı, kare başına 9 megapiksel ve klip başına 360 megapiksel-saniye ile sınırlıdır, bu nedenle büyük veya uzun videolar daha az büyütülür ve faktör, bir kenarı 5120 pikselin ötesine taşıyacaksa tekrar azaltılır (varsayılan: 2.0). | FLOAT | Evet | 1.0 ila 200.0 (adım 0.1) |

**Not:** Klip, her iki tarafta en fazla 5120 piksel ve kare başına en fazla 9 megapiksel olabilir. Maksimum uzunluk, kare boyutuna ve kare hızına bağlıdır: 360 megapiksel-saniyenin kare piksellerine ve 30 fps'nin katlarına yuvarlanmış kare hızına bölünmesiyle hesaplanır, bu nedenle 30 fps'de 1080p bir klip yaklaşık 173 saniyeye kadar sürebilir. 30 fps'nin üzerindeki klipler 2 kat, 60 fps'nin üzerindekiler 3 kat maliyetlidir ve bu şekilde devam eder.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Büyütülmüş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClarityCrystalVideoUpscaleNode/tr.md)

---
**Source fingerprint (SHA-256):** `ca44ed6591474421edaf7e4e99e6da62e0c2e4e66964b7dac51d45758150aaa8`
