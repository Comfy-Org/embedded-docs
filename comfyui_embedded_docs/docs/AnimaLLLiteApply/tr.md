# AnimaLLLiteApply

Bu düğüm, bir difüzyon modeline hafif bir animasyon yaması uygulayarak, ayarlanabilir güç ve zamanlama ile kontrollü görüntüden görüntüye üretim sağlar. Önceden yapılandırılmış bir model yamasını, bir giriş görüntüsü ve isteğe bağlı bir maske ile entegre ederek, modelin dikkat ve MLP katmanlarını değiştirir ve üretim sürecini etkiler.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yamanın uygulanacağı temel difüzyon modeli | MODEL | Evet | |
| `model_patch` | Uygulanacak önceden yapılandırılmış animasyon yaması | MODEL_PATCH | Evet | |
| `image` | Üretime rehberlik edecek referans görüntü | IMAGE | Evet | |
| `strength` | Yama efektinin gücü (varsayılan: 1.0) | FLOAT | Evet | -10.0 ile 10.0 arası |
| `start_percent` | Yamanın etkisini göstermeye başladığı gürültü giderme sürecinin yüzdesi (varsayılan: 0.0) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `end_percent` | Yamanın etkisini göstermeyi bıraktığı gürültü giderme sürecinin yüzdesi (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `mask` | Yama efektini görüntünün belirli alanlarıyla sınırlamak için isteğe bağlı bir maske | MASK | Hayır | |

**Parametre kısıtlamaları hakkında not:** `model_patch` 4 giriş kanalına sahipse ve `mask` sağlanmamışsa, görüntü boyutlarıyla eşleşecek şekilde otomatik olarak sıfır maskesi oluşturulur. `model_patch` 4 giriş kanalına sahip değilse, `mask` parametresi yok sayılır ve `None` olarak ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | Animasyon yaması uygulanmış, yamalı difüzyon modeli | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AnimaLLLiteApply/tr.md)

---
**Source fingerprint (SHA-256):** `291dc6a6619faab1c1100110c71c47381addcd80dbaf933dd8025a376bc2bee7`
