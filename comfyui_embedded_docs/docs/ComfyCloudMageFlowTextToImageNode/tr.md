# Comfy Cloud Mage Flow Metinden Görüntüye [BETA]

Bu düğüm, isteği Comfy Cloud'daki Mage-Flow metinden görüntüye iş akışına göndererek bir metin isteminden görüntü üretir. Daha hızlı damıtılmış turbo geçişi yerine tam 30 adımlı üretim geçişini çalıştırır ve bir negatif istem kabul eder; böylece nihai görüntüde istemediğiniz içeriği tanımlayabilirsiniz. Negatif istem bu 30 adımlı modda desteklenir; düğüm özetine göre, damıtılmış turbo varyantı bundan iyi şekilde yararlanamaz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Üretilecek görüntünün metin açıklaması. | STRING | Evet | Serbest metin |
| `negative_prompt` | Üretilen görüntüde görünmemesi gereken içeriği tanımlayan metin. Bu girdi standart 30 adımlı üretim geçişi sırasında kullanılır, ancak damıtılmış turbo varyantı negatif istemleri iyi kullanmaz. | STRING | Hayır | Serbest metin |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `image` | Sağlanan metin isteminden ve negatif istemden üretilen görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTextToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `80f4ecf1df3f2c46d94138f8ada817e12cc49e69e69a001630776ed644868367`
