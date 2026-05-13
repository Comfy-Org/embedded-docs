> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringTrim/tr.md)

StringTrim düğümü, bir metin dizesinin başından, sonundan veya her iki tarafından boşluk karakterlerini kaldırır. Dizenin sol tarafından, sağ tarafından veya her iki tarafından kırpma yapmayı seçebilirsiniz. Bu, istenmeyen boşlukları, sekmeleri veya yeni satır karakterlerini kaldırarak metin girdilerini temizlemek için kullanışlıdır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Evet | - | İşlenecek metin dizesi. Çok satırlı girdiyi destekler. |
| `mode` | COMBO | Evet | "Both"<br>"Left"<br>"Right" | Dizenin hangi taraf(lar)ının kırpılacağını belirtir. "Both" her iki uçtan boşlukları kaldırır, "Left" yalnızca başlangıçtan kaldırır, "Right" yalnızca sondan kaldırır. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Seçilen moda göre boşlukları kaldırılmış, kırpılmış metin dizesi. |

---
**Source fingerprint (SHA-256):** `29b4da100373585af8a672ccfbd4c0b597705c1d8c176b2f88f3e878c1192460`
