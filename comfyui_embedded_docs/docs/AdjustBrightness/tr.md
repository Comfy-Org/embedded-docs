> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/tr.md)

Parlaklık Ayarla düğümü, bir giriş görüntüsünün parlaklığını değiştirir. Her pikselin değerini belirtilen bir faktörle çarparak ve ardından elde edilen değerleri geçerli bir aralıkta kalacak şekilde sınırlandırarak çalışır. 1.0 faktörü görüntüyü değiştirmez, 1.0'ın altındaki değerler karartır, 1.0'ın üzerindeki değerler ise aydınlatır.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `image` | IMAGE | Evet | - | Ayarlanacak giriş görüntüsü. |
| `faktör` | FLOAT | Hayır | 0.0 - 2.0 | Parlaklık faktörü. 1.0 = değişiklik yok, <1.0 = daha koyu, >1.0 = daha parlak. (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `image` | IMAGE | Parlaklığı ayarlanmış çıkış görüntüsü. |

---
**Source fingerprint (SHA-256):** `c8f2fbb5fa149812a2ecd1ff9fce7bd6d29bf4c48b929e9ebc0a95c9e46ec65e`
