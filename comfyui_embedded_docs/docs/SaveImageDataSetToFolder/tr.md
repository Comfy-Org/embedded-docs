# Görüntü Veri Setini Klasöre Kaydet

Bu belge, ComfyUI'nin çıktı dizininde belirtilen bir klasöre resim listesini kaydeden bir düğümdür. Birden fazla resmi girdi olarak alır ve özelleştirilebilir bir dosya adı ön ekiyle diske yazar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `images` | Kaydedilecek resim listesi. | IMAGE | Evet | Yok |
| `folder_name` | Resimlerin kaydedileceği klasörün adı (çıktı dizini içinde). Varsayılan değer "dataset"tir. | STRING | Hayır | Yok |
| `filename_prefix` | Kaydedilen resim dosya adları için ön ek. Varsayılan değer "image"dır. | STRING | Hayır | Yok |

**Not:** `images` girdisi bir listedir, yani aynı anda birden fazla resmi alıp işleyebilir. `folder_name` ve `filename_prefix` parametreleri skaler değerlerdir; bir liste bağlanırsa, bu listeden yalnızca ilk değer kullanılacaktır.

## Çıktılar

Bu düğümün herhangi bir çıktısı yoktur. Dosya sistemine kaydetme işlemi gerçekleştiren bir çıktı düğümüdür.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/tr.md)

---
**Source fingerprint (SHA-256):** `65c7905caa8ff2811054bec2830c1359d0c441b5d93f50bc4d0bf10645046556`
