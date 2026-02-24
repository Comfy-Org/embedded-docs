> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/tr.md)

Adjust Brightness düğümü, bir giriş görüntüsünün parlaklığını değiştirir. Her pikselin değerini belirtilen bir faktörle çarparak çalışır ve ardından ortaya çıkan değerlerin geçerli bir aralıkta kalmasını sağlar. 1.0 faktörü görüntüyü değiştirmeden bırakır, 1.0'ın altındaki değerler görüntüyü koyulaştırır ve 1.0'ın üzerindeki değerler görüntüyü aydınlatır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Evet | - | Ayarlanacak giriş görüntüsü. |
| `factor` | FLOAT | Hayır | 0.0 - 2.0 | Parlaklık faktörü. 1.0 = değişiklik yok, <1.0 = koyu, >1.0 = parlak. (varsayılan: 1.0) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `image` | IMAGE | Parlaklığı ayarlanmış çıkış görüntüsü. |
