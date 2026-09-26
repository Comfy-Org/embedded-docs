# Görüntü Renk Uzayını Dönüştür

ImageColorSpace düğümü, görüntüleri sRGB (Rec.709), doğrusal Rec.709, HDR (Rec.2020 HLG), HDR PQ (Rec.2020 PQ), HDR LogC3 ve HDR ACEScct renk uzayları arasında dönüştürür. LogC3, Rec.709 ana renkleriyle EI 800 eğrisini kullanır ve kodlar [0, 1] aralığına kırpılır; ACEScct ise AP1 ana renklerini ve D60 beyazını kullanır, D65'e Bradford uyarlaması yapılır. SDR çıktısına veya HDR PQ'dan HDR'a dönüştürürken, parti genelinde fazla parlaklığa ton eşlemesi uygular ve gam dışı renkleri sıkıştırır; doğrusal ve ACEScct çıktıları ile doğrusaldan HDR'a dönüşümler genişletilmiş değerleri korur. HLG ve PQ çıktıları negatif kanalları kırpar. Dönüşümler float32'de hesaplanır ve alfa kanalı varsa değiştirilmeden geçirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Dönüştürülecek giriş görüntüsü. | IMAGE | Evet | Herhangi bir geçerli görüntü. |
| `source` | Giriş piksellerinin renk uzayı. Varsayılan: "sRGB". | COMBO | Evet | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"`<br>`"HDR LogC3"`<br>`"HDR ACEScct"` |
| `destination` | Çıkış piksellerinin renk uzayı. Kaydetme düğümünü de bu aynı renk uzayına ayarlayın. EXR kaydetmeden önce LogC3 veya ACEScct'yi doğrusala, video kaydetmeden önce ise sRGB/HDR/HDR PQ'ya dönüştürün. Varsayılan: "sRGB". | COMBO | Evet | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"`<br>`"HDR LogC3"`<br>`"HDR ACEScct"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Belirtilen hedef renk uzayındaki dönüştürülmüş görüntü. | IMAGE |

## Notlar

- Doğrusal 1.0, sRGB ile aynı 203 nit referans beyazını kullanır; HLG ise 1000 nit referans ekran kullanır.
- Doğrusal ve ACEScct çıktıları genişletilmiş değerleri korur; doğrusaldan HDR'a dönüşümler ton eşleme olmadan vurguları korur.
- SDR çıktısı ve PQ'dan HLG'ye dönüşüm, parti genelinde fazla parlaklığa ton eşlemesi uygular (pozlama kare kare değişmesin diye tek bir beyaz noktası paylaşır) ve gam dışı renkleri sıkıştırır. HLG ve PQ çıktıları negatif kanalları kırpar.
- Dönüşümler float32'de hesaplanır ve ara aygıtı ve dtype'ı döndürür.
- LogC3 ve ACEScct kamera log kodlamalarıdır: EXR kaydetmek için bunları doğrusala veya video kaydetmeden önce sRGB/HDR/HDR PQ'ya dönüştürün.
- Düz alfa renk dönüşümüne uğratılmaz; yalnızca RGB kanalları dönüştürülür.
- `source` ve `destination` aynıysa, hiçbir renk dönüşümü uygulanmaz — görüntü yalnızca ara aygıta ve dtype'a taşınır.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/tr.md)

---
**Source fingerprint (SHA-256):** `fdf8b4f16a1e0c7ff9a86b8cc40f6f796175205e4b1f491b595a74a8456b9b94`
