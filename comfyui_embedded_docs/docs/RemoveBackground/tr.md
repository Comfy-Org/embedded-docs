# Arka Planı Kaldır

## Genel Bakış

Remove Background düğümü, bir giriş görüntüsünün ana öznesini arka plandan ayıran bir ön plan maskesi oluşturur. Görüntüyü analiz etmek ve ön plan öğelerini vurgulayan bir maske üretmek için bir arka plan kaldırma modeli kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `bg_removal_model` | Maskeyi oluşturmak için kullanılan arka plan kaldırma modeli | BACKGROUND_REMOVAL_MODEL | Evet | N/A |
| `image` | Arka planın kaldırılacağı giriş görüntüsü | IMAGE | Evet | N/A |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mask` | Oluşturulan ön plan maskesi | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/tr.md)

---
**Source fingerprint (SHA-256):** `75b415acedaeaa1a694aeba2e4b0367524c6878e3e4a1f48b2a62898c68109f9`
