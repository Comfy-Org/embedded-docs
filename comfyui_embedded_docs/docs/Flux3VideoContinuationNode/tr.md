# Flux 3 Video Devamı

Bu düğüm, mevcut bir video klibini FLUX 3 ile devam ettirir: yeni klip, sağladığınız videonun son karelerinden itibaren devam eder. Kaynak klibinizi yükler, prompt'u ve ayarları üretim hizmetine gönderir ve hazır olduğunda ortaya çıkan devam videosunu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Devam ettirilecek klip. | VIDEO | Evet | Tek video klibi |
| `prompt` | Devam klibinin ne göstermesi gerektiği; prompt üretimden önce yorumlanır ve genişletilir. (varsayılan: "") | STRING | Evet | Boş olmayan metin (en az 1 karakter) |
| `aspect_ratio` | Çıktı en-boy oranı. 'auto', prompt'tan ve girdilerden birini seçer. (varsayılan: "auto") | COMBO | Evet | "auto" (varsayılan)<br>Birden fazla ön tanımlı seçenek |
| `duration` | Klibin saniye cinsinden uzunluğu. 'auto', uzunluğu içeriğe göre ayarlar. (varsayılan: "auto") | COMBO | Evet | "auto" (varsayılan)<br>Saniye cinsinden sayısal değerler |
| `resolution` | Çıktı çözünürlüğü. (varsayılan: "720p") | COMBO | Evet | "720p" (varsayılan)<br>"1080p"<br>Diğer ön tanımlı seçenekler |
| `generate_audio` | Senkronize ses üret (ortam sesi, konuşma, efektler). Kapalı, ses parçası olmayan bir video üretir. (varsayılan: true) | BOOLEAN | Evet | true<br>false |
| `safety_tolerance` | Moderasyon toleransı, 0 en katıdır. Görsel veya video gönderen istekler, burada ne ayarlanırsa ayarlansın 2 ile sınırlandırılır. (gelişmiş parametre, varsayılan: 2) | INT | Evet | 0 - 4 (video istekleri için etkin maksimum: 2) |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum; FLUX 3 kendi tohumunu seçer, bu nedenle bu değerden bağımsız olarak gerçek sonuçlar deterministik değildir. (gelişmiş parametre, varsayılan: 42) | INT | Evet | 0 - 4294967295 (0xFFFFFFFF) |

### Notlar

- `prompt` en az bir karakter içermelidir, aksi takdirde üretim başarısız olur. Alan varsayılan olarak boş bir dize olsa da, düğümü çalıştırmak için boş olmayan bir prompt gereklidir.
- `safety_tolerance` 0 ile 4 arasında herhangi bir değeri kabul eder, ancak bu düğüm API'ye bir video gönderdiğinden, seçilen değerden bağımsız olarak etkin tolerans 2 ile sınırlandırılmıştır.
- `duration` bir sayıya ayarlandığında, saniye cinsinden bir tam sayıya dönüştürülür. "auto" özel değeri, hizmetin uzunluğu içeriğe göre ayarlamasını sağlar.
- `aspect_ratio`, `duration` ve `resolution` için kesin seçenek listeleri düğüm tarafından dahili olarak tanımlanır. Çözünürlük seçenekleri en azından "720p" (varsayılan) ve "1080p" içerir. Fiyatlandırma, seçilen `resolution` ve `duration`'a göre hesaplanır; "1080p" saniye başına 0,7579 $, diğer çözünürlükler ise saniye başına 0,5863 $ üzerinden faturalandırılır.
- Kimlik doğrulama ve düğüm tanımlama alanları (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) gizlidir ve platform tarafından otomatik olarak yönetilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | FLUX 3 tarafından üretilen, kaynak videonun sonundan itibaren devam eden oluşturulmuş devam klibi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/tr.md)

---
**Source fingerprint (SHA-256):** `129ad0eb62c368854cebb010cc886aecac4caab00f9111143b883d028d7c30d9`
