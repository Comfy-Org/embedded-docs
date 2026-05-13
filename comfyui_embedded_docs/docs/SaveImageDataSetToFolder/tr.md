> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/tr.md)

Bu belge, ComfyUI'nin çıktı dizininde belirtilen bir klasöre resim listesini kaydeden bir düğümdür. Birden fazla resmi girdi olarak alır ve özelleştirilebilir bir dosya adı ön ekiyle diske yazar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Evet | Yok | Kaydedilecek resim listesi. |
| `folder_name` | STRING | Hayır | Yok | Resimlerin kaydedileceği klasörün adı (çıktı dizini içinde). Varsayılan değer "dataset"tir. |
| `filename_prefix` | STRING | Hayır | Yok | Kaydedilen resim dosya adları için ön ek. Varsayılan değer "image"dır. |

**Not:** `images` girdisi bir listedir, yani aynı anda birden fazla resmi alıp işleyebilir. `folder_name` ve `filename_prefix` parametreleri skaler değerlerdir; bir liste bağlanırsa, bu listeden yalnızca ilk değer kullanılacaktır.

## Çıktılar

Bu düğümün herhangi bir çıktısı yoktur. Dosya sistemine kaydetme işlemi gerçekleştiren bir çıktı düğümüdür.

---
**Source fingerprint (SHA-256):** `65c7905caa8ff2811054bec2830c1359d0c441b5d93f50bc4d0bf10645046556`
