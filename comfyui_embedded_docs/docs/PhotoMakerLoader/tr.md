> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/tr.md)

PhotoMakerLoader düğümü, mevcut model dosyalarından bir PhotoMaker modeli yükler. Belirtilen model dosyasını okur ve kimlik tabanlı görüntü oluşturma görevlerinde kullanılmak üzere PhotoMaker ID kodlayıcısını hazırlar. Bu düğüm deneysel olarak işaretlenmiştir ve test amaçlarıyla kullanılmak üzere tasarlanmıştır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `photomaker_model_name` | STRING | Evet | Birden fazla seçenek mevcut | Yüklenecek PhotoMaker model dosyasının adı. Mevcut seçenekler, photomaker klasöründe bulunan model dosyaları tarafından belirlenir. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `photomaker_model` | PHOTOMAKER | Kimlik kodlama işlemlerinde kullanıma hazır, ID kodlayıcıyı içeren yüklenmiş PhotoMaker modeli. |