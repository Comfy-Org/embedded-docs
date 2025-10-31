> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunControlToVideo/tr.md)

Bu düğüm, video oluşturma için Alibaba Wan Fun Control modelini desteklemek amacıyla eklendi ve [bu commit](https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82) sonrasında eklendi.

- **Amaç:** Wan 2.1 Fun Control modelini kullanarak video oluşturma için gerekli olan koşullandırma bilgisini hazırlamak.

WanFunControlToVideo düğümü, video oluşturma için Wan Fun Control modellerini desteklemek üzere tasarlanmış bir ComfyUI eklentisidir ve amacı video oluşturmada WanFun kontrolünü kullanmaktır.

Bu düğüm, temel koşullandırma bilgisi için bir hazırlık noktası görevi görür ve gizli uzayın merkez noktasını başlatarak, Wan 2.1 Fun modeli kullanılarak yapılacak sonraki video oluşturma sürecine rehberlik eder. Düğümün adı işlevini açıkça belirtir: çeşitli girdileri kabul eder ve bunları WanFun çerçevesi içinde video oluşturmayı kontrol etmek için uygun bir formata dönüştürür.

Düğümün ComfyUI düğüm hiyerarşisindeki konumu, video oluşturma işlem hattının erken aşamalarında çalıştığını, video karelerinin gerçek örneklemesi veya kod çözme işleminden önce koşullandırma sinyallerini manipüle etmeye odaklandığını gösterir.

## Girdiler

| Parametre Adı      | Gerekli  | Veri Türü          | Açıklama                                                  | Varsayılan Değer |
|:-------------------|:---------|:-------------------|:-------------------------------------------------------------|:-------------|
| `positive`           | Evet     | CONDITIONING       | Genellikle bir "CLIP Text Encode" düğümünden gelen standart ComfyUI pozitif koşullandırma verisi. Pozitif prompt, kullanıcının oluşturulacak video için öngördüğü içeriği, konuyu ve sanatsal stili tanımlar. | Yok  |
| `negative`           | Evet     | CONDITIONING       | Genellikle bir "CLIP Text Encode" düğümü tarafından oluşturulan standart ComfyUI negatif koşullandırma verisi. Negatif prompt, kullanıcının oluşturulan videoda kaçınmak istediği öğeleri, stilleri veya artefaktları belirtir. | Yok  |
| `vae`                | Evet     | VAE                | Wan 2.1 Fun model ailesi ile uyumlu, görüntü/video verilerini kodlamak ve kodunu çözmek için kullanılan bir VAE (Varyasyonel Otokodlayıcı) modeli gerektirir. | Yok  |
| `width`              | Evet     | INT                | Piksel cinsinden çıktı video karelerinin istenen genişliği. Varsayılan değer 832, minimum değer 16, maksimum değer `nodes.MAX_RESOLUTION` tarafından belirlenir ve adım boyutu 16'dır. | 832  |
| `height`             | Evet     | INT                | Piksel cinsinden çıktı video karelerinin istenen yüksekliği. Varsayılan değer 480, minimum değer 16, maksimum değer `nodes.MAX_RESOLUTION` tarafından belirlenir ve adım boyutu 16'dır. | 480  |
| `length`             | Evet     | INT                | Oluşturulan videodaki toplam kare sayısı. Varsayılan değer 81, minimum değer 1, maksimum değer `nodes.MAX_RESOLUTION` tarafından belirlenir ve adım boyutu 4'tür. | 81   |
| `batch_size`         | Evet     | INT                | Tek bir partide oluşturulan video sayısı. Varsayılan değer 1, minimum değer 1 ve maksimum değer 4096'dır. | 1    |
| `clip_vision_output` | Hayır    | CLIP_VISION_OUTPUT | (İsteğe bağlı) Bir CLIP görüntü modeli tarafından çıkarılan görsel özellikler; görsel stil ve içerik rehberliğine olanak tanır. | Yok |
| `start_image`        | Hayır    | IMAGE              | (İsteğe bağlı) Oluşturulan videonun başlangıcını etkileyen bir başlangıç görüntüsü. | Yok |
| `control_video`      | Hayır    | IMAGE              | (İsteğe bağlı) Kullanıcıların, oluşturulan videonun hareketini ve potansiyel yapısını yönlendirecek önceden işlenmiş bir ControlNet referans videosu sağlamasına olanak tanır.| Yok |

## Çıktılar

| Parametre Adı      | Veri Türü          | Açıklama                                                  |
|:-------------------|:-------------------|:-------------------------------------------------------------|
| `positive`           | CONDITIONING       | Kodlanmış `start_image` ve `control_video`'yu içeren geliştirilmiş pozitif koşullandırma verisini sağlar. |
| `negative`           | CONDITIONING       | Aynı `concat_latent_image`'ı içeren, aynı zamanda geliştirilmiş negatif koşullandırma verisini sağlar. |
| `latent`             | LATENT             | "samples" anahtarına sahip boş bir gizli tensör içeren bir sözlük. |