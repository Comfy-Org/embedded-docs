# Kırp

StringTrim düğümü, bir metin dizesinin başından, sonundan veya her iki tarafından boşluk karakterlerini kaldırır. Dizenin sol tarafından, sağ tarafından veya her iki tarafından kırpma yapmayı seçebilirsiniz. Bu, istenmeyen boşlukları, sekmeleri veya yeni satır karakterlerini kaldırarak metin girdilerini temizlemek için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `dize` | İşlenecek metin dizesi. Çok satırlı girdiyi destekler. | STRING | Evet | - |
| `mod` | Dizenin hangi taraf(lar)ının kırpılacağını belirtir. "Both" her iki uçtan boşlukları kaldırır, "Left" yalnızca başlangıçtan kaldırır, "Right" yalnızca sondan kaldırır. | COMBO | Evet | "Both"<br>"Left"<br>"Right" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Seçilen moda göre boşlukları kaldırılmış, kırpılmış metin dizesi. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringTrim/tr.md)

---
**Source fingerprint (SHA-256):** `29b4da100373585af8a672ccfbd4c0b597705c1d8c176b2f88f3e878c1192460`
