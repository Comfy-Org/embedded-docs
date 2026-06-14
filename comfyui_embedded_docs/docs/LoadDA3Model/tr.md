# Depth Anything 3'ü Yükle

Bu düğüm, bir dosyadan Depth Anything 3 modelini yükleyerek derinlik tahmini görevlerinde kullanıma hazır hale getirir. Model dosyasını seçmenize ve isteğe bağlı olarak model ağırlıkları için sayısal hassasiyeti (veri türü) belirlemenize olanak tanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `model_name` | Yüklenecek Depth Anything 3 model dosyasının adı. | STRING | Evet | `geometry_estimation` klasöründeki mevcut model dosyalarının listesi |
| `weight_dtype` | Model ağırlıkları için sayısal hassasiyet (veri türü). "default" seçeneği modelin orijinal hassasiyetini kullanır. (varsayılan: "default") | STRING | Hayır | `"default"`<br>`"fp16"`<br>`"bf16"`<br>`"fp32"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `DA3_MODEL` | Derinlik tahmini iş akışlarında kullanıma hazır, yüklenmiş Depth Anything 3 modeli. | DA3_MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadDA3Model/tr.md)

---
**Source fingerprint (SHA-256):** `b1b3f4075cd9172bc1f274848b9300bca20d3cbd53b23d3c4a9f0986b36e409e`
