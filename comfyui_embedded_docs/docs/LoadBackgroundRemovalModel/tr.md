> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/tr.md)

## Genel Bakış

Bir dosyadan arka plan kaldırma modeli yükler. Bu düğüm, modeli görüntülerden arka plan kaldırma işleminde kullanılmak üzere hazırlar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `bg_removal_name` | STRING | Evet | Mevcut model dosyalarının listesi | Görüntülerden arka plan kaldırmak için kullanılan model. Mevcut arka plan kaldırma model dosyaları listesinden seçim yapın. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `bg_model` | BACKGROUND_REMOVAL | Yüklenmiş arka plan kaldırma modeli, görüntüleri işlemek için diğer düğümler tarafından kullanılmaya hazır. |