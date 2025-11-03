> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/tr.md)

AudioConcat düğümü, iki ses girişini birleştirerek birleştirir. İki ses girişini alır ve sizin belirttiğiniz sırayla bağlar; ikinci sesi birinci sesten önce veya sonra yerleştirir. Düğüm, mono sesi stereo'ya dönüştürerek ve iki giriş arasındaki örnekleme hızlarını eşleştirerek farklı ses formatlarını otomatik olarak halleder.

## Girişler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `audio1` | AUDIO | gerekli | - | - | Birleştirilecek ilk ses girişi |
| `audio2` | AUDIO | gerekli | - | - | Birleştirilecek ikinci ses girişi |
| `direction` | COMBO | gerekli | after | ['after', 'before'] | audio2'nin audio1'den sonra mı yoksa önce mi ekleneceği |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | Her iki giriş ses dosyasının birleştirilmiş halini içeren ses |