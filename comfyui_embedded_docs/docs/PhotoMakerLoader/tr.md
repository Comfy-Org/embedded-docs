# PhotoMakerYükleyici

PhotoMakerLoader düğümü, mevcut model dosyalarından bir PhotoMaker modeli yükler. Belirtilen model dosyasını okur ve PhotoMaker ID kodlayıcıyı kimlik tabanlı görüntü oluşturma görevlerinde kullanıma hazırlar. Bu düğüm deneysel olarak işaretlenmiştir ve test amaçlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `photomaker_model_name` | Yüklenecek PhotoMaker model dosyasının adı. Kullanılabilir seçenekler, `photomaker` klasöründe bulunan model dosyalarına göre belirlenir. | COMBO | Evet | Birden fazla seçenek mevcuttur |

Not: Seçilen model dosyası `photomaker` klasöründe mevcut olmalıdır. Belirtilen dosya bulunamazsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `photomaker_model` | Kimlik kodlama işlemlerinde kullanıma hazır, ID kodlayıcıyı içeren yüklenmiş PhotoMaker modeli. | PHOTOMAKER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/tr.md)

---
**Source fingerprint (SHA-256):** `1b26630fadbdc144cd42ca7393f743b079ee7463deb9c8b31b628b5dc7432317`
