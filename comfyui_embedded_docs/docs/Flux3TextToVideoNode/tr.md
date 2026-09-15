# Flux 3 Metinden Videoya

FLUX 3 kullanarak bir metin isteminden senkronize sesli video oluşturur. Düğüm, isteminizi FLUX 3 hizmetine gönderir, oluşturmanın tamamlanmasını bekler ve tamamlanan video klibini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Ne istediğinizi sade bir dille yazın; istem, oluşturmadan önce yorumlanır ve genişletilir. Katmanlı ses için ortam sesini, müziği ve konuşmayı ayrı ayrı tanımlayın. (varsayılan: "") | STRING | Evet | Çok satırlı metin |
| `aspect_ratio` | Çıktı en-boy oranı. 'auto', istemden ve girdilerden birini seçer. (varsayılan: "auto") | COMBO | Evet | `"auto"` dahil olmak üzere birden çok seçenek mevcut |
| `duration` | Klip uzunluğu saniye cinsinden. 'auto', uzunluğu içeriğe uydurur. (varsayılan: "auto") | COMBO | Evet | `"auto"` dahil olmak üzere birden çok seçenek mevcut |
| `resolution` | Çıktı çözünürlüğü. (varsayılan: "720p") | COMBO | Evet | `"720p"`<br>`"1080p"` |
| `generate_audio` | Senkronize ses oluştur (ortam, konuşma, efektler). Kapalı olduğunda, ses parçası olmayan bir video üretir. (varsayılan: True) | BOOLEAN | Evet | True<br>False |
| `safety_tolerance` | Moderasyon toleransı, 0 en katıdır. Görsel veya video gönderen istekler, burada ne ayarlarsanız ayarlayın 2 ile sınırlandırılır. (varsayılan: 2) | INT | Evet | 0 ile 4 |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen tohum; FLUX 3 kendi tohumunu seçer, bu nedenle bu değerden bağımsız olarak gerçek sonuçlar deterministik değildir. (varsayılan: 42) | INT | Evet | 0 ile 4294967295 |

Not: `safety_tolerance` gelişmiş bir girdidir. `seed` girdisi, arayüzde Oluşturma Sonrası Kontrol denetimlerini içerir. Görüntülenen fiyat `resolution` ve `duration` değerlerine göre hesaplanır: HD (720p) saniye başına $0.2431, FHD (1080p) ise saniye başına $0.4147 olarak ücretlendirilir. Sabit bir süre seçildiğinde, klip için tahmini toplam maliyet gösterilir; `duration` "auto" olduğunda saniye başına ücret gösterilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | `generate_audio` etkinleştirildiğinde senkronize ses içeren oluşturulmuş video klibi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `9957c78291c320b1a8a6a9c0edeefae5f1ccc21a6b58f0b39069c2df8decd100`
