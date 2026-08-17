# ModelÖrneklemeLTXV

ModelSamplingLTXV düğümü, token sayısına göre bir modele gelişmiş örnekleme parametreleri uygular. Taban ve maksimum kaydırma değerleri arasında doğrusal interpolasyon kullanarak bir kaydırma değeri hesaplar; hesaplama, girdi latentindeki token sayısına bağlıdır. Düğüm daha sonra özel bir model örnekleme yapılandırması oluşturur ve bunu girdi modeline uygular.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme parametrelerinin uygulanacağı girdi modeli | MODEL | Evet | - |
| `max_shift` | Doğrusal interpolasyon hesaplamasında kullanılan maksimum kaydırma değeri. Kaydırma değeri, 4096 tokende bu maksimuma eşittir (varsayılan: 2.05) | FLOAT | Evet | 0.0 to 100.0 |
| `base_shift` | Doğrusal interpolasyon hesaplamasında kullanılan taban kaydırma değeri. Kaydırma değeri, 1024 tokende bu tabana eşittir (varsayılan: 0.95) | FLOAT | Evet | 0.0 to 100.0 |
| `latent` | Kaydırma hesaplaması için token sayısını belirlemek amacıyla kullanılan isteğe bağlı latent girdi. Token sayısı, latent örneklerinin uzamsal boyutlarının çarpımıdır. Sağlanmazsa, varsayılan token sayısı olarak 4096 kullanılır | LATENT | Hayır | - |

Not: Kaydırma değeri, 1024 tokendeki `base_shift` ile 4096 tokendeki `max_shift` arasında doğrusal interpolasyonla hesaplanır. `latent` sağlanmadığında, varsayılan token sayısı 4096 olduğundan kaydırma değeri `max_shift` değerine eşit olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Uygulanan örnekleme parametreleriyle birlikte değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/tr.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
