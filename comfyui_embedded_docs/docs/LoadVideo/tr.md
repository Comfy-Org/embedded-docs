# Video Yükle

Load Video düğümü, girdi dizininden video dosyalarını yükler ve bunları iş akışında işlenmeye hazır hale getirir. Belirtilen girdi klasöründen video dosyalarını okur ve diğer video işleme düğümlerine bağlanabilecek video verisi olarak çıktı verir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `file` | Girdi dizininden yüklenecek video dosyası. Açılır liste, ComfyUI girdi klasöründe bulunan tüm video dosyalarıyla dinamik olarak doldurulur ve yeni video dosyaları doğrudan dosya seçici aracılığıyla yüklenebilir. | COMBO | Evet | Birden çok seçenek mevcut (girdi dizinindeki tüm video dosyaları) |

**Not:** `file` parametresi için kullanılabilir seçenekler, girdi dizininde bulunan video dosyalarından dinamik olarak doldurulur. Yalnızca desteklenen video içerik türleriyle eşleşen dosyalar görüntülenir ve liste alfabetik olarak sıralanır. Ayrıca düğümün dosya seçici arayüzü aracılığıyla doğrudan yeni bir video dosyası yükleyebilirsiniz. Daha önce seçilen bir video dosyası artık bulunamazsa, düğüm geçersiz dosya hatası bildirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Diğer video işleme düğümlerine daha fazla işleme veya analiz için aktarılabilecek yüklenen video verisi. | VIDEO |

**Not:** Düğüm ayrıca yüklenen videonun bir önizlemesini üretir ve bu önizleme doğrudan düğüm üzerinde görüntülenir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/tr.md)

---
**Source fingerprint (SHA-256):** `dcdd252792ade2a106c11826bbe7344011f0bc08506b80d634043a4dc156e076`
