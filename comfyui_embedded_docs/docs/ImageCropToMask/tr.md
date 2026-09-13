# Görüntüyü Maskeye Göre Kırp

Bir görüntüyü maskesinin sınırlayıcı kutusuna kırparak düz bir arka plan rengi üzerinde ortalanmış bir özne üretir. Düğüm, maskelenmiş görüntüyü seçilen arka plan üzerine birleştirir ve sonucu belirtilen çıktı boyutlarına yeniden boyutlandırır; bu da sabit çözünürlükte ortalanmış, arka plansız bir özne bekleyen 3B iş akışları için uygun hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `images` | Kırpılacak giriş görüntüsü veya görüntü grubu. | IMAGE | Evet | — |
| `masks` | Özne alanını tanımlayan maske veya maske grubu. Tek bir maske tüm görüntülere uygulanır; aksi halde maske grup boyutu görüntü grup boyutuyla eşleşmelidir. Maske çözünürlüğü görüntü çözünürlüğünden farklıysa, maske otomatik olarak eşleşecek şekilde yeniden boyutlandırılır. | MASK | Evet | — |
| `width` | Piksel cinsinden çıktı genişliği. (varsayılan: 1024) | INT | Evet | 64 ile 4096 (adım: 8) |
| `height` | Piksel cinsinden çıktı yüksekliği. (varsayılan: 1024) | INT | Evet | 64 ile 4096 (adım: 8) |
| `pad_factor` | Maske sınırlayıcı kutusu etrafındaki ek kenar boşluğu, çarpan olarak. (varsayılan: 1.0) | FLOAT | Evet | 1.0 ile 2.0 (adım: 0.01) |
| `grow_mask` | Kırpmadan önce maskeyi bu kadar piksel büyütün veya küçültün. Pozitif değerler maskeyi genişletir, negatif değerler daraltır. (varsayılan: 0) | INT | Evet | -32 ile 32 (adım: 1) |
| `background` | Maskelenmiş öznenin arkasındaki arka plan rengi. (varsayılan: #000000) | COLOR | Evet | — |

Not: Kırpma bölgesi maskenin sınırlayıcı kutusu üzerinde ortalanır ve en-boy oranı `width` / `height` ile eşleşir. Düğüm, ters çevrilmiş bir maskeyi (kenar boyunca ön plan pikselleri, merkezde arka plan) otomatik olarak algılar ve düzeltir. Maske hiç ön plan pikseli içermiyorsa, düğüm ters çevrilmiş maskeyi dener; bu da boşsa bir uyarı kaydeder ve tüm görüntüyü kırpar. Maske grup boyutu görüntü grup boyutuyla eşleşmediğinde ve tek bir maske olmadığında bir hata oluşur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `images` | Kırpılmış bileşik görüntüler (seçilen arka plan rengi üzerinde maskelenmiş özne), `width` x `height` boyutlarına yeniden boyutlandırılır. Grup boyutu giriş görüntü grubuyla eşleşir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropToMask/tr.md)

---
**Source fingerprint (SHA-256):** `fcc14b5db7318699526dd544d404f78f9d1ab362b73769276f113f2b1062b214`
