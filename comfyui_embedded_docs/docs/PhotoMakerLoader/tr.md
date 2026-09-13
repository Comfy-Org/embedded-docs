# PhotoMakerYükleyici

PhotoMakerLoader düğümü, mevcut model dosyaları arasından bir PhotoMaker modeli yükler. Seçilen dosyayı okur, ID kodlayıcı ağırlıklarını yükler ve kimlik tabanlı görüntü üretme görevlerinde kullanılmak üzere PhotoMaker ID kodlayıcıyı hazırlar. Bu düğüm deneysel olarak işaretlenmiştir ve test amacıyla kullanılmak üzere tasarlanmıştır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `photomaker_model_name` | Yüklenecek PhotoMaker model dosyasının adı. Kullanılabilir seçenekler `photomaker` klasöründe bulunan model dosyalarına göre belirlenir. | COMBO | Evet | Birden çok seçenek mevcut (`photomaker` klasöründen dinamik olarak doldurulur) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `photomaker_model` | ID kodlayıcıyı içeren yüklenmiş PhotoMaker modeli, kimlik kodlama işlemlerinde kullanıma hazır. | PHOTOMAKER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/tr.md)

---
**Source fingerprint (SHA-256):** `1b26630fadbdc144cd42ca7393f743b079ee7463deb9c8b31b628b5dc7432317`
