> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/tr.md)

RegexMatch düğümü, bir metin dizesinin belirli bir düzenli ifade kalıbıyla eşleşip eşleşmediğini kontrol eder. Girdi dizesini tarar ve kalıbın metin içinde herhangi bir yerde bulunup bulunmadığını belirten basit bir evet/hayır sonucu döndürür. Büyük/küçük harf duyarsız eşleme veya çok satırlı mod gibi seçenekleri etkinleştirerek aramanın nasıl çalıştığını ayarlayabilirsiniz.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `string` | STRING | Evet | - | Eşleşme aranacak metin dizesi |
| `regex_pattern` | STRING | Evet | - | Dizeyle eşleştirilecek düzenli ifade kalıbı |
| `case_insensitive` | BOOLEAN | Hayır | - | Eşleme sırasında büyük/küçük harf duyarlılığının yok sayılıp sayılmayacağı (varsayılan: True) |
| `multiline` | BOOLEAN | Hayır | - | Düzenli ifade eşlemesi için çok satırlı modun etkinleştirilip etkinleştirilmeyeceği (varsayılan: False) |
| `dotall` | BOOLEAN | Hayır | - | Düzenli ifade eşlemesi için dotall modunun etkinleştirilip etkinleştirilmeyeceği (varsayılan: False) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `matches` | BOOLEAN | Düzenli ifade kalıbı girdi dizesinin herhangi bir kısmıyla eşleşirse True, aksi halde False döndürür |

---
**Source fingerprint (SHA-256):** `b0ee05277edd8600d880051aa33a940c01abc170553515ab02960f25b1aec2be`
