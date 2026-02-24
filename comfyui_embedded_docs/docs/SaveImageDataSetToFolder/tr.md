> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/tr.md)

Bu düğüm, ComfyUI'nin çıktı dizini içinde belirtilen bir klasöre bir görüntü listesi kaydeder. Birden fazla görüntüyü girdi olarak alır ve özelleştirilebilir bir dosya adı öneki ile diske yazar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | Yok | Kaydedilecek görüntü listesi. |
| `folder_name` | STRING | Hayır | Yok | Görüntülerin kaydedileceği klasörün adı (çıktı dizini içinde). Varsayılan değer "dataset"tir. |
| `filename_prefix` | STRING | Hayır | Yok | Kaydedilen görüntü dosya adları için önek. Varsayılan değer "image"dır. |

**Not:** `images` girdisi bir listedir, yani aynı anda birden fazla görüntü alıp işleyebilir. `folder_name` ve `filename_prefix` parametreleri skaler değerlerdir; bir liste bağlanırsa, o listeden yalnızca ilk değer kullanılacaktır.

## Çıktılar

Bu düğümün herhangi bir çıktısı yoktur. Dosya sistemine bir kaydetme işlemi gerçekleştiren bir çıktı düğümüdür.
