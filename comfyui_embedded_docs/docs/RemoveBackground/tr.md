## Genel Bakış

Arka Planı Kaldır düğümü, bir arka plan kaldırma modeli kullanarak, giriş görüntüsündeki ön plan nesnesini arka plandan ayıran bir maske oluşturur. Bir görüntü ve bir arka plan kaldırma modeli alır, ardından ana nesneyi vurgulayan bir maske üretir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görsel` | Arka planı kaldırılacak giriş görüntüsü | IMAGE | Evet | Yok |
| `arka_plan_kaldırma_modeli` | Maskeyi oluşturmak için kullanılan arka plan kaldırma modeli | BACKGROUND_REMOVAL_MODEL | Evet | Yok |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `mask` | Giriş görüntüsünün ana nesnesini vurgulayan oluşturulmuş ön plan maskesi | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/tr.md)

---
**Source fingerprint (SHA-256):** `cd19134e6afed4d31096b613dd534eacad39afe7de2c8b74feab512bd5f09f66`
