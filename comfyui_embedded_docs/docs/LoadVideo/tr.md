> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/tr.md)

Video Yükle düğümü, giriş dizininden video dosyalarını yükler ve iş akışında işlenmek üzere kullanılabilir hale getirir. Belirlenen giriş klasöründen video dosyalarını okur ve diğer video işleme düğümlerine bağlanabilen video verisi olarak çıktı verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `dosya` | STRING | Evet | Birden fazla seçenek mevcut | Giriş dizininden yüklenecek video dosyası |

**Not:** `file` parametresi için mevcut seçenekler, giriş dizininde bulunan video dosyalarından dinamik olarak doldurulur. Yalnızca desteklenen içerik türlerine sahip video dosyaları görüntülenir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Diğer video işleme düğümlerine aktarılabilen yüklenmiş video verisi |