PhotoMakerLoader düğümü, mevcut model dosyalarından bir PhotoMaker modeli yükler. Belirtilen model dosyasını okur ve kimlik tabanlı görüntü oluşturma görevlerinde kullanılmak üzere PhotoMaker kimlik kodlayıcısını hazırlar. Bu düğüm deneysel olarak işaretlenmiştir ve test amaçlı kullanım içindir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `photomaker_model_adı` | Yüklenecek PhotoMaker model dosyasının adı. Mevcut seçenekler, `photomaker` klasöründe bulunan model dosyalarına göre belirlenir. | STRING | Evet | Birden çok seçenek mevcut |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `photomaker_model` | Yüklenmiş, kimlik kodlama işlemlerinde kullanıma hazır PhotoMaker modelini (kimlik kodlayıcıyı içerir) temsil eder. | PHOTOMAKER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/tr.md)

---
**Source fingerprint (SHA-256):** `4c55abacf8462d8de3d1f2a728d4b09ab1d1c8c6476d25cc4af5089508a721da`
