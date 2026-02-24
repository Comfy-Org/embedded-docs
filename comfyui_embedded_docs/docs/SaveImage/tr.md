> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/tr.md)

SaveImage düğümü aldığı görüntüleri `ComfyUI/output` dizininize kaydeder. Her görüntüyü bir PNG dosyası olarak kaydeder ve gelecekte referans için istem (prompt) gibi iş akışı meta verilerini kaydedilen dosyaya gömebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `görüntüler` | IMAGE | Evet | - | Kaydedilecek görüntüler. |
| `dosyaadı_öneki` | STRING | Evet | - | Kaydedilecek dosya için ön ek. Bu, düğümlerden gelen değerleri dahil etmek için `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme bilgilerini içerebilir (varsayılan: "ComfyUI"). |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `ui` | UI_RESULT | Bu düğüm, kaydedilen görüntülerin dosya adları ve alt klasörleriyle birlikte bir listesini içeren bir UI sonucu çıktılar. Diğer düğümlere bağlanmak için veri çıktılamaz. |
