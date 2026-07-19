# SeedVR2Preprocess

Bu düğüm, yeniden boyutlandırılmış bir görüntüyü SeedVR2 modeli için hazırlamak amacıyla kenar boşluğu (padding) ekler. İşlem sırasında alfa kanalını kaldırır; bu kanal daha sonra, orijinal yeniden boyutlandırılmış görüntü kullanılarak eşlik eden SeedVR2 Çıkış Son İşleme düğümü tarafından geri yüklenir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `resized_images` | İşlenecek yeniden boyutlandırılmış görüntü. | IMAGE | Evet | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `images` | SeedVR2 işlemi için hazır, kenar boşluğu eklenmiş görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/tr.md)

---
**Source fingerprint (SHA-256):** `b8135d0e27f75a673f52d080c6704de8cc86d15b5d16eca055d55e2d20837dc7`
