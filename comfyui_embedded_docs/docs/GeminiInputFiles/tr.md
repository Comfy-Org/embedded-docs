# Gemini Girdi Dosyaları

Gemini API ile kullanılmak üzere girdi dosyalarını yükler ve biçimlendirir. Bu düğüm, kullanıcıların Gemini modeli için girdi bağlamı olarak metin (.txt) ve PDF (.pdf) dosyalarını eklemesine olanak tanır. Dosyalar, API tarafından gereken uygun biçime dönüştürülür ve tek bir istekte birden fazla dosyayı bir araya getirmek için zincirleme olarak kullanılabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `dosya` | Modele bağlam olarak eklenecek girdi dosyaları. Şimdilik yalnızca metin (.txt) ve PDF (.pdf) dosyalarını kabul eder. Dosyalar, maksimum girdi dosyası boyut sınırından küçük olmalıdır. | COMBO | Evet | Birden çok seçenek mevcut |
| `GEMINI_GİRDİ_DOSYALARI` | Bu düğümden yüklenen dosyayla birlikte toplu olarak işlenecek isteğe bağlı ek dosya(lar). Tek bir mesajın birden çok girdi dosyası içermesi için girdi dosyalarının zincirlenmesine olanak tanır. | GEMINI_INPUT_FILES | Hayır | Yok |

**Not:** `file` parametresi yalnızca maksimum girdi dosyası boyut sınırından küçük olan metin (.txt) ve PDF (.pdf) dosyalarını görüntüler. Dosyalar otomatik olarak filtrelenir ve ada göre sıralanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GEMINI_GİRDİ_DOSYALARI` | Gemini LLM düğümleriyle kullanıma hazır, yüklenen dosya içeriğini uygun API biçiminde içeren biçimlendirilmiş dosya verisi. | GEMINI_INPUT_FILES |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiInputFiles/tr.md)

---
**Source fingerprint (SHA-256):** `54da8696d144513efa9660fbc5ddbf5480da12eafe4d2791c8e81cd207ef8a52`
