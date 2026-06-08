ImageFlip düğümü, görüntüleri farklı eksenler boyunca döndürür. Görüntüleri x ekseni boyunca dikey olarak veya y ekseni boyunca yatay olarak döndürebilir. Düğüm, seçilen yönteme göre döndürme işlemini gerçekleştirmek için torch.flip işlemlerini kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `görüntü` | Döndürülecek giriş görüntüsü | IMAGE | Evet | - |
| `çevirme yöntemi` | Uygulanacak döndürme yönü (varsayılan: "x-axis: vertically") | STRING | Evet | "x-axis: vertically"<br>"y-axis: horizontally" |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntü` | Döndürülmüş çıkış görüntüsü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/tr.md)

---
**Source fingerprint (SHA-256):** `5cb9949c53653192b1a696179351976c3a87e2e7afc4634624b4d827ad75b527`
