> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/tr.md)

Kling Image Generation Node, metin prompt'larından görüntüler oluşturur ve rehberlik için bir referans görsel kullanma seçeneği sunar. Metin açıklamanıza ve referans ayarlarınıza dayanarak bir veya daha fazla görsel oluşturur ve ardından oluşturulan görselleri çıktı olarak döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Olumlu metin prompt'u |
| `negatif_istem` | STRING | Evet | - | Olumsuz metin prompt'u |
| `görüntü_türü` | COMBO | Evet | KlingImageGenImageReferenceType'dan seçenekler<br>(kaynak kodundan çıkarılmıştır) | Görsel referans türü seçimi |
| `görüntü_sadakati` | FLOAT | Evet | 0.0 - 1.0 | Kullanıcı tarafından yüklenen görseller için referans yoğunluğu (varsayılan: 0.5) |
| `insan_sadakati` | FLOAT | Evet | 0.0 - 1.0 | Konu referans benzerliği (varsayılan: 0.45) |
| `model_adı` | COMBO | Evet | "kling-v1"<br>(ve KlingImageGenModelName'den diğer seçenekler) | Görsel oluşturma için model seçimi (varsayılan: "kling-v1") |
| `en_boy_oranı` | COMBO | Evet | "16:9"<br>(ve KlingImageGenAspectRatio'dan diğer seçenekler) | Oluşturulan görseller için en-boy oranı (varsayılan: "16:9") |
| `n` | INT | Evet | 1 - 9 | Oluşturulan görsel sayısı (varsayılan: 1) |
| `görüntü` | IMAGE | Hayır | - | İsteğe bağlı referans görseli |

**Parametre Kısıtlamaları:**

- `image` parametresi isteğe bağlıdır, ancak sağlandığında, kling-v1 modeli referans görsellerini desteklemez
- Prompt ve olumsuz prompt maksimum uzunluk sınırlamalarına sahiptir (MAX_PROMPT_LENGTH_IMAGE_GEN)
- Referans görseli sağlanmadığında, `image_type` parametresi otomatik olarak None olarak ayarlanır

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Girdi parametrelerine dayalı olarak oluşturulan görsel(ler) |