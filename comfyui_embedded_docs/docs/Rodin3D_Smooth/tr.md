> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/tr.md)

Rodin 3D Smooth düğümü, giriş görüntülerini işleyerek bunları pürüzsüz 3B modellere dönüştürmek için Rodin API'sini kullanarak 3B varlıklar oluşturur. Birden fazla görüntüyü girdi olarak alır ve indirilebilir bir 3B model dosyası üretir. Düğüm, görev oluşturma, durum sorgulama ve dosya indirme dahil olmak üzere tüm üretim sürecini otomatik olarak yönetir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Evet | - | 3B model oluşturma için kullanılacak girdi görüntüleri |
| `Seed` | INT | Evet | - | Üretim tutarlılığı için rastgele tohum değeri |
| `Material_Type` | STRING | Evet | - | 3B modele uygulanacak malzeme türü |
| `Polygon_count` | STRING | Evet | - | Oluşturulan 3B model için hedef çokgen sayısı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | İndirilen 3B modelin dosya yolu |