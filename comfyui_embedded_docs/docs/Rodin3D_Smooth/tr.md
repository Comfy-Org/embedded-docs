# Rodin 3D Oluştur - Pürüzsüz Oluştur

Rodina 3D Düzgün düğümü, Rodin API'sini kullanarak giriş görüntülerini işleyip bunları düzgün 3D modellere dönüştürerek 3D varlıklar üretir. Birden fazla görüntüyü girdi olarak alır ve indirilebilir bir 3D model dosyası üretir. Düğüm, görev oluşturma, durum yoklaması ve dosya indirme dahil olmak üzere tüm üretim sürecini otomatik olarak yönetir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `Görüntüler` | 3D model üretimi için kullanılacak giriş görüntüleri. Birden fazla görüntü sağlanabilir. | IMAGE | Evet | - |
| `Tohum` | Üretim tutarlılığı için rastgele tohum değeri. | INT | Evet | - |
| `Malzeme_Türü` | 3D modele uygulanacak malzeme türü. | STRING | Evet | - |
| `Çokgen_Sayısı` | Oluşturulan 3D model için hedef çokgen sayısı. Ağ kalitesini ve detay seviyesini belirler. | STRING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GLB` | İndirilen 3D modelin dosya yolu (yalnızca geriye dönük uyumluluk için). | STRING |
| `GLB` | GLB formatında oluşturulan 3D model. | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/tr.md)

---
**Source fingerprint (SHA-256):** `18783d4a3010234a3640d20c73cdd78e35a0eef7090bd433dba0fcc58e35ad3f`
