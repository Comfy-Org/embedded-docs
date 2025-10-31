> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/tr.md)

SaveGLB düğümü, 3B mesh verilerini GLB dosyaları olarak kaydeder; bu, 3B modeller için yaygın bir biçimdir. Mesh verilerini girdi olarak alır ve belirtilen dosya adı öneki ile çıktı dizinine aktarır. Girdi birden fazla mesh nesnesi içeriyorsa, düğüm birden fazla mesh'i kaydedebilir ve meta veriler etkinleştirildiğinde dosyalara otomatik olarak meta veri ekler.

## Girdiler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `mesh` | MESH | Evet | - | GLB dosyası olarak kaydedilecek 3B mesh verisi |
| `filename_prefix` | STRING | Hayır | - | Çıktı dosya adı için önek (varsayılan: "mesh/ComfyUI") |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `ui` | UI | Kaydedilen GLB dosyalarını, dosya adı ve alt klasör bilgisiyle kullanıcı arayüzünde görüntüler |