# YuE2 ABC Oluştur

Bu düğüm, bir YuE2 metin ve şarkı sözü modeli kullanarak stil açıklaması ve şarkı sözlerine dayalı bir şarkı için ABC notasyonu üretir. Elde edilen `abc` çıktısı, ses üretmek için YuE2 Generate Music düğümüne bağlanabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | Stili ve şarkı sözlerini tokenize etmek ve ABC notasyonunu üretmek için kullanılan YuE2 modeli. | CLIP | Evet | - |
| `style` | Şarkının müzik stilini açıklayan metin. | STRING | Evet | - |
| `lyrics` | Şarkının sözlerini içeren metin. | STRING | Evet | - |
| `seed` | Üretim için kullanılan rastgele tohum. Değiştirilmesi farklı sonuçlar üretir. Varsayılan: 0. | INT | Evet | 0 to 18446744073709551615 |
| `mode` | full: melodi ve akorları üretir; melody: yalnızca melodi üretir, cover parçaları için önerilir. | COMBO | Evet | "full"<br>"melody" |
| `max_abc_tokens` | ABC notasyonu için üretilen maksimum token sayısı. Varsayılan: 8192. | INT | Evet | 1 to 20000 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `abc` | Şarkının üretilen ABC notasyonu; YuE2 Generate Music düğümüne bağlanabilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/tr.md)

---
**Source fingerprint (SHA-256):** `3e06f980a53e90b750f4190a95199e0e5ed1bd8c54d4dbf8485602ff1af00102`
