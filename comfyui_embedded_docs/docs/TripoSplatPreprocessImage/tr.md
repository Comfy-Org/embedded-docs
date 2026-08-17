# TripoSplat Ön İşlem Görüntüsü

Bu düğüm, her giriş görüntüsünü siyah bir arka plan üzerinde ortalanmış bir kareye kırpar ve ardından belirtilen çıktı boyutuna ulaşmak için dolgu ekler. TripoSplat 3D modeli için görüntüleri hazırlamak amacıyla tutarlı kare çerçeveleme ve kenar yapaylıklarını önlemek için isteğe bağlı alfa mat aşındırması sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Ön işlenecek giriş görüntüsü/görüntüleri | IMAGE | Evet | - |
| `mask` | Görüntü için alfa maskesi; kırpma bölgesini belirlemek için kullanılır | MASK | Evet | - |
| `erode_radius` | Kırpmadan önce alfa matını bu piksel yarıçapıyla aşındırır (kenar taşmasını önler). Varsayılan: 1 | INT | Evet | 0 ila 16 |
| `size` | Kare görüntü boyutu. Model 1024 ile eğitilmiştir; diğer boyutlar çalışır ancak dağılım dışıdır. Varsayılan: 1024 | INT | Evet | 256 ila 4096 (16'lık adımlarla) |

**Not:** `mask` girdisi zorunludur ve sağlanmalıdır. Maskenin batch boyutu görüntüden farklıysa, eşleşmesi için otomatik olarak tekrarlanır. Maske boyutları görüntü boyutlarından farklıysa, maske çift doğrusal enterpolasyon kullanılarak görüntüyle eşleşecek şekilde yeniden boyutlandırılır. Çıktı boyutu, DINOv3 patch ve Flux2 VAE stride gereksinimleriyle uyumluluğu sağlamak için otomatik olarak en yakın 16 katına yuvarlanır. Maske hiçbir ön plan pikseli içermiyorsa bir hata oluşturulur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Siyah bir arka plan üzerinde ortalanmış kare şeklinde kırpılmış ve dolgulanmış ön işlenmiş görüntü(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/tr.md)

---
**Source fingerprint (SHA-256):** `ec66941846398ee6637576b11ae9d2f9576f6b05ed2ef730cdbf99a68fe9b838`
