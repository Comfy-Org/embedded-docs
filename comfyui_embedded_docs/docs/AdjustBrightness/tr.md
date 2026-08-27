# Parlaklığı Ayarla

Adjust Brightness düğümü, bir girdi görüntüsünün parlaklığını değiştirir. Her pikselin değerini belirtilen bir faktörle çarparak ve ardından sonuç değerlerini geçerli bir aralıkta kalacak şekilde sınırlayarak çalışır. 1.0 faktörü görüntüyü değiştirmez, 1.0'ın altındaki değerler onu koyulaştırır ve 1.0'ın üzerindeki değerler onu aydınlatır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Ayarlanacak girdi görüntüsü. | IMAGE | Evet | - |
| `faktör` | Parlaklık faktörü. 1.0 = değişiklik yok, <1.0 = koyulaştırır, >1.0 = aydınlatır. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 2.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görseller` | Parlaklığı ayarlanmış çıktı görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/tr.md)

---
**Source fingerprint (SHA-256):** `696fb3c0bfc8edccc2049dad8f44b4b056fe1caa95b0cc0126164269cb65ab1a`
