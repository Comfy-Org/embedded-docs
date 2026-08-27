# ROPEÖlçekle

ScaleROPE düğümü, bir modelin Döner Konum Gömme (ROPE) parametrelerini, X, Y ve T (zaman) bileşenlerine ayrı ölçekleme ve kaydırma faktörleri uygulayarak değiştirmenizi sağlar. Modelin konumsal kodlama davranışını ayarlamak için kullanılan gelişmiş, deneysel bir düğümdür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | ROPE parametreleri değiştirilecek model. | MODEL | Evet | - |
| `x_ölçeği` | ROPE'un X bileşenine uygulanacak ölçekleme faktörü (varsayılan: 1.0). | FLOAT | Evet | 0.0 - 100.0 (adım 0.1) |
| `x_kaydırma` | ROPE'un X bileşenine uygulanacak kaydırma değeri (varsayılan: 0.0). | FLOAT | Evet | -256.0 - 256.0 (adım 0.1) |
| `y_ölçeği` | ROPE'un Y bileşenine uygulanacak ölçekleme faktörü (varsayılan: 1.0). | FLOAT | Evet | 0.0 - 100.0 (adım 0.1) |
| `y_kaydırma` | ROPE'un Y bileşenine uygulanacak kaydırma değeri (varsayılan: 0.0). | FLOAT | Evet | -256.0 - 256.0 (adım 0.1) |
| `t_ölçeği` | ROPE'un T (zaman) bileşenine uygulanacak ölçekleme faktörü (varsayılan: 1.0). | FLOAT | Evet | 0.0 - 100.0 (adım 0.1) |
| `t_kaydırma` | ROPE'un T (zaman) bileşenine uygulanacak kaydırma değeri (varsayılan: 0.0). | FLOAT | Evet | -256.0 - 256.0 (adım 0.1) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Yeni ROPE ölçekleme ve kaydırma parametreleri uygulanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/tr.md)

---
**Source fingerprint (SHA-256):** `5d5ab0182b78c8c12ceaf44685a91e666ce15fa099fd194e3605bbdb9cc3c961`
