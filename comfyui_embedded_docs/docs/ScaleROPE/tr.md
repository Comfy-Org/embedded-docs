# ROPEÖlçekle

ScaleROPE düğümü, bir modelin Döner Konum Gömme (ROPE) parametrelerini X, Y ve T (zaman) bileşenlerine ayrı ayrı ölçekleme ve kaydırma faktörleri uygulayarak değiştirmenizi sağlar. Bu, modelin konumsal kodlama davranışını ayarlamak için kullanılan gelişmiş, deneysel bir düğümdür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | ROPE parametreleri değiştirilecek model. | MODEL | Evet | - |
| `x_ölçeği` | ROPE'un X bileşenine uygulanacak ölçekleme faktörü (varsayılan: 1.0). | FLOAT | Hayır | 0.0 - 100.0 |
| `x_kaydırma` | ROPE'un X bileşenine uygulanacak kaydırma değeri (varsayılan: 0.0). | FLOAT | Hayır | -256.0 - 256.0 |
| `y_ölçeği` | ROPE'un Y bileşenine uygulanacak ölçekleme faktörü (varsayılan: 1.0). | FLOAT | Hayır | 0.0 - 100.0 |
| `y_kaydırma` | ROPE'un Y bileşenine uygulanacak kaydırma değeri (varsayılan: 0.0). | FLOAT | Hayır | -256.0 - 256.0 |
| `t_ölçeği` | ROPE'un T (zaman) bileşenine uygulanacak ölçekleme faktörü (varsayılan: 1.0). | FLOAT | Hayır | 0.0 - 100.0 |
| `t_kaydırma` | ROPE'un T (zaman) bileşenine uygulanacak kaydırma değeri (varsayılan: 0.0). | FLOAT | Hayır | -256.0 - 256.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Yeni ROPE ölçekleme ve kaydırma parametreleri uygulanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/tr.md)

---
**Source fingerprint (SHA-256):** `c5ca193a46faa9477a2e6c99b905205685e8add8faa2f2d161c7c384b3dc2441`
