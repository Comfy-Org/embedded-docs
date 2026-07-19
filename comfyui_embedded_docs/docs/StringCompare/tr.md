# Karşılaştır

StringCompare düğümü, iki metin dizesini farklı karşılaştırma yöntemleri kullanarak karşılaştırır. Bir dizenin diğeriyle başlayıp başlamadığını, diğeriyle bitip bitmediğini veya her iki dizenin tamamen eşit olup olmadığını kontrol edebilir. Karşılaştırma, harf büyüklüğü farklılıkları dikkate alınarak veya alınmadan gerçekleştirilebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `dize_a` | Karşılaştırılacak ilk dize | STRING | Evet | - |
| `dize_b` | Karşılaştırma yapılacak ikinci dize | STRING | Evet | - |
| `mod` | Kullanılacak karşılaştırma yöntemi (varsayılan: "İle Başlar") | COMBO | Evet | "İle Başlar"<br>"İle Biter"<br>"Eşit" |
| `büyük/küçük harf duyarlı` | Karşılaştırma sırasında harf büyüklüğünün dikkate alınıp alınmayacağı (varsayılan: true) | BOOLEAN | Hayır | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Karşılaştırma koşulu karşılanıyorsa true, aksi halde false döndürür | BOOLEAN |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/tr.md)

---
**Source fingerprint (SHA-256):** `4491e4acd2c1881e9c924c6ae51d764dec5f46279094d173fe551e9ee9256597`
