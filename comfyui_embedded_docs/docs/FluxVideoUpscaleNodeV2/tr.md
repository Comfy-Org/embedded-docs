# Flux Video Upscale

Flux Video Upscale, bir videoyu FLUX süper çözünürlüğüyle büyütür; bunu ya sabit 1080p, 2K veya 4K kare boyutuna ya da 1,5 ila 3 katına çıkararak yapar. Yaratıcı mod ince detayları geri kazandırır ve üretir; bu, oluşturulmuş görüntülere uygundur; hassas mod ise kaynağı değiştirmeden keskinleştirir; bu da yüzler, ürünler ve gerçek görüntüler için uygundur. Klip yüklenir, BFL işi yoklanır ve bitmiş video 24 fps'te geri gelir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | 1 ila 20 saniyelik, en az 64x64 piksel olan ve en-boy oranı 1:4 ile 4:1 arasında bulunan kaynak klip. Çıktı 24 fps'te işlenir ve kare başına yaklaşık 14,4 megapiksel ile sınırlandırılır. | VIDEO | Evet | 1 ila 20 saniye süre; en-boy oranı 1:4 ile 4:1 arasında; en az 64x64 piksel |
| `target_resolution` | Çıktı boyutu. `"1080p"`, `"2K"` ve `"4K"` sonucu 1920x1080, 2560x1440 veya 3840x2160 piksel içine sığdırır; dikey klipler için döndürülür; `"by factor"` ise bunun yerine `upscale_factor` kullanır. | DYNAMIC_COMBO | Evet | `"2K"`<br>`"4K"`<br>`"1080p"`<br>`"by factor"` |
| `mode` | `"creative"` ince detayları geri kazandırır ve üretir; üretilmiş görüntüler, dokular ve manzaralar için en iyisidir. `"precise"` kaynağı değiştirmeden keskinleştirir; yüzler, ürünler ve gerçek görüntüler içindir. (varsayılan: `"creative"`) | COMBO | Evet | `"creative"`<br>`"precise"` |
| `prompt` | İyileştirilmiş detayı yönlendiren, klip için isteğe bağlı açıklama. Nötr bir büyütme için boş bırakın. (varsayılan: boş) | STRING | Evet | Çok satırlı metin |
| `auto_downscale` | Çok büyük kaynakları reddetmek yerine küçültün: alan olarak 2560x1440 pikselin üzerinde veya hedef çözünürlüğün üçte ikisinin üzerinde olanlar. En-boy oranı korunur. (varsayılan: true) | BOOLEAN | Evet | true<br>false |
| `safety_tolerance` | Moderasyon toleransı; 0 en katı seçenektir. (varsayılan: 2, gelişmiş parametre) | INT | Evet | 0 ila 4 |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; FLUX kendi seed değerini seçer, bu nedenle gerçek sonuçlar bu değerden bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ila 4294967295 |

### by factor Girdileri

Bu girdiler, `target_resolution` değeri `"by factor"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `upscale_factor` | Kaynağa göre çıktı boyutu. Çok büyük kaynaklar, kare başına üst sınır nedeniyle istenen çarpandan daha az büyütülür. (varsayılan: 2.0) | FLOAT | Evet | 1.5 ila 3.0 (adım 0.1) |

Hedef boyut, 1.5-3.0 aralığına sınırlandırılmış bir büyütme çarpanı olarak uygulanır; bu nedenle 3x'te kutuyu doldurmak için çok küçük olan bir kaynak, istenen çözünürlükten daha küçük çıkar ve kutuyu sığdırmak için 1.5x'ten daha azına ihtiyaç duyacak bir kaynak önce küçültülür. `auto_downscale` kapalıyken düğüm, küçültme yerine bir hatayla durur. Çıktı 24 fps'tir ve kare başına yaklaşık 14.4 megapiksel ile sınırlandırılır; bu nedenle çok büyük kaynaklar istenen çarpandan daha az büyütülebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Büyütülmüş video klibi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `bef6ef4614d75bc9e6bab977f5f19c45fe30d300907913462a058e6e7e7e4ac7`
