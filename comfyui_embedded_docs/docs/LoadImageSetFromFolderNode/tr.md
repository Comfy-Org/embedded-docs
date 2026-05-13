> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/tr.md)

LoadImageSetFromFolderNode, eğitim amaçlı olarak belirtilen bir klasör dizininden birden fazla görüntü yükler. Yaygın görüntü formatlarını otomatik olarak algılar ve isteğe bağlı olarak görüntüleri farklı yöntemler kullanarak yeniden boyutlandırıp bir grup halinde döndürebilir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `folder` | STRING | Evet | Birden çok seçenek mevcut | Görüntülerin yükleneceği klasör. |
| `resize_method` | STRING | Hayır | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | Görüntüleri yeniden boyutlandırmak için kullanılacak yöntem (varsayılan: "None"). |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `IMAGE` | IMAGE | Yüklenen görüntülerin tek bir tensör olarak grubu. |

---
**Source fingerprint (SHA-256):** `46fcfbf6a2ad95e707e32e54ed7b4c06bfd1cc290df122042187689f41bed828`
