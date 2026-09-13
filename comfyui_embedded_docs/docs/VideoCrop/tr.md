# Videoyu Kırp

Bu düğüm, bir videoyu piksel cinsinden tanımlanan dikdörtgen bir bölgeye kırpar ve yalnızca bu dikdörtgenin içindeki alanı korur. Kırpılan sonucun geçici bir MP4 önizlemesini kaydeder ve kırpılmış videoyu çıktı olarak verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Kırpılacak kaynak video. | VIDEO | Evet | Herhangi bir video |
| `crop` | Piksel cinsinden kırpma bölgesi. Sıfır genişlik/yükseklik tam kareyi korur. Kırpma dikdörtgeni `x`, `y`, `width` ve `height` değerlerini sağlar; tümünün varsayılan değeri 0'dır. | VIDEO_EDIT | Evet | `x` ≥ 0<br>`y` ≥ 0<br>`width` ≥ 0<br>`height` ≥ 0<br>Tüm değerlerin varsayılanı 0'dır |

Not: Kırpma bölgesi piksel koordinatlarıyla tanımlanır. Genişlik ve yükseklik 0 olduğunda kırpma uygulanmaz ve düğüm tam giriş videosunu çıktı olarak verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Seçilen dikdörtgen bölgeye kırpılmış video. Kırpma genişliği ve yüksekliği 0 olduğunda çıktı, tam giriş videosudur. Kırpılan sonuç ayrıca geçici bir MP4 dosyası olarak kaydedilir ve video önizlemesi olarak gösterilir. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoCrop/tr.md)

---
**Source fingerprint (SHA-256):** `0c4ebd51027669fc232fe42a5e8840b5e4e95083b6794cd7b4c43123ddc0341b`
