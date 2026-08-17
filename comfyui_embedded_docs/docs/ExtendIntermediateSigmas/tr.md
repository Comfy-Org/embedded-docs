# AraSigmalarıGenişlet

The ExtendIntermediateSigmas node takes an existing sequence of sigma values and inserts additional intermediate sigma values between them. It allows you to specify how many extra steps to add, the spacing method for interpolation, and optional start and end sigma boundaries to control where the extension occurs within the sigma sequence.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `sigmas` | Orta değerlerle genişletilecek girdi sigma dizisi | SIGMAS | Evet | - |
| `steps` | Mevcut sigmalar arasına eklenecek orta adım sayısı; N adımda, uygun her çift arasına N-1 orta sigma değeri eklenir (varsayılan: 2) | INT | Evet | 1 to 100 |
| `start_at_sigma` | Uzatma için üst sigma sınırı - yalnızca bu değerin altındaki sigmaları uzatır (varsayılan: -1.0, bu sonsuzluk anlamına gelir) | FLOAT | Evet | -1.0 to 20000.0 |
| `end_at_sigma` | Uzatma için alt sigma sınırı - yalnızca bu değerin üzerindeki sigmaları uzatır (varsayılan: 12.0) | FLOAT | Evet | 0.0 to 20000.0 |
| `spacing` | Orta sigma değerlerinin aralıklandırılması için enterpolasyon yöntemi: "linear" bunları eşit olarak dağıtır, "cosine" ve "sine" kavisli aralıklandırma uygular (varsayılan: "linear") | COMBO | Evet | `"linear"`<br>`"cosine"`<br>`"sine"` |

**Not:** Düğüm, yalnızca hem mevcut sigma değeri `start_at_sigma` değerine eşit veya daha küçük hem de `end_at_sigma` değerine eşit veya daha büyük olan mevcut sigma çiftleri arasına orta sigma değerleri ekler. `start_at_sigma` -1.0 olarak ayarlandığında sonsuzluk olarak ele alınır; bu durumda yalnızca `end_at_sigma` alt sınırı uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `sigmas` | Ek orta değerler eklenmiş genişletilmiş sigma dizisi | SIGMAS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/tr.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
