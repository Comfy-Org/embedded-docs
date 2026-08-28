# TripoSplat Ön İşlem Görüntüsü

Bu düğüm, her giriş görüntüsünü siyah bir arka plan üzerinde ortalanmış bir kare olacak şekilde kırpar ve belirtilen çıktı boyutuna ulaşmak için dolgu (padding) ekler. TripoSplat 3D modeli için görüntüleri hazırlamak amacıyla tutarlı kare çerçeveleme ve kenar bozulmalarını önlemek için isteğe bağlı alfa mat aşındırması sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Ön işlenecek giriş görüntüsü/görüntüleri. | IMAGE | Evet | - |
| `mask` | Görüntü için alfa maskesi; kırpma bölgesini belirlemek için kullanılır. | MASK | Evet | - |
| `aşındırma_yarıçapı` | Kırpmadan önce alfa matını bu piksel yarıçapı kadar aşındırır (kenar taşmasını önler). Varsayılan: 1. Aşındırmayı devre dışı bırakmak için 0 olarak ayarlayın. | INT | Evet | 0 ile 16 |
| `boyut` | Kare görüntü boyutu. Model 1024 ile eğitilmiştir; diğer boyutlar çalışır ancak dağılım dışıdır. Varsayılan: 1024. | INT | Evet | 256 ile 4096 (step of 16) |

**Not:** `mask` girdisi zorunludur ve sağlanmalıdır. Maskenin parti boyutu görüntüden farklıysa, eşleşecek şekilde otomatik olarak tekrarlanır. Maske boyutları görüntü boyutlarından farklıysa, maske çift doğrusal enterpolasyon kullanılarak görüntüyle eşleşecek şekilde yeniden boyutlandırılır. Çıktı boyutu, DINOv3 patch ve Flux2 VAE stride gereksinimleriyle uyumluluğu sağlamak için otomatik olarak 16'nın en yakın katına (minimum 16) yuvarlanır. Düğüm, maske hiçbir ön plan pikseli içermiyorsa (boş maske) bir hata verir. `erode_radius` 0 olduğunda aşındırma uygulanmaz. Kare kırpma, maskenin alfa sınırlayıcı kutusuna ortalanır ve daha büyük sınırlayıcı kutu boyutunun 1,2 katı olacak şekilde boyutlandırılır; görüntü sınırlarının dışında kalan her alan siyahla doldurulur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `görüntü` | İstenen `size` çözünürlüğünde, siyah arka plan üzerinde ortalanmış kare şeklinde kırpılmış ve dolgu eklenmiş ön işlenmiş görüntü(ler). | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/tr.md)

---
**Source fingerprint (SHA-256):** `ec66941846398ee6637576b11ae9d2f9576f6b05ed2ef730cdbf99a68fe9b838`
