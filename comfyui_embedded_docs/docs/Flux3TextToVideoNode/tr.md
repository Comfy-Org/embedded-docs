# Flux3TextToVideoNode

FLUX 3 kullanarak bir metin isteminden senkronize sesli video oluşturur. Düğüm, isteminizi FLUX 3 hizmetine gönderir, oluşturmanın bitmesini bekler ve tamamlanmış video klibini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Ne istediğinizi sade bir dille ifade edin; istem, oluşturmadan önce yorumlanır ve genişletilir. Katmanlı ses için ortam sesi, müzik ve konuşmayı ayrı ayrı tanımlayın. (varsayılan: "") | STRING | Evet | Çok satırlı metin |
| `aspect_ratio` | Çıktı en-boy oranı. 'auto', istemden ve girdilerden birini seçer. (varsayılan: "auto") | STRING | Evet | Birden çok seçenek mevcuttur, `"auto"` dahil |
| `duration` | Klibin saniye cinsinden uzunluğu. 'auto', uzunluğu içeriğe göre ayarlar. (varsayılan: "auto") | STRING | Evet | Birden çok seçenek mevcuttur, `"auto"` dahil |
| `resolution` | Çıktı çözünürlüğü. (varsayılan: "720p") | STRING | Evet | `"720p"`<br>`"1080p"` |
| `generate_audio` | Senkronize ses oluştur (ortam sesi, konuşma, efektler). Kapalı, ses parçası olmayan bir video üretir. (varsayılan: True) | BOOLEAN | Evet | True<br>False |
| `safety_tolerance` | Moderasyon toleransı, 0 en katıdır. Görsel veya video gönderen istekler, burada ne ayarlarsanız ayarlayın 2 ile sınırlıdır. (varsayılan: 2) | INT | Evet | 0 ile 4 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum değeri; FLUX 3 kendi tohumunu seçer, bu nedenle gerçek sonuçlar bu değerden bağımsız olarak deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ile 4294967295 |

Not: `seed` girdisi, kullanıcı arayüzünde Control After Generate kontrollerini içerir. Görüntülenen fiyat, `resolution` ve `duration` değerlerine dayanır: HD (720p) saniye başına $0.2431 ve FHD (1080p) saniye başına $0.4147 olarak ücretlendirilir. Sabit bir süre seçildiğinde klibin toplam tahmini maliyeti gösterilir; `duration` "auto" olduğunda saniye başına ücret gösterilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Oluşturulan video klibi, `generate_audio` etkinleştirildiğinde senkronize ses ile. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `35f5e5b1c6dd737afab78f53700997a458781d38149cb64fc60d86a86858b2e6`
