LoadImageSetFromFolderNode, eğitim amaçlı olarak belirtilen bir klasör dizininden birden fazla görüntü yükler. Yaygın görüntü formatlarını otomatik olarak algılar ve isteğe bağlı olarak görüntüleri farklı yöntemler kullanarak yeniden boyutlandırıp bir grup halinde döndürebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `folder` | Görüntülerin yükleneceği klasör. | STRING | Evet | Birden çok seçenek mevcut |
| `resize_method` | Görüntüleri yeniden boyutlandırmak için kullanılacak yöntem (varsayılan: "None"). | STRING | Hayır | "None"<br>"Stretch"<br>"Crop"<br>"Pad" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `IMAGE` | Yüklenen görüntülerin tek bir tensör olarak grubu. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/tr.md)

---
**Source fingerprint (SHA-256):** `46fcfbf6a2ad95e707e32e54ed7b4c06bfd1cc290df122042187689f41bed828`
