> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/tr.md)

Rodina 3D Düzgün düğümü, Rodin API'sini kullanarak giriş görüntülerini işleyip bunları düzgün 3D modellere dönüştürerek 3D varlıklar üretir. Birden fazla görüntüyü girdi olarak alır ve indirilebilir bir 3D model dosyası üretir. Düğüm, görev oluşturma, durum yoklaması ve dosya indirme dahil olmak üzere tüm üretim sürecini otomatik olarak yönetir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `Görüntüler` | IMAGE | Evet | - | 3D model üretimi için kullanılacak giriş görüntüleri. Birden fazla görüntü sağlanabilir. |
| `Tohum` | INT | Evet | - | Üretim tutarlılığı için rastgele tohum değeri. |
| `Malzeme_Türü` | STRING | Evet | - | 3D modele uygulanacak malzeme türü. |
| `Çokgen_Sayısı` | STRING | Evet | - | Oluşturulan 3D model için hedef çokgen sayısı. Ağ kalitesini ve detay seviyesini belirler. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `3D Model Yolu` | STRING | İndirilen 3D modelin dosya yolu (yalnızca geriye dönük uyumluluk için). |
| `GLB` | FILE3DGLB | GLB formatında oluşturulan 3D model. |

---
**Source fingerprint (SHA-256):** `18783d4a3010234a3640d20c73cdd78e35a0eef7090bd433dba0fcc58e35ad3f`
