# Clarity AI Crystal Upscale

Clarity AI'nin Crystal Upscaler'ı ile bir görüntüyü yükseltin; bu, yüzleri, cildi ve ince dokuyu onarırken orijinale sadık kalan yüksek sadakatli bir yükselticidir. Görüntü Clarity AI'nin API'sine gönderilir ve yükseltilmiş sonuç bir görüntü olarak döndürülür.

Bir `model` seçmek, o modele özgü parametreleri gösterir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. Bir model seçmek, ona özgü parametreleri gösterir: `image`, `scale_factor` ve `creativity`. | DYNAMIC_COMBO | Evet | `"crystal-upscaler"` |
| `image` | Yükseltilecek görüntü. Tam olarak bir görüntü içermelidir; görüntü grupları desteklenmez. | IMAGE | Evet | N/A |
| `scale_factor` | Görüntü genişliğinin ve yüksekliğinin çarpılacağı katsayı. Çıktı 100 megapiksel ile sınırlıdır (varsayılan: 2.0). | FLOAT | Evet | 1.0 - 200.0 (adım 0.1) |
| `creativity` | Daha yüksek değerler, modelin orijinali katı biçimde korumak yerine daha fazla ayrıntıyı yeniden oluşturmasını sağlar. Kısa kenarı 256 piksel veya daha az olan görüntülerde etkisi yoktur (varsayılan: 0). | INT | Evet | 0 - 10 |

**Not:** Girdi görüntüsü en az 2x2 piksel olmalıdır. Çıktı 100 megapiksel ve kenar başına 65535 piksel ile sınırlandırılmıştır; daha büyük bir sonuç hata verir, bu nedenle daha küçük bir görüntü veya daha düşük bir `scale_factor` kullanın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Yükseltilmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClarityCrystalUpscaleNode/tr.md)

---
**Source fingerprint (SHA-256):** `38c90cf7054a93477ee63c356c3fdf8ba38c7edaf1a337da7ac366cd9d746d9e`
