> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddTextSuffix/tr.md)

Bu düğüm, girdi metin dizesinin sonuna belirtilen bir sonek ekler. Orijinal metni ve soneki girdi olarak alır, ardından birleştirilmiş sonucu döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Evet | | Sonekin ekleneceği orijinal metin. |
| `suffix` | STRING | Hayır | | Metne eklenecek sonek (varsayılan: ""). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `text` | STRING | Sonek eklendikten sonra elde edilen sonuç metni. |

---
**Source fingerprint (SHA-256):** `5dd75a9a29709a35343ec0dce144d2eb27a6e7aef5cb0b9245329c678897a763`
