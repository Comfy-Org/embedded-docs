> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadAudio/tr.md)

LoadAudio düğümü, giriş dizininden ses dosyalarını yükler ve ComfyUI'deki diğer ses düğümleri tarafından işlenebilecek bir formata dönüştürür. Ses dosyalarını okur ve hem dalga formu verilerini hem de örnekleme hızını çıkararak, aşağı yönlü ses işleme görevleri için kullanılabilir hale getirir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ses` | AUDIO | Evet | Giriş dizinindeki desteklenen tüm ses/video dosyaları | Giriş dizininden yüklenecek ses dosyası |

**Not:** Düğüm yalnızca ComfyUI'nin giriş dizininde bulunan ses ve video dosyalarını kabul eder. Dosyanın başarılı bir şekilde yüklenebilmesi için mevcut ve erişilebilir olması gerekir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | Dalga formu ve örnekleme hızı bilgilerini içeren ses verisi |