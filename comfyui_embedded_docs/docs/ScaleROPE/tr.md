> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/tr.md)

ScaleROPE düğümü, bir modelin Döner Konum Gömme (ROPE) parametrelerini X, Y ve T (zaman) bileşenlerine ayrı ayrı ölçekleme ve kaydırma faktörleri uygulayarak değiştirmenizi sağlar. Bu, modelin konumsal kodlama davranışını ayarlamak için kullanılan gelişmiş, deneysel bir düğümdür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | ROPE parametreleri değiştirilecek model. |
| `scale_x` | FLOAT | Hayır | 0.0 - 100.0 | ROPE'un X bileşenine uygulanacak ölçekleme faktörü (varsayılan: 1.0). |
| `shift_x` | FLOAT | Hayır | -256.0 - 256.0 | ROPE'un X bileşenine uygulanacak kaydırma değeri (varsayılan: 0.0). |
| `scale_y` | FLOAT | Hayır | 0.0 - 100.0 | ROPE'un Y bileşenine uygulanacak ölçekleme faktörü (varsayılan: 1.0). |
| `shift_y` | FLOAT | Hayır | -256.0 - 256.0 | ROPE'un Y bileşenine uygulanacak kaydırma değeri (varsayılan: 0.0). |
| `scale_t` | FLOAT | Hayır | 0.0 - 100.0 | ROPE'un T (zaman) bileşenine uygulanacak ölçekleme faktörü (varsayılan: 1.0). |
| `shift_t` | FLOAT | Hayır | -256.0 - 256.0 | ROPE'un T (zaman) bileşenine uygulanacak kaydırma değeri (varsayılan: 0.0). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Yeni ROPE ölçekleme ve kaydırma parametreleri uygulanmış model. |

---
**Source fingerprint (SHA-256):** `c5ca193a46faa9477a2e6c99b905205685e8add8faa2f2d161c7c384b3dc2441`
