SaveImage düğümü, aldığı görselleri `ComfyUI/output` dizininize kaydeder. Her görseli PNG dosyası olarak kaydeder ve prompt gibi iş akışı meta verilerini, ileride başvurmak üzere kaydedilen dosyaya gömmektedir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `görüntüler` | Kaydedilecek görseller. | IMAGE | Evet | - |
| `dosyaadı_öneki` | Kaydedilecek dosyanın ön eki. Bu, düğümlerden değerleri dahil etmek için `%date:yyyy-MM-dd%` veya `%Empty Latent Image.width%` gibi biçimlendirme bilgileri içerebilir (varsayılan: "ComfyUI"). | STRING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `ui` | Bu düğüm, kaydedilen görsellerin dosya adlarını ve alt klasörlerini içeren bir liste olarak bir kullanıcı arayüzü sonucu çıktısı verir. Diğer düğümlere bağlanmak için veri çıktısı sağlamaz. | UI_RESULT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/tr.md)

---
**Source fingerprint (SHA-256):** `fa88c26e5e03f788dcc545434a54124c5e9d03b559da67f0857b52faec0e97e7`
