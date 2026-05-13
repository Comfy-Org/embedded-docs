> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/tr.md)

Rodin3D_Gen2 düğümü, Rodin API'sini kullanarak 3D varlıklar üretir. Giriş görüntülerini alır ve bunları çeşitli malzeme türleri ve çokgen sayılarıyla 3D modellere dönüştürür. Düğüm, görev oluşturma, durum sorgulama ve dosya indirme dahil olmak üzere tüm üretim sürecini otomatik olarak yönetir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `Görseller` | IMAGE | Evet | - | 3D model üretimi için kullanılacak giriş görüntüleri |
| `Tohum` | INT | Hayır | 0-65535 | Üretim için rastgele tohum değeri (varsayılan: 0) |
| `Malzeme_Türü` | COMBO | Hayır | "PBR"<br>"Shaded" | 3D modele uygulanacak malzeme türü (varsayılan: "PBR") |
| `Poligon_sayısı` | COMBO | Hayır | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" | Üretilen 3D model için hedef çokgen sayısı (varsayılan: "500K-Triangle") |
| `TAPoz` | BOOLEAN | Hayır | - | TAPose işleminin uygulanıp uygulanmayacağı (varsayılan: False) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `GLB` | STRING | Üretilen 3D modele giden dosya yolu (geriye dönük uyumluluk için) |
| `GLB` | FILE3DGLB | GLB formatında üretilen 3D model |

---
**Source fingerprint (SHA-256):** `940712a9a40f4cb07050f3ed7ac502469b30bd364f86bb42b9dd8bf63eb912a2`
