# Parlaklığı Ayarla

The Adjust Brightness node modifies the brightness of an input image. It works by multiplying each pixel's value by a specified factor, then clamping the resulting values to stay within a valid range. A factor of 1.0 leaves the image unchanged, values below 1.0 make it darker, and values above 1.0 make it brighter.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Ayarlanacak girdi görüntüsü. | IMAGE | Evet | - |
| `factor` | Parlaklık faktörü. 1.0 = değişiklik yok, <1.0 = koyulaştırır, >1.0 = aydınlatır. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 2.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Parlaklığı ayarlanmış çıktı görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/tr.md)

---
**Source fingerprint (SHA-256):** `696fb3c0bfc8edccc2049dad8f44b4b056fe1caa95b0cc0126164269cb65ab1a`
