> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/tr.md)

## Genel Bakış

Dosyadan bir arka plan kaldırma modeli yükler. Bu düğüm, modeli görüntülerden arka plan kaldırma işleminde kullanılmak üzere hazırlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `bg_removal_name` | STRING | Evet | Mevcut model dosyalarının listesi | Görüntülerden arka planları kaldırmak için kullanılan model. Mevcut arka plan kaldırma model dosyaları listesinden seçim yapın. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `bg_model` | BACKGROUND_REMOVAL | Yüklenmiş arka plan kaldırma modeli, diğer düğümler tarafından görüntüleri işlemek için kullanılmaya hazırdır. |

---
**Source fingerprint (SHA-256):** `63a1ffb37ea8581e3ba29f7dc4f871612d7ec458e6d36f5e2244201941d48f9d`
