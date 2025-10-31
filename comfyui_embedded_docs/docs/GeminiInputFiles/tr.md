> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiInputFiles/tr.md)

Gemini API ile kullanım için giriş dosyalarını yükler ve biçimlendirir. Bu düğüm, kullanıcıların Gemini modeli için giriş bağlamı olarak metin (.txt) ve PDF (.pdf) dosyalarını eklemesine olanak tanır. Dosyalar, API tarafından gereken uygun formata dönüştürülür ve tek bir istekte birden fazla dosya eklemek için birbirine zincirlenebilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `file` | COMBO | Evet | Birden fazla seçenek mevcut | Modele bağlam olarak eklenecek giriş dosyaları. Şu an için yalnızca metin (.txt) ve PDF (.pdf) dosyalarını kabul eder. Dosyalar maksimum giriş dosyası boyut sınırından küçük olmalıdır. |
| `GEMINI_INPUT_FILES` | GEMINI_INPUT_FILES | Hayır | Yok | Bu düğümden yüklenen dosya ile birlikte toplu işlemek için isteğe bağlı ek dosya(lar). Tek bir mesajın birden fazla giriş dosyası içermesini sağlamak için giriş dosyalarının zincirlenmesine olanak tanır. |

**Not:** `file` parametresi yalnızca maksimum giriş dosyası boyut sınırından küçük olan metin (.txt) ve PDF (.pdf) dosyalarını görüntüler. Dosyalar otomatik olarak filtrelenir ve ada göre sıralanır.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `GEMINI_INPUT_FILES` | GEMINI_INPUT_FILES | Yüklenen dosya içeriğini uygun API formatında içeren, Gemini LLM düğümleriyle kullanıma hazır biçimlendirilmiş dosya verisi. |