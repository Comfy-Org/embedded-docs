> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Regular/tr.md)

Rodin 3D Regular düğümü, Rodin API'sini kullanarak 3B varlıklar oluşturur. Girdi görüntülerini alır ve bunları Rodin servisi aracılığıyla işleyerek 3B modeller oluşturur. Düğüm, görev oluşturmadan nihai 3B model dosyalarının indirilmesine kadar tüm iş akışını yönetir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Evet | - | 3B model oluşturma için kullanılan girdi görüntüleri |
| `Seed` | INT | Evet | - | Tekrarlanabilir sonuçlar için rastgele tohum değeri |
| `Material_Type` | STRING | Evet | - | 3B modele uygulanacak malzeme türü |
| `Polygon_count` | STRING | Evet | - | Oluşturulan 3B model için hedef çokgen sayısı |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Oluşturulan 3B modelin dosya yolu |