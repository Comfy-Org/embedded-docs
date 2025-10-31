> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/tr.md)

Rodin3D_Gen2 düğümü, Rodin API'sini kullanarak 3B varlıklar oluşturur. Girdi görüntülerini alır ve bunları çeşitli malzeme türleri ve çokgen sayılarına sahip 3B modellere dönüştürür. Düğüm, görev oluşturma, durum sorgulama ve dosya indirme dahil olmak üzere tüm oluşturma sürecini otomatik olarak yönetir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Evet | - | 3B model oluşturma için kullanılacak girdi görüntüleri |
| `Seed` | INT | Hayır | 0-65535 | Oluşturma için rastgele tohum değeri (varsayılan: 0) |
| `Material_Type` | COMBO | Hayır | "PBR"<br>"Shaded" | 3B modele uygulanacak malzeme türü (varsayılan: "PBR") |
| `Polygon_count` | COMBO | Hayır | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" | Oluşturulan 3B model için hedef çokgen sayısı (varsayılan: "500K-Triangle") |
| `TAPose` | BOOLEAN | Hayır | - | TAPose işleminin uygulanıp uygulanmayacağı (varsayılan: False) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Oluşturulan 3B modelin dosya yolu |