# Arka Plan Kaldırma Modelini Yükle

Bir dosyadan arka plan kaldırma modeli yükler. Bu düğüm, modeli görüntülerdeki arka planları kaldırmak için diğer düğümler tarafından kullanılabilecek şekilde hazırlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `arka_plan_kaldırma_adı` | Görüntülerdeki arka planları kaldırmak için kullanılan model. Kullanılabilir arka plan kaldırma model dosyaları listesinden seçin. | COMBO | Evet | Kullanılabilir model dosyalarının listesi (alfabetik olarak sıralanmış) |

Not: Seçilen dosya geçerli bir arka plan kaldırma modeli içermiyorsa, düğüm bir RuntimeError oluşturur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `bg_model` | Yüklenen arka plan kaldırma modeli; görüntüleri işlemek için diğer düğümler tarafından kullanılmaya hazırdır. | BACKGROUND_REMOVAL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/tr.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
