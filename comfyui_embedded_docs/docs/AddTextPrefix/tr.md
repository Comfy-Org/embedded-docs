> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddTextPrefix/tr.md)

Add Text Prefix düğümü, her bir giriş metninin başına belirli bir dize ekleyerek metni değiştirir. Metni ve bir ön eki girdi olarak alır, ardından birleştirilmiş sonucu döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Evet | | Ön ekin ekleneceği metin. |
| `prefix` | STRING | Hayır | | Metnin başına eklenecek dize (varsayılan: ""). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `text` | STRING | Ön ekin başa eklendiği sonuç metni. |
