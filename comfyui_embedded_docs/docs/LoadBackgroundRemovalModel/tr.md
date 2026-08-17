# Arka Plan Kaldırma Modelini Yükle

Bir dosyadan arka plan kaldırma modeli yükler ve görüntülerden arka plan kaldırılırken diğer düğümlerin kullanımına hazır hale getirir. Model dosyası, arka plan kaldırma klasöründeki mevcut dosyalar arasından seçilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | Görüntülerden arka plan kaldırmak için kullanılan model. | COMBO | Evet | Mevcut model dosyalarının listesi (background_removal klasöründeki dosyaların sıralı listesi) |

**Not:** Seçilen dosya geçerli bir arka plan kaldırma modeli içermiyorsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `bg_model` | Yüklenen arka plan kaldırma modeli; görüntüleri işlemek için diğer düğümler tarafından kullanılmaya hazırdır. | BACKGROUND_REMOVAL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/tr.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
