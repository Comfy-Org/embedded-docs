# ImageCropToMask

Bir görüntüyü maskesinin sınırlayıcı kutusuna göre kırpar ve düz bir arka plan rengi üzerinde ortalanmış bir özne üretir. Düğüm, maskelenmiş görüntüyü seçilen arka plan üzerinde birleştirir ve sonucu belirtilen çıktı boyutlarına yeniden boyutlandırarak sabit çözünürlükte ortalanmış, arka plansız bir özne bekleyen 3D işlem hatları için uygun hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntüler` | Kırpılacak giriş görüntüsü veya görüntü grubu. | IMAGE | Evet | — |
| `maskeler` | Özne alanını tanımlayan maske veya maske grubu. Tek bir maske tüm görüntülere uygulanır; aksi takdirde maske grubu boyutu, görüntü grubu boyutuyla eşleşmelidir. Maske çözünürlüğü görüntü çözünürlüğünden farklıysa, maske otomatik olarak eşleşecek şekilde yeniden boyutlandırılır. | MASK | Evet | — |
| `genişlik` | Çıktı genişliği piksel cinsinden. (varsayılan: 1024) | INT | Evet | 64 ile 4096 (step 8) |
| `yükseklik` | Çıktı yüksekliği piksel cinsinden. (varsayılan: 1024) | INT | Evet | 64 ile 4096 (step 8) |
| `pad_factor` | Maske sınırlayıcı kutusu etrafındaki ek kenar boşluğu çarpanı. (varsayılan: 1.0) | FLOAT | Evet | 1.0 ile 2.0 (step 0.01) |
| `grow_mask` | Kırpmadan önce maskeyi bu kadar piksel büyütün veya küçültün. Pozitif değerler maskeyi genişletir, negatif değerler küçültür. (varsayılan: 0) | INT | Evet | -32 ile 32 (step 1) |
| `arka plan` | Maskeli öznenin arkasındaki arka plan rengi. (varsayılan: #000000) | COLOR | Evet | — |

Not: Kırpma bölgesi, maskenin sınırlayıcı kutusuna ortalanır ve en-boy oranı `width` / `height` ile eşleşir. Düğüm, ters çevrilmiş bir maskeyi (kenarlar boyunca ön plan pikselleri, merkezde arka plan) otomatik olarak algılar ve düzeltir. Maske hiçbir ön plan pikseli içermiyorsa, düğüm ters çevrilmiş maskeyi dener; bu da boşsa, bir uyarı kaydeder ve görüntünün tamamını kırpar. Maske grubu boyutu, görüntü grubu boyutuyla eşleşmediğinde ve tek bir maske olmadığında bir hata oluşturulur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `görüntüler` | Kırpılmış birleşik görüntüler (seçilen arka plan rengi üzerinde maskeli özne), `width` x `height` boyutuna yeniden boyutlandırılmıştır. Grup boyutu, giriş görüntü grubuyla eşleşir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropToMask/tr.md)

---
**Source fingerprint (SHA-256):** `fcc14b5db7318699526dd544d404f78f9d1ab362b73769276f113f2b1062b214`
