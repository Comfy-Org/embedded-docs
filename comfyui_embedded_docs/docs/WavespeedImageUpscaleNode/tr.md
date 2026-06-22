# WaveSpeed Görüntü Yükseltme

WaveSpeed Görüntü Yükseltme düğümü, bir görüntünün çözünürlüğünü ve kalitesini artırmak için harici bir yapay zeka hizmeti kullanır. Tek bir giriş fotoğrafı alır ve bunu 2K, 4K veya 8K gibi daha yüksek bir hedef çözünürlüğe yükselterek daha keskin ve daha ayrıntılı bir sonuç üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Yükseltme için kullanılacak yapay zeka modeli. "SeedVR2" ve "Ultimate" farklı kalite ve fiyatlandırma seviyeleri sunar. | STRING | Evet | `"SeedVR2"`<br>`"Ultimate"` |
| `görüntü` | Yükseltilecek giriş görüntüsü. | IMAGE | Evet |  |
| `hedef_çözünürlük` | Yükseltilmiş görüntü için istenen çıktı çözünürlüğü. | STRING | Evet | `"2K"`<br>`"4K"`<br>`"8K"` |

**Not:** Bu düğüm tam olarak bir adet giriş görüntüsü gerektirir. Birden fazla görüntüden oluşan bir grup sağlanması hataya neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Yükseltilmiş, yüksek çözünürlüklü çıktı görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedImageUpscaleNode/tr.md)

---
**Source fingerprint (SHA-256):** `b14056f981f6e34c67d8126391acc11878f92f5f406559afbac803c86da42bcc`
