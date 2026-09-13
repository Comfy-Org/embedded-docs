# Flux Video Ölçek Büyütme

Flux Video Upscale, FLUX süper çözünürlüğünü kullanarak bir video klibini 1.5 ila 3 kat yükseltir. `creative` modunda ince ayrıntıları geri kazandırır ve üretir; `precise` modunda kaynağı değiştirmeden keskinleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | 1 ila 20 saniye arasında, en-boy oranı 1:4 ile 4:1 arasında olan kaynak klip. Çıktı 24 fps'te oluşturulur ve kare başına yaklaşık 14.4 megapiksel ile sınırlandırılır. | VIDEO | Evet | 1 ila 20 saniye süre; en-boy oranı 1:4 ile 4:1 arası; minimum 64x64 piksel |
| `upscale_factor` | Kaynağa göre çıktı boyutu. Çok büyük kaynaklar, kare başına sınır nedeniyle istenen faktörden daha az yükseltilir. (varsayılan: 2.0) | FLOAT | Evet | 1.5 ila 3.0 (adım 0.1) |
| `mod` | `creative` ince ayrıntıları geri kazandırır ve üretir; üretilmiş görüntüler, dokular ve manzaralar için en iyisidir. `precise` kaynağı değiştirmeden keskinleştirir; yüzler, ürünler ve gerçek çekimler içindir. (varsayılan: "creative") | COMBO | Evet | "creative"<br>"precise" |
| `istem` | Geliştirilmiş ayrıntıyı yönlendiren, klip için isteğe bağlı açıklama. Nötr bir yükseltme için boş bırakın. (varsayılan: boş) | STRING | Evet | Çok satırlı metin |
| `auto_downscale` | Alanı 3840x2160 pikselden büyük kaynakları giriş sınırına sığacak şekilde otomatik olarak küçültür. En-boy oranı korunur; daha küçük videolara dokunulmaz. (varsayılan: true) | BOOLEAN | Evet | true<br>false |
| `safety_tolerance` | Moderasyon toleransı, 0 en katıdır. (varsayılan: 2, gelişmiş parametre) | INT | Evet | 0 ila 4 |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirlemek için tohum; FLUX kendi tohumunu seçer, bu nedenle gerçek sonuçlar bu değerden bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ila 4294967295 |

Not: Kaynak video 1 ile 20 saniye arasında olmalı, boyutu en az 64x64 piksel olmalı ve en-boy oranı 1:4 ile 4:1 arasında olmalıdır. `auto_downscale` devre dışıysa ve video alanı 3840x2160 pikseli aşarsa düğüm bir hata verir. Çıktı videosu 24 fps'te oluşturulur ve kare başına yaklaşık 14.4 megapiksel ile sınırlandırılır; bu nedenle çok büyük kaynaklar istenen faktörden daha az yükseltilebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Yükseltilmiş video klibi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/tr.md)

---
**Source fingerprint (SHA-256):** `22dcf7c176705ce21a9032b1c9f4fe82ee6aa153f5057b90dac653b37281a677`
