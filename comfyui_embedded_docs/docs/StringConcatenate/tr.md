> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringConcatenate/tr.md)

StringConcatenate düğümü, iki metin dizgesini belirtilen bir ayırıcı ile birleştirerek tek bir dize haline getirir. İki girdi dizesi ve bir ayırıcı karakter veya dize alır, ardından iki girdinin ayırıcı ile birbirine bağlandığı tek bir dize çıktısı verir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | Evet | - | Birleştirilecek ilk metin dizesi |
| `string_b` | STRING | Evet | - | Birleştirilecek ikinci metin dizesi |
| `ayırıcı` | STRING | Hayır | - | İki girdi dizesi arasına eklenecek karakter veya dize (varsayılan: boş dize) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `çıktı` | STRING | string_a ve string_b arasına ayırıcı eklenmiş birleşik dize |

---
**Source fingerprint (SHA-256):** `8e33665fb14a53f6c3bbfb6a4553ac7effa96d7d16d9ab2a9d4a1249abfc62e4`
