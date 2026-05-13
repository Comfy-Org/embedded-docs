> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunControlToVideo/tr.md)

Bu düğüm, video oluşturma için Alibaba Wan Fun Control modelini desteklemek amacıyla eklenmiş olup, [bu commit](https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82) sonrasında eklenmiştir.

- **Amaç:** Wan 2.1 Fun Control modelini kullanarak video oluşturma için gerekli koşullandırma bilgilerini hazırlamak.

WanFunControlToVideo düğümü, video oluşturma için Wan Fun Control modellerini desteklemek üzere tasarlanmış bir ComfyUI eklentisidir ve video oluşturmada WanFun kontrolünü kullanmayı amaçlar.

Bu düğüm, temel koşullandırma bilgileri için bir hazırlık noktası görevi görür ve gizli uzayın merkez noktasını başlatarak Wan 2.1 Fun modelini kullanarak sonraki video oluşturma sürecini yönlendirir. Düğümün adı, işlevini açıkça belirtir: çeşitli girdileri alır ve bunları WanFun çerçevesinde video oluşturmayı kontrol etmeye uygun bir formata dönüştürür.

Düğümün ComfyUI düğüm hiyerarşisindeki konumu, video oluşturma hattının erken aşamalarında çalıştığını ve video karelerinin fiilen örneklenmesi veya kod çözülmesinden önce koşullandırma sinyallerini işlemeye odaklandığını gösterir.

## Girdiler

| Parametre Adı      | Gerekli | Veri Türü           | Açıklama                                                  | Varsayılan Değer |
|:-------------------|:---------|:-------------------|:-------------------------------------------------------------|:-------------|
| positive           | Evet      | CONDITIONING       | Standart ComfyUI pozitif koşullandırma verisi, genellikle bir "CLIP Text Encode" düğümünden gelir. Pozitif istem, kullanıcının oluşturulan video için hayal ettiği içeriği, konuyu ve sanatsal stili tanımlar. | N/A  |
| negative           | Evet      | CONDITIONING       | Standart ComfyUI negatif koşullandırma verisi, genellikle bir "CLIP Text Encode" düğümü tarafından oluşturulur. Negatif istem, kullanıcının oluşturulan videoda kaçınmak istediği öğeleri, stilleri veya yapaylıkları belirtir. | N/A  |
| vae                | Evet      | VAE                | Wan 2.1 Fun model ailesiyle uyumlu bir VAE (Değişken Otomatik Kodlayıcı) modeli gerektirir; görüntü/video verilerini kodlamak ve çözmek için kullanılır. | N/A  |
| width              | Evet      | INT                | Çıktı video karelerinin piksel cinsinden istenen genişliği; varsayılan değer 832, minimum değer 16, maksimum değer nodes.MAX_RESOLUTION tarafından belirlenir ve adım boyutu 16'dır. | 832  |
| height             | Evet      | INT                | Çıktı video karelerinin piksel cinsinden istenen yüksekliği; varsayılan değer 480, minimum değer 16, maksimum değer nodes.MAX_RESOLUTION tarafından belirlenir ve adım boyutu 16'dır. | 480  |
| length             | Evet      | INT                | Oluşturulan videodaki toplam kare sayısı; varsayılan değer 81, minimum değer 1, maksimum değer nodes.MAX_RESOLUTION tarafından belirlenir ve adım boyutu 4'tür. | 81   |
| batch_size         | Evet      | INT                | Tek bir yığında oluşturulan video sayısı; varsayılan değer 1, minimum değer 1 ve maksimum değer 4096'dır. | 1    |
| clip_vision_output | Hayır       | CLIP_VISION_OUTPUT | (İsteğe bağlı) Bir CLIP görme modeli tarafından çıkarılan görsel özellikler; görsel stil ve içerik yönlendirmesine olanak tanır. | Yok |
| start_image        | Hayır       | IMAGE              | (İsteğe bağlı) Oluşturulan videonun başlangıcını etkileyen bir başlangıç görüntüsü. | Yok |
| control_video      | Hayır       | IMAGE              | (İsteğe bağlı) Kullanıcıların, oluşturulan videonun hareketini ve potansiyel yapısını yönlendirecek önceden işlenmiş bir ControlNet referans videosu sağlamasına olanak tanır.| Yok |

## Çıktılar

| Parametre Adı      | Veri Türü           | Açıklama                                                  |
|:-------------------|:-------------------|:-------------------------------------------------------------|
| positive           | CONDITIONING       | Kodlanmış start_image ve control_video dahil olmak üzere gelişmiş pozitif koşullandırma verileri sağlar. |
| negative           | CONDITIONING       | Aynı concat_latent_image'i içeren, aynı zamanda geliştirilmiş negatif koşullandırma verileri sağlar. |
| latent             | LATENT             | "samples" anahtarına sahip boş bir gizli tensör içeren bir sözlük. |