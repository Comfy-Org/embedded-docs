# İlkSigmayıAyarla

SetFirstSigma düğümü, bir sigma değerleri dizisini, dizideki ilk sigma değerini özel bir değerle değiştirerek değiştirir. Mevcut bir sigma dizisini ve yeni bir sigma değerini girdi olarak alır; ardından yalnızca ilk öğesi değiştirilmiş, diğer tüm sigma değerleri aynı kalmış yeni bir sigma dizisi döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `sigmas` | Değiştirilecek sigma değerleri giriş dizisi | SIGMAS | Evet | - |
| `sigma` | Dizide ilk öğe olarak ayarlanacak yeni sigma değeri (varsayılan: 136.0) | FLOAT | Evet | 0.0 to 20000.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | İlk öğesi özel sigma değeriyle değiştirilmiş modifiye sigma dizisi | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/tr.md)

---
**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`
