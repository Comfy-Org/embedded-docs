# ImageCropToMask

Bir görüntüyü maskesinin sınırlayıcı kutusuna göre kırpar ve düz bir arka plan rengi üzerinde ortalanmış bir nesne üretir. Düğüm, maskelenmiş görüntüyü seçilen arka plan üzerine yerleştirir ve sonucu belirtilen çıktı boyutlarına yeniden boyutlandırarak sabit çözünürlükte ortalanmış, arka plandan arındırılmış bir nesne bekleyen 3B işlem hatları için uygun hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Kırpılacak giriş görüntüsü veya görüntü dizisi. | IMAGE | Evet | — |
| `masks` | Nesne alanını tanımlayan maske veya maske dizisi. Tek bir maske tüm görüntülere uygulanır; aksi takdirde maske dizisi boyutu, görüntü dizisi boyutuyla eşleşmelidir. Maske çözünürlüğü görüntü çözünürlüğünden farklıysa, maske otomatik olarak eşleşecek şekilde yeniden boyutlandırılır. | MASK | Evet | — |
| `width` | Piksel cinsinden çıktı genişliği. (varsayılan: 1024) | INT | Evet | 64 to 4096 (step 8) |
| `height` | Piksel cinsinden çıktı yüksekliği. (varsayılan: 1024) | INT | Evet | 64 to 4096 (step 8) |
| `pad_factor` | Maske sınırlayıcı kutusu çevresinde çarpan olarak ek kenar boşluğu. (varsayılan: 1.0) | FLOAT | Evet | 1.0 to 2.0 (step 0.01) |
| `grow_mask` | Kırpmadan önce maskeyi bu kadar piksel büyütün veya küçültün. Pozitif değerler maskeyi genişletir, negatif değerler küçültür. (varsayılan: 0) | INT | Evet | -32 to 32 (step 1) |
| `background` | Maskelenmiş nesnenin arkasındaki arka plan rengi. (varsayılan: #000000) | COLOR | Evet | — |

Not: Kırpma bölgesi, maskenin sınırlayıcı kutusuna ortalanır ve en-boy oranı `width` / `height` ile eşleşir. Düğüm, ters çevrilmiş bir maskeyi otomatik olarak algılar ve düzeltir (kenarlarda ön plan pikselleri, merkezde arka plan). Maske hiçbir ön plan pikseli içermiyorsa, düğüm ters çevrilmiş maskeyi dener; o da boşsa, bir uyarı günlüğe yazılır ve görüntünün tamamı kırpılır. Maske dizisi boyutu, görüntü dizisi boyutuyla eşleşmiyorsa ve tek bir maske değilse bir hata oluşturulur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `images` | Kırpılmış birleşik görüntüler (seçilen arka plan rengi üzerinde maskelenmiş nesne), `width` x `height` boyutuna yeniden boyutlandırılır. Dizi boyutu, giriş görüntü dizisiyle eşleşir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropToMask/tr.md)

---
**Source fingerprint (SHA-256):** `fcc14b5db7318699526dd544d404f78f9d1ab362b73769276f113f2b1062b214`
