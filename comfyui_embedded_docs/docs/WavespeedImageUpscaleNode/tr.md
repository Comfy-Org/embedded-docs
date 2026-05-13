> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedImageUpscaleNode/tr.md)

WaveSpeed Görüntü Yükseltme düğümü, bir görüntünün çözünürlüğünü ve kalitesini artırmak için harici bir yapay zeka hizmeti kullanır. Tek bir giriş fotoğrafı alır ve bunu 2K, 4K veya 8K gibi daha yüksek bir hedef çözünürlüğe yükselterek daha keskin ve daha ayrıntılı bir sonuç üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | STRING | Evet | `"SeedVR2"`<br>`"Ultimate"` | Yükseltme için kullanılacak yapay zeka modeli. "SeedVR2" ve "Ultimate" farklı kalite ve fiyatlandırma seviyeleri sunar. |
| `image` | IMAGE | Evet | | Yükseltilecek giriş görüntüsü. |
| `target_resolution` | STRING | Evet | `"2K"`<br>`"4K"`<br>`"8K"` | Yükseltilmiş görüntü için istenen çıktı çözünürlüğü. |

**Not:** Bu düğüm tam olarak bir adet giriş görüntüsü gerektirir. Birden fazla görüntüden oluşan bir grup sağlanması hataya neden olur.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `image` | IMAGE | Yükseltilmiş, yüksek çözünürlüklü çıktı görüntüsü. |

---
**Source fingerprint (SHA-256):** `b14056f981f6e34c67d8126391acc11878f92f5f406559afbac803c86da42bcc`
