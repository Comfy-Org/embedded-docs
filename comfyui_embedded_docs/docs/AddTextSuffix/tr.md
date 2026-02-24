> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddTextSuffix/tr.md)

Bu düğüm, belirtilen bir soneki giriş metin dizisinin sonuna ekler. Orijinal metni ve soneki girdi olarak alır, ardından birleştirilmiş sonucu döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Evet | | Sonekin ekleneceği orijinal metin. |
| `suffix` | STRING | Hayır | | Metne eklenecek sonek (varsayılan: ""). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `text` | STRING | Sonek eklendikten sonra ortaya çıkan metin. |
