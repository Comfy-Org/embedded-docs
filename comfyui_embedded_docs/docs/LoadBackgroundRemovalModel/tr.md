# Arka Plan Kaldırma Modelini Yükle

Bir dosyadan arka plan kaldırma modeli yükler. Bu düğüm, modeli görüntülerden arka planları kaldırmak için kullanıma hazırlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `arka_plan_kaldırma_adı` | Görüntülerden arka planları kaldırmak için kullanılan model. Mevcut arka plan kaldırma modeli dosyaları listesinden seçin. | COMBO | Evet | Mevcut model dosyalarının listesi (alfabetik olarak sıralanmıştır) |

Not: Seçilen dosya geçerli bir arka plan kaldırma modeli içermiyorsa, düğüm bir RuntimeError hatası oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `bg_model` | Yüklenen arka plan kaldırma modeli; diğer düğümler tarafından görüntüleri işlemek için kullanıma hazırdır. | BACKGROUND_REMOVAL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/tr.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
