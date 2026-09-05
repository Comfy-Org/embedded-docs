# ComfyCloudMageFlowTextToImageNode

Bu düğüm, isteği Comfy Cloud'daki Mage-Flow metinden görüntüye iş akışına göndererek bir metin promptundan görüntü üretir. Daha hızlı olan damıtılmış turbo geçişi yerine tam 30 adımlık üretim geçişini çalıştırır ve negatif prompt kabul eder; böylece nihai görüntüde istemediğiniz içeriği tanımlayabilirsiniz. Negatif prompt bu 30 adımlık modda desteklenir; düğüm özetine göre damıtılmış turbo varyantı ondan iyi şekilde yararlanamaz.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|--------|
| `prompt` | Oluşturulacak görüntünün metin açıklaması. | STRING | Evet | Serbest metin |
| `negative_prompt` | Oluşturulan görüntüde bulunmaması gereken içeriği tanımlayan metin. Bu girdi standart 30 adımlık üretim geçişinde kullanılır; ancak damıtılmış turbo varyantı negatif promptları iyi şekilde kullanamaz. | STRING | Hayır | Serbest metin |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|------------|----------|-----------|
| `image` | Sağlanan metin promptu ve negatif prompt kullanılarak üretilen görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTextToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `80f4ecf1df3f2c46d94138f8ada817e12cc49e69e69a001630776ed644868367`
