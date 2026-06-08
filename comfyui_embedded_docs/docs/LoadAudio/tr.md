# LoadAudio Düğümü

LoadAudio düğümü, girdi dizininden ses dosyalarını yükler ve ComfyUI'deki diğer ses düğümleri tarafından işlenebilecek bir formata dönüştürür. Ses dosyalarını okuyarak hem dalga biçimi verilerini hem de örnekleme hızını çıkarır ve bunları aşağı yönlü ses işleme görevleri için kullanılabilir hale getirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | Girdi dizininden yüklenecek ses dosyası | AUDIO | Evet | Girdi dizinindeki desteklenen tüm ses ve video dosyaları |

**Not:** Düğüm yalnızca ComfyUI'nin girdi dizininde bulunan ses ve video dosyalarını kabul eder. Başarılı yükleme için dosyanın mevcut ve erişilebilir olması gerekir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `AUDIO` | Dalga biçimi ve örnekleme hızı bilgilerini içeren ses verisi | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadAudio/tr.md)

---
**Source fingerprint (SHA-256):** `a7fe63cbbb3a854359189e8685936a2b8b855e22c3c282fc77affacf640af010`
