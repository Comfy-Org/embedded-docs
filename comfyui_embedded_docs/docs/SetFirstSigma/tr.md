# İlkSigmayıAyarla

SetFirstSigma düğümü, bir sigma dizisinin yalnızca ilk değerini özel bir sigma değeriyle değiştirerek diziyi değiştirir. Mevcut bir sigma dizisini ve yeni bir sigma değerini alır; ardından ilk değer dışındaki tüm değerleri değişmemiş olan yeni bir sigma dizisi döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `sigmalar` | Değiştirilecek sigma değerlerinin girdi dizisi | SIGMAS | Evet | - |
| `sigma` | Dizide ilk öğe olarak ayarlanacak yeni sigma değeri (varsayılan: 136.0) | FLOAT | Evet | 0.0 ile 20000.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | İlk öğesi özel sigma değeriyle değiştirilmiş değiştirilmiş sigma dizisi | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/tr.md)

---
**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`
