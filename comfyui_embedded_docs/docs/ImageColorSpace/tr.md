# Görüntü Renk Uzayını Dönüştür

ImageColorSpace düğümü, görüntüleri sRGB (Rec.709), doğrusal Rec.709, HDR (Rec.2020 HLG) ve HDR PQ (Rec.2020 PQ) renk uzayları arasında dönüştürür. SDR çıktısına veya HDR PQ'dan HDR'a dönüştürme yaparken, toplu iş genelinde aşırı luminansı ton eşlemesiyle işler ve gamut dışı renkleri sıkıştırır; doğrusal çıktı ve doğrusaldan HDR'a dönüşümler, ton eşlemesi olmadan genişletilmiş değerleri korur. Dönüşümler float32'de hesaplanır ve herhangi bir alfa kanalı değiştirilmeden geçirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Dönüştürülecek giriş görüntüsü. | IMAGE | Evet | Herhangi bir geçerli görüntü. |
| `source` | Giriş piksellerinin renk uzayı. Varsayılan: "sRGB". | COMBO | Evet | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |
| `destination` | Çıkış piksellerinin renk uzayı. Kaydetme düğümünü de aynı renk uzayına ayarlayın. Varsayılan: "sRGB". | COMBO | Evet | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Belirtilen hedef renk uzayında dönüştürülmüş görüntü. | IMAGE |

## Notlar

- Doğrusal 1.0, sRGB ile aynı 203-nit referans beyazını kullanır; HLG ise 1000-nit referans ekran kullanır.
- Doğrusal çıktı ve doğrusaldan HDR'a dönüşümler, ton eşlemesi olmadan genişletilmiş değerleri korur.
- SDR çıktısı ve PQ'dan HLG'ye dönüşüm, toplu iş genelinde aşırı luminansı ton eşlemesiyle işler (pozlamanın kare kare değişmemesi için tek bir beyaz noktası paylaşır) ve gamut dışı renkleri sıkıştırır.
- Dönüşümler float32'de hesaplanır ve ara cihazı ve dtype'ı döndürür.
- Düz alfa renk dönüşümüne uğramaz; yalnızca RGB kanalları dönüştürülür.
- `source` ve `destination` aynıysa, renk dönüşümü uygulanmaz — görüntü yalnızca ara cihaza ve dtype'a taşınır.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/tr.md)

---
**Source fingerprint (SHA-256):** `04ae447a9f9805341e31755ad0fa56746ac0371fa2cb9bda95df3879c9dbead7`
