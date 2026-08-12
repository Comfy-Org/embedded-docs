# Flux3VideoContinuationNode

Bu düğüm, mevcut bir video klibini FLUX 3 ile devam ettirir; böylece yeni klip, sağladığınız videonun son karelerinden itibaren sürer. Kaynak klibinizi yükler, istemi ve ayarları oluşturma servisine gönderir ve hazır olduğunda sonuç devam videosunu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `video` | Devam ettirilecek klip. | VIDEO | Evet | Tek video klibi |
| `prompt` | Devam filminin ne göstermesi gerektiği; istem, oluşturmadan önce yorumlanır ve genişletilir. (varsayılan: "") | STRING | Evet | Boş olmayan metin (minimum 1 karakter) |
| `aspect_ratio` | Çıktı en-boy oranı. 'auto', istemden ve girdilerden birini seçer. (varsayılan: "auto") | STRING | Evet | Birden çok ön tanımlı seçenek (varsayılan: "auto") |
| `duration` | Saniye cinsinden klip uzunluğu. 'auto', uzunluğu içeriğe uydurur. (varsayılan: "auto") | STRING | Evet | "auto" (varsayılan)<br>Saniye cinsinden sayısal değerler |
| `resolution` | Çıktı çözünürlüğü. (varsayılan: "720p") | STRING | Evet | Birden çok ön tanımlı seçenek (varsayılan: "720p") |
| `generate_audio` | Senkronize ses üretir (ortam, konuşma, efektler). Kapalı, hiçbir ses parçası olmayan bir video üretir. (varsayılan: true) | BOOLEAN | Evet | true<br>false |
| `safety_tolerance` | Moderasyon toleransı, 0 en katı olanıdır. Görüntü veya video gönderen istekler, burada ne ayarlarsanız ayarlayın 2 ile sınırlandırılır. (gelişmiş parametre, varsayılan: 2) | INT | Evet | 0 - 4 (video istekleri için etkin maksimum: 2) |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum; FLUX 3 kendi tohumunu seçer, bu nedenle bu değerden bağımsız olarak gerçek sonuçlar deterministik değildir. (gelişmiş parametre, varsayılan: 42) | INT | Evet | 0 - 4294967295 (0xFFFFFFFF) |

### Notlar

- `prompt` en az bir karakter içermelidir, aksi takdirde oluşturma başarısız olur. Alan varsayılan olarak boş bir dizeye ayarlanmış olsa da, düğümü çalıştırmak için boş olmayan bir istem gerekir.
- `safety_tolerance` 0 ile 4 arasında herhangi bir değeri kabul eder, ancak bu düğüm API'ye bir video gönderdiğinden, seçilen değerden bağımsız olarak etkin tolerans 2 ile sınırlandırılır.
- `duration` bir sayıya ayarlandığında, tam sayı saniyeye dönüştürülür. "auto" özel değeri, servisin uzunluğu içeriğe uydurmasını sağlar.
- `aspect_ratio`, `duration` ve `resolution` için kesin seçenek listeleri düğüm tarafından dahili olarak tanımlanır. Çözünürlük seçenekleri en azından "720p" (varsayılan) ve farklı bir fiyatlandırma oranı kullanan "1080p" içerir.
- Kimlik doğrulama ve düğüm tanımlama alanları (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) gizlidir ve platform tarafından otomatik olarak yönetilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `video` | FLUX 3 tarafından üretilen, kaynak videonun sonundan itibaren devam eden oluşturulmuş devam klibi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/tr.md)

---
**Source fingerprint (SHA-256):** `4b3a3df86b870edd696d10d352c7123b9c6c60ce0b57910529fca60615efa9f9`
