> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/tr.md)

StringCompare düğümü, iki metin dizesini farklı karşılaştırma yöntemleri kullanarak karşılaştırır. Bir dizenin diğeriyle başlayıp başlamadığını, diğeriyle bitip bitmediğini veya her iki dizenin tamamen eşit olup olmadığını kontrol edebilir. Karşılaştırma, harf büyüklüğü farklılıkları dikkate alınarak veya alınmadan gerçekleştirilebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | Evet | - | Karşılaştırılacak ilk dize |
| `string_b` | STRING | Evet | - | Karşılaştırma yapılacak ikinci dize |
| `mode` | COMBO | Evet | "İle Başlar"<br>"İle Biter"<br>"Eşit" | Kullanılacak karşılaştırma yöntemi (varsayılan: "İle Başlar") |
| `case_sensitive` | BOOLEAN | Hayır | - | Karşılaştırma sırasında harf büyüklüğünün dikkate alınıp alınmayacağı (varsayılan: true) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | BOOLEAN | Karşılaştırma koşulu karşılanıyorsa true, aksi halde false döndürür |

---
**Source fingerprint (SHA-256):** `4491e4acd2c1881e9c924c6ae51d764dec5f46279094d173fe551e9ee9256597`
