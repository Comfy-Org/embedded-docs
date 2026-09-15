# WanMoveConcatTrack

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `tracks_1` | Birleştirilecek ilk hareket izleme verisi kümesi. | TRACKS | Evet |  |
| `tracks_2` | İsteğe bağlı ikinci hareket izleme verisi kümesi. Sağlanmazsa, `tracks_1` doğrudan çıktıya geçirilir. | TRACKS | Hayır |  |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `tracks` | Girişlerden gelen birleştirilmiş `track_path` ve `track_visibility` değerlerini içeren birleştirilmiş hareket izleme verisi. `tracks_2` bağlı olmadığında `tracks_1` değerini değiştirmeden döndürür. | TRACKS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/tr.md)

---
**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`
