> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/tr.md)

LTXVSeparateAVLatent düğümü, birleşik bir görsel-işitsel gizli temsili alır ve onu iki ayrı parçaya böler: biri video, diğeri ses için. Girdi gizli temsilinden örnekleri ve varsa gürültü maskelerini ayırarak iki yeni gizli nesne oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `av_latent` | LATENT | Evet | Yok | Ayrıştırılacak birleşik görsel-işitsel gizli temsil. |

**Not:** Girdi gizli temsilinin `samples` tensörünün ilk boyutunda (batch boyutu) en az iki öğe olması beklenir. İlk öğe video gizli temsili için, ikinci öğe ise ses gizli temsili için kullanılır. Eğer bir `noise_mask` mevcutsa, aynı şekilde bölünür.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video_latent` | LATENT | Ayrıştırılmış video verilerini içeren gizli temsil. |
| `audio_latent` | LATENT | Ayrıştırılmış ses verilerini içeren gizli temsil. |
