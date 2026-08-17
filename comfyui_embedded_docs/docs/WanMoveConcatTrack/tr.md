# WanMoveConcatTrack

WanMoveConcatTrack düğümü, iki hareket takip verisi kümesini tek ve daha uzun bir dizi halinde birleştirir. Giriş takip verilerindeki takip yollarını ve görünürlük maskelerini kendi boyutları boyunca birleştirerek çalışır. Yalnızca bir takip girişi sağlanırsa, bu veriyi değiştirmeden olduğu gibi iletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `tracks_1` | Birleştirilecek ilk hareket takip verisi kümesi. | TRACKS | Evet |  |
| `tracks_2` | İsteğe bağlı ikinci hareket takip verisi kümesi. Sağlanmazsa, `tracks_1` doğrudan çıktıya iletilir. | TRACKS | Hayır |  |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `tracks` | Girişlerden gelen birleşik `track_path` ve `track_visibility` verilerini içeren, birleştirilmiş hareket takip verisi. | TRACKS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/tr.md)

---
**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`
