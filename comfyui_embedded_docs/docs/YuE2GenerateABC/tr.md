# YuE2 ABC Oluştur

Bu düğüm, bir YuE2 metin ve şarkı sözü modeli kullanarak stil açıklaması ve şarkı sözlerine dayalı bir şarkı için ABC notasyonu üretir. Elde edilen `abc` çıktısı, ses üretmek için YuE2 Generate Music düğümüne bağlanabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | Stili ve şarkı sözlerini tokenize etmek ve ABC notasyonunu üretmek için kullanılan YuE2 modeli. | CLIP | Evet | - |
| `style` | Şarkının müzik stilini açıklayan metin. Çok satırlı girişi ve dinamik istemleri destekler. | STRING | Evet | - |
| `lyrics` | Şarkının sözlerini içeren metin. Çok satırlı girişi ve dinamik istemleri destekler. | STRING | Evet | - |
| `tohum` | Üretim için kullanılan rastgele tohum. Değiştirilmesi farklı sonuçlar üretir. Varsayılan: 0. | INT | Evet | 0 ile 18446744073709551615 |
| `mod` | full: melodi ve akorları üretir; melody: yalnızca melodi üretir, cover parçaları için önerilir. | COMBO | Evet | "full"<br>"melody" |
| `max_abc_tokens` | ABC notasyonu için üretilen maksimum token sayısı. Varsayılan: 8192. Gelişmiş ayar. | INT | Evet | 1 ile 20000 arası |
| `temperature` | Üretilen tokenların rastgeleliğini kontrol eder. Daha yüksek değerler daha çeşitli çıktı üretir. Varsayılan: 0.7. Gelişmiş ayar. | FLOAT | Evet | 0.0 ile 5.0 arası |
| `top_p` | Nucleus örnekleme eşiği; yalnızca kümülatif olasılığı bu eşiğin içinde olan tokenlar dikkate alınır. Varsayılan: 0.9. Gelişmiş ayar. | FLOAT | Evet | 0.01 ile 1.0 arası |
| `top_k` | Token seçimini en olası K tokenla sınırlar. Varsayılan: 30. Gelişmiş ayar. | INT | Evet | 1 ile 32768 arası |
| `repetition_penalty` | Üretim sırasında tekrar eden tokenlara uygulanan ceza. Varsayılan: 1.005. Gelişmiş ayar. | FLOAT | Evet | 0.01 ile 10.0 arası |
| `penalty_window` | Tekrar cezası için kullanılan son ABC token sayısı. Varsayılan: 100. Gelişmiş ayar. | INT | Evet | 1 ile 20000 arası |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `abc` | Şarkının üretilen ABC notasyonu; YuE2 Generate Music düğümüne bağlanabilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/tr.md)

---
**Source fingerprint (SHA-256):** `2c1bf0841a044724ff0477f920972d70bbd97de49b56fbe6213a9ac134797130`
