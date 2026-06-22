# WanMoveConcatTrack

WanMoveConcatTrack düğümü, iki hareket izleme verisi kümesini tek, daha uzun bir dizi halinde birleştirir. Giriş izlerinden gelen iz yollarını ve görünürlük maskelerini ilgili boyutları boyunca birleştirerek çalışır. Yalnızca bir iz girişi sağlanırsa, bu veriyi değiştirmeden olduğu gibi iletir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `tracks_1` | Birleştirilecek ilk hareket izleme verisi kümesi. | TRACKS | Evet |  |
| `tracks_2` | İsteğe bağlı ikinci hareket izleme verisi kümesi. Sağlanmazsa, `tracks_1` doğrudan çıktıya iletilir. | TRACKS | Hayır |  |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `tracks` | Girişlerden birleştirilmiş `track_path` ve `track_visibility` içeren, birleştirilmiş hareket izleme verisi. | TRACKS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/tr.md)

---
**Source fingerprint (SHA-256):** `d9b4c00291c6fa8e17bf54ecdcd16f7f6874159fe8cebebe66568dc2a744868f`
