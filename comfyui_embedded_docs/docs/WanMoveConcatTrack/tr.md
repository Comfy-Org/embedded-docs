> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/tr.md)

WanMoveConcatTrack düğümü, iki hareket izleme verisi kümesini tek, daha uzun bir dizi halinde birleştirir. Giriş izlerinden gelen iz yollarını ve görünürlük maskelerini ilgili boyutları boyunca birleştirerek çalışır. Yalnızca bir iz girişi sağlanırsa, bu veriyi değiştirmeden olduğu gibi iletir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `tracks_1` | TRACKS | Evet | | Birleştirilecek ilk hareket izleme verisi kümesi. |
| `tracks_2` | TRACKS | Hayır | | İsteğe bağlı ikinci hareket izleme verisi kümesi. Sağlanmazsa, `tracks_1` doğrudan çıktıya iletilir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `tracks` | TRACKS | Girişlerden birleştirilmiş `track_path` ve `track_visibility` içeren, birleştirilmiş hareket izleme verisi. |

---
**Source fingerprint (SHA-256):** `d9b4c00291c6fa8e17bf54ecdcd16f7f6874159fe8cebebe66568dc2a744868f`
