> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/tr.md)

## Genel Bakış

FreeU düğümü, görüntü üretim kalitesini artırmak için bir modelin çıktı bloklarına frekans alanı değişiklikleri uygular. Farklı kanal gruplarını ölçeklendirerek ve belirli özellik haritalarına Fourier filtrelemesi uygulayarak çalışır; bu sayede üretim sürecinde modelin davranışı üzerinde ince ayarlı kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | - | FreeU değişikliklerinin uygulanacağı model |
| `b1` | FLOAT | Evet | 0,0 - 10,0 | model_channels × 4 özellikleri için omurga ölçekleme faktörü (varsayılan: 1,1) |
| `b2` | FLOAT | Evet | 0,0 - 10,0 | model_channels × 2 özellikleri için omurga ölçekleme faktörü (varsayılan: 1,2) |
| `s1` | FLOAT | Evet | 0,0 - 10,0 | model_channels × 4 özellikleri için atlama bağlantısı ölçekleme faktörü (varsayılan: 0,9) |
| `s2` | FLOAT | Evet | 0,0 - 10,0 | model_channels × 2 özellikleri için atlama bağlantısı ölçekleme faktörü (varsayılan: 0,2) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | FreeU yamaları uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `449a02a4bb5b42eb37fab394bcdc6375e08e369961d633618211ebc5f737ab51`
