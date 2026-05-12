> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/tr.md)

# Genel Bakış

Arka Plan Kaldırma düğümü, bir arka plan kaldırma modeli kullanarak giriş görüntüsünün ön plan nesnesini arka plandan ayıran bir maske oluşturur. Bir görüntü ve bir arka plan kaldırma modeli alır, ardından ana nesneyi vurgulayan bir maske üretir.

# Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `image` | IMAGE | Evet | Yok | Arka planı kaldırılacak giriş görüntüsü |
| `bg_removal_model` | BACKGROUND_REMOVAL_MODEL | Evet | Yok | Maskeyi oluşturmak için kullanılan arka plan kaldırma modeli |

# Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `mask` | MASK | Giriş görüntüsünün ana nesnesini vurgulayan oluşturulmuş ön plan maskesi |