# Rodin 3D Oluştur - Gen-2 Oluştur

Rodin3D_Gen2 düğümü, Rodin API'sini kullanarak 3D varlıklar üretir. Giriş görüntülerini alır ve bunları çeşitli malzeme türleri ve çokgen sayılarıyla 3D modellere dönüştürür. Düğüm, görev oluşturma, durum sorgulama ve dosya indirme dahil olmak üzere tüm üretim sürecini otomatik olarak yönetir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `Görseller` | 3D model üretimi için kullanılacak giriş görüntüleri | IMAGE | Evet | - |
| `Tohum` | Üretim için rastgele tohum değeri (varsayılan: 0) | INT | Hayır | 0-65535 |
| `Malzeme_Türü` | 3D modele uygulanacak malzeme türü (varsayılan: "PBR") | COMBO | Hayır | "PBR"<br>"Shaded" |
| `Poligon_sayısı` | Üretilen 3D model için hedef çokgen sayısı (varsayılan: "500K-Triangle") | COMBO | Hayır | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" |
| `TAPoz` | TAPose işleminin uygulanıp uygulanmayacağı (varsayılan: False) | BOOLEAN | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `3B Model Yolu` | Üretilen 3D modele giden dosya yolu (geriye dönük uyumluluk için) | STRING |
| `GLB` | GLB formatında üretilen 3D model | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/tr.md)

---
**Source fingerprint (SHA-256):** `940712a9a40f4cb07050f3ed7ac502469b30bd364f86bb42b9dd8bf63eb912a2`
