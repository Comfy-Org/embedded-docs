> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/tr.md)

ImageFlip düğümü, görüntüleri farklı eksenler boyunca döndürür. Görüntüleri x ekseni boyunca dikey olarak veya y ekseni boyunca yatay olarak döndürebilir. Düğüm, seçilen yönteme göre döndürme işlemini gerçekleştirmek için torch.flip işlemlerini kullanır.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `image` | IMAGE | Evet | - | Döndürülecek giriş görüntüsü |
| `flip_method` | STRING | Evet | "x-axis: vertically"<br>"y-axis: horizontally" | Uygulanacak döndürme yönü (varsayılan: "x-axis: vertically") |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `image` | IMAGE | Döndürülmüş çıkış görüntüsü |

---
**Source fingerprint (SHA-256):** `5cb9949c53653192b1a696179351976c3a87e2e7afc4634624b4d827ad75b527`
