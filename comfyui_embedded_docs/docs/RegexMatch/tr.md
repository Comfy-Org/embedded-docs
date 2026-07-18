RegexMatch düğümü, bir metin dizesinin belirli bir düzenli ifade kalıbıyla eşleşip eşleşmediğini kontrol eder. Girdi dizesini tarar ve kalıbın metin içinde herhangi bir yerde bulunup bulunmadığını belirten basit bir evet/hayır sonucu döndürür. Büyük/küçük harf duyarsız eşleme veya çok satırlı mod gibi seçenekleri etkinleştirerek aramanın nasıl çalıştığını ayarlayabilirsiniz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `dize` | Eşleşme aranacak metin dizesi | STRING | Evet | - |
| `regex_deseni` | Dizeyle eşleştirilecek düzenli ifade kalıbı | STRING | Evet | - |
| `büyük/küçük harf duyarsız` | Eşleme sırasında büyük/küçük harf duyarlılığının yok sayılıp sayılmayacağı (varsayılan: True) | BOOLEAN | Hayır | - |
| `çok satırlı` | Düzenli ifade eşlemesi için çok satırlı modun etkinleştirilip etkinleştirilmeyeceği (varsayılan: False) | BOOLEAN | Hayır | - |
| `nokta her şey` | Düzenli ifade eşlemesi için dotall modunun etkinleştirilip etkinleştirilmeyeceği (varsayılan: False) | BOOLEAN | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `eşleşmeler` | Düzenli ifade kalıbı girdi dizesinin herhangi bir kısmıyla eşleşirse True, aksi halde False döndürür | BOOLEAN |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/tr.md)

---
**Source fingerprint (SHA-256):** `b0ee05277edd8600d880051aa33a940c01abc170553515ab02960f25b1aec2be`
