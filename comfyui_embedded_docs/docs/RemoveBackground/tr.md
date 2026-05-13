> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/tr.md)

## Genel Bakış

Arka Planı Kaldır düğümü, bir arka plan kaldırma modeli kullanarak, giriş görüntüsündeki ön plan nesnesini arka plandan ayıran bir maske oluşturur. Bir görüntü ve bir arka plan kaldırma modeli alır, ardından ana nesneyi vurgulayan bir maske üretir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `görsel` | IMAGE | Evet | Yok | Arka planı kaldırılacak giriş görüntüsü |
| `arka_plan_kaldırma_modeli` | BACKGROUND_REMOVAL_MODEL | Evet | Yok | Maskeyi oluşturmak için kullanılan arka plan kaldırma modeli |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `mask` | MASK | Giriş görüntüsünün ana nesnesini vurgulayan oluşturulmuş ön plan maskesi |

---
**Source fingerprint (SHA-256):** `cd19134e6afed4d31096b613dd534eacad39afe7de2c8b74feab512bd5f09f66`
