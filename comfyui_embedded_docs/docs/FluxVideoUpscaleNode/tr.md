# FluxVideoUpscaleNode

Flux Video Upscale, bir video klibini FLUX süper çözünürlüğünü kullanarak 1,5 ila 3 kat büyütür. Yaratıcı modda ince ayrıntıları geri kazandırır ve yeniden oluşturur; hassas modda ise kaynağı değiştirmeden keskinleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | En-boy oranı 1:4 ile 4:1 arasında olan, 1 ila 20 saniye arasındaki kaynak kliptir. Çıktı, 24 fps'de işlenir ve kare başına yaklaşık 14,4 megapiksel ile sınırlandırılır. | VIDEO | Evet | 1 ila 20 saniye süre; 1:4 ile 4:1 arasında en-boy oranı; minimum 64x64 piksel |
| `upscale_factor` | Kaynağa göre çıktı boyutu. Kare başına sınır nedeniyle çok büyük kaynaklar, istenen faktörden daha az büyütülür. (varsayılan: 2.0) | FLOAT | Evet | 1.5 ila 3.0 (adım 0.1) |
| `mod` | 'creative', ince ayrıntıları geri kazandırır ve yeniden üretir; üretilmiş çekimler, dokular ve manzaralar için en iyisidir. 'precise', kaynağı değiştirmeden keskinleştirir; yüzler, ürünler ve gerçek çekimler için uygundur. (varsayılan: "creative") | COMBO | Evet | "creative"<br>"precise" |
| `istem` | Geliştirilmiş ayrıntıyı yönlendiren, klibe ait isteğe bağlı açıklama. Nötr bir büyütme için boş bırakın. (varsayılan: boş) | STRING | Evet | Çok satırlı metin |
| `auto_downscale` | Alanı 3840x2160 pikselden büyük olan kaynakları girdi sınırına uyacak şekilde otomatik olarak küçültür. En-boy oranı korunur; daha küçük videolara dokunulmaz. (varsayılan: true) | BOOLEAN | Evet | true<br>false |
| `safety_tolerance` | Moderasyon toleransı, 0 en katıdır. (varsayılan: 2, gelişmiş parametre) | INT | Evet | 0 ila 4 |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum değeri; FLUX kendi tohumunu seçtiğinden, bu değerden bağımsız olarak gerçek sonuçlar deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ila 4294967295 |

Not: Kaynak video 1 ila 20 saniye arasında ve en az 64x64 piksel boyutunda olmalıdır. `auto_downscale` devre dışıysa ve video alanı 3840x2160 pikseli aşarsa düğüm hata verir. Çıktı videosu 24 fps'de işlenir ve kare başına yaklaşık 14,4 megapiksel ile sınırlandırılır; bu nedenle çok büyük kaynaklar istenen faktörden daha az büyütülebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Büyütülmüş video klibi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/tr.md)

---
**Source fingerprint (SHA-256):** `22dcf7c176705ce21a9032b1c9f4fe82ee6aa153f5057b90dac653b37281a677`
