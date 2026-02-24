> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/tr.md)

LTXV Audio VAE Decode düğümü, bir sesin gizli (latent) temsilini tekrar bir ses dalga formuna dönüştürür. Bu kodlama çözme işlemini gerçekleştirmek için özelleştirilmiş bir Audio VAE modeli kullanır ve belirli bir örnekleme hızına sahip bir ses çıktısı üretir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Evet | Yok | Kodlaması çözülecek gizli (latent) temsil. |
| `audio_vae` | VAE | Evet | Yok | Gizli temsili kodunu çözmek için kullanılan Audio VAE modeli. |

**Not:** Sağlanan gizli temsil iç içe geçmişse (birden fazla gizli temsil içeriyorsa), düğüm kodlama çözme işlemi için otomatik olarak dizideki son gizli temsili kullanacaktır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `Audio` | AUDIO | Kodu çözülmüş ses dalga formu ve ilişkili örnekleme hızı. |
