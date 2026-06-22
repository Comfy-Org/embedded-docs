# Video Yükle

Video Yükle düğümü, giriş dizininden video dosyalarını yükler ve bunları iş akışında işlenmek üzere kullanılabilir hale getirir. Belirlenen giriş klasöründen video dosyalarını okur ve bunları diğer video işleme düğümlerine bağlanabilen video verileri olarak çıktılar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `dosya` | Giriş dizininden yüklenecek video dosyası. Açılır liste, ComfyUI giriş klasöründe bulunan tüm video dosyalarıyla dinamik olarak doldurulur. | STRING | Evet | Birden çok seçenek mevcut |

**Not:** `file` parametresi için mevcut seçenekler, giriş dizininde bulunan video dosyalarından dinamik olarak doldurulur. Yalnızca desteklenen içerik türlerine sahip video dosyaları görüntülenir. Ayrıca düğümün dosya seçici arayüzü aracılığıyla doğrudan yeni bir video dosyası yükleyebilirsiniz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Daha fazla işleme veya analiz için diğer video işleme düğümlerine aktarılabilen yüklenmiş video verileri. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/tr.md)

---
**Source fingerprint (SHA-256):** `e3d18eb43cba34734761b5b147d9fee91fe3ca99db21f9e19a130efc3349cecb`
