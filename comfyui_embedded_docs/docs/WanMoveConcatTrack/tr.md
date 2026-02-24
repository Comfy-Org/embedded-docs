> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/tr.md)

WanMoveConcatTrack düğümü, iki hareket izleme verisi setini tek, daha uzun bir dizi halinde birleştirir. Bunu, giriş izlerindeki iz yollarını ve görünürlük maskelerini kendi boyutları boyunca birleştirerek yapar. Yalnızca bir iz girişi sağlanırsa, bu veriyi değiştirmeden olduğu gibi iletir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `tracks_1` | TRACKS | Evet | | Birleştirilecek ilk hareket izleme verisi seti. |
| `tracks_2` | TRACKS | Hayır | | İsteğe bağlı ikinci hareket izleme verisi seti. Sağlanmazsa, `tracks_1` doğrudan çıkışa iletilir. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `tracks` | TRACKS | Birleştirilmiş hareket izleme verisi. Girişlerden gelen birleşik `track_path` ve `track_visibility` içerir. |
