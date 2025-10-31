> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/tr.md)

DiffusersLoader düğümü, önceden eğitilmiş modelleri diffusers formatından yükler. Model dizinlerinde model_index.json dosyası içeren geçerli diffusers model dizinlerini arar ve bunları MODEL, CLIP ve VAE bileşenleri olarak yükleyerek pipeline'da kullanıma hazır hale getirir. Bu düğüm, kullanımdan kaldırılmış yükleyiciler kategorisinin bir parçasıdır ve Hugging Face diffusers modelleriyle uyumluluk sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model_yolu` | STRING | Evet | Birden fazla seçenek mevcut<br>(diffusers klasörlerinden otomatik doldurulur) | Yüklenecek diffusers model dizininin yolu. Düğüm, yapılandırılmış diffusers klasörlerinde geçerli diffusers modellerini otomatik olarak tarar ve mevcut seçenekleri listeler. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `MODEL` | MODEL | Diffusers formatından yüklenen model bileşeni |
| `CLIP` | CLIP | Diffusers formatından yüklenen CLIP model bileşeni |
| `VAE` | VAE | Diffusers formatından yüklenen VAE (Değişimli Otokodlayıcı) bileşeni |