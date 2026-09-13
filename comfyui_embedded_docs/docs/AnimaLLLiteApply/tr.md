# Anima LLLite Uygula

AnimaLLLiteApply, bir difüzyon modeline hafif bir animasyon yaması uygulayarak ayarlanabilir güç ve zamanlamayla kontrollü görüntüden görüntüye üretim sağlar. Önceden yapılandırılmış bir model yamasını bir giriş görüntüsü ve isteğe bağlı maske ile bütünleştirir; üretim sürecini etkilemek için modelin dikkat ve MLP katmanlarını değiştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yamanın uygulanacağı temel difüzyon modeli | MODEL | Evet | |
| `model_patch` | Uygulanacak önceden yapılandırılmış animasyon yaması | MODEL_PATCH | Evet | |
| `image` | Üretime rehberlik edecek referans görüntü. Yalnızca ilk 3 renk kanalı (RGB) kullanılır | IMAGE | Evet | |
| `strength` | Yama etkisinin gücü (varsayılan: 1.0, adım: 0.01) | FLOAT | Evet | -10.0 - 10.0 |
| `start_percent` | Yamanın etkisini göstermeye başladığı gürültü giderme sürecinin yüzdesi (varsayılan: 0.0, adım: 0.001) | FLOAT | Evet | 0.0 - 1.0 |
| `end_percent` | Yamanın etkisini göstermeyi bıraktığı gürültü giderme sürecinin yüzdesi (varsayılan: 1.0, adım: 0.001) | FLOAT | Evet | 0.0 - 1.0 |
| `mask` | Yama etkisini görüntünün belirli alanlarıyla sınırlamak için isteğe bağlı maske | MASK | Hayır | |

**Parametre kısıtlamalarına ilişkin not:** `model_patch` 4 giriş kanalına sahipse ve `mask` sağlanmamışsa, görüntü boyutlarıyla eşleşecek şekilde otomatik olarak sıfır maske oluşturulur. `model_patch` 4 giriş kanalına sahip değilse, `mask` parametresi yok sayılır ve `None` olarak ayarlanır. Giriş görüntüsünün yalnızca ilk 3 renk kanalı kullanılır. Bu düğüm ComfyUI'da deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | Animasyon yaması uygulanmış yamalı difüzyon modeli | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AnimaLLLiteApply/tr.md)

---
**Source fingerprint (SHA-256):** `48e455b767509a5a8c329365d5ffded86d6f4545d575c9fdc5ffbaf4da7c2287`
