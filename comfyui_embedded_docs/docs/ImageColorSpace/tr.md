# Görüntü Renk Uzayını Dönüştür

ImageColorSpace düğümü, görüntüleri sRGB (Rec.709), doğrusal Rec.709, HDR (Rec.2020 HLG), HDR PQ (Rec.2020 PQ), HDR LogC3, doğrusal ACEScg ve HDR ACEScct renk uzayları arasında dönüştürür. LogC3, Rec.709 ana renkleriyle EI 800 eğrisini kullanır ve kodlar [0, 1] aralığına kırpılır; ACEScg, D60 beyazına sahip sahne doğrusal AP1'dir ve ACEScct onun log kodlamasıdır; ikisi de Bradford uyarlamasıyla D65'e uyarlanır. SDR çıktısına veya HDR PQ'dan HDR'a dönüştürürken, parti genelinde fazla parlaklığa ton eşlemesi uygular ve gam dışı renkleri sıkıştırır; doğrusal, ACEScg ve ACEScct çıktıları ile doğrusaldan HDR'a dönüşümler genişletilmiş değerleri korur. HLG ve PQ çıktıları negatif kanalları kırpar. Dönüşümler float32'de hesaplanır ve alfa kanalı varsa değiştirilmeden geçirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Dönüştürülecek giriş görüntüsü. | IMAGE | Evet | Herhangi bir geçerli görüntü. |
| `source` | Giriş piksellerinin renk uzayı. Varsayılan: "sRGB". | COMBO | Evet | `"sRGB"`<br>`"HDR"`<br>`"HDR ACEScct"`<br>`"HDR LogC3"`<br>`"HDR PQ"`<br>`"linear"`<br>`"linear ACEScg"` |
| `destination` | Çıkış piksellerinin renk uzayı. Kaydetme düğümünü de bu aynı renk uzayına ayarlayın. ACEScg EXR kaydetmeden önce LogC3 veya ACEScct'yi doğrusal ACEScg'ye, Rec.709 EXR kaydetmeden önce doğrusala, video kaydetmeden önce ise sRGB/HDR/HDR PQ'ya dönüştürün. Varsayılan: "sRGB". | COMBO | Evet | `"sRGB"`<br>`"HDR"`<br>`"HDR ACEScct"`<br>`"HDR LogC3"`<br>`"HDR PQ"`<br>`"linear"`<br>`"linear ACEScg"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Belirtilen hedef renk uzayındaki dönüştürülmüş görüntü. | IMAGE |

## Notlar

- Doğrusal 1.0 ve ACEScg 1.0, sRGB ile aynı 203 nit referans beyazını kullanır; HLG ise 1000 nit referans ekran kullanır.
- Doğrusal, ACEScg ve ACEScct çıktıları genişletilmiş değerleri korur; doğrusaldan HDR'a dönüşümler ton eşleme olmadan vurguları korur.
- SDR çıktısı ve PQ'dan HLG'ye dönüşüm, parti genelinde fazla parlaklığa ton eşlemesi uygular (pozlama kare kare değişmesin diye tek bir beyaz noktası paylaşır) ve gam dışı renkleri sıkıştırır. HLG ve PQ çıktıları negatif kanalları kırpar.
- Dönüşümler float32'de hesaplanır ve ara aygıtı ve dtype'ı döndürür.
- LogC3 ve ACEScct kamera log kodlamalarıdır: ACEScg EXR kaydetmek için bunları doğrusal ACEScg'ye (AP1), Rec.709 EXR kaydetmek için doğrusala (Rec.709), video kaydetmeden önce ise sRGB/HDR/HDR PQ'ya dönüştürün.
- Düz alfa renk dönüşümüne uğratılmaz; yalnızca RGB kanalları dönüştürülür.
- `source` ve `destination` aynıysa, hiçbir renk dönüşümü uygulanmaz — görüntü yalnızca ara aygıta ve dtype'a taşınır.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/tr.md)

---
**Source fingerprint (SHA-256):** `cbb3452e6844985580d5b91c6b1cbfbd770307cda6c92aba8b21c9bdd45ae370`
