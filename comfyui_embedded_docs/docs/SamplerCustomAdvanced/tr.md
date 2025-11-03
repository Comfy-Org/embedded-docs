> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/tr.md)

SamplerCustomAdvanced düğümü, özel gürültü, yönlendirme ve örnekleme yapılandırmaları kullanarak gelişmiş latent uzay örneklemesi gerçekleştirir. Bir latent görüntüyü, özelleştirilebilir gürültü üretimi ve sigma çizelgeleri ile yönlendirilmiş bir örnekleme sürecinden geçirir ve hem nihai örneklenmiş çıktıyı hem de mevcut olduğunda gürültüsüzleştirilmiş bir versiyonu üretir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `gürültü` | NOISE | Evet | - | Örnekleme süreci için başlangıç gürültü desenini ve seed değerini sağlayan gürültü üreteci |
| `rehber` | GUIDER | Evet | - | Örnekleme sürecini istenen çıktılara yönlendiren yönlendirme modeli |
| `örnekleyici` | SAMPLER | Evet | - | Üretim sırasında latent uzayın nasıl gezinileceğini tanımlayan örnekleme algoritması |
| `sigmalar` | SIGMAS | Evet | - | Örnekleme adımları boyunca gürültü seviyelerini kontrol eden sigma çizelgesi |
| `gizli_görüntü` | LATENT | Evet | - | Örnekleme için başlangıç noktası olarak hizmet eden başlangıç latent temsili |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `gürültüsü_alınmış_çıktı` | LATENT | Örnekleme süreci tamamlandıktan sonra elde edilen nihai örneklenmiş latent temsil |
| `denoised_output` | LATENT | Mevcut olduğunda çıktının gürültüsüzleştirilmiş bir versiyonu, aksi takdirde çıktı ile aynısını döndürür |