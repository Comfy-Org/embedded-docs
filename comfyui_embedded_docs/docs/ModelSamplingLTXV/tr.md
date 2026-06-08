ModelSamplingLTXV düğümü, token sayısına bağlı olarak bir modele gelişmiş örnekleme parametreleri uygular. Temel ve maksimum kaydırma değerleri arasında doğrusal enterpolasyon kullanarak bir kaydırma değeri hesaplar; bu hesaplama, giriş latenti içindeki token sayısına bağlıdır. Düğüm daha sonra özelleştirilmiş bir model örnekleme yapılandırması oluşturur ve bunu giriş modeline uygular.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Örnekleme parametrelerinin uygulanacağı giriş modeli | MODEL | Evet | - |
| `maks_kaydırma` | Doğrusal enterpolasyon hesaplamasında kullanılan maksimum kaydırma değeri (varsayılan: 2,05) | FLOAT | Evet | 0,0 - 100,0 |
| `temel_kaydırma` | Doğrusal enterpolasyon hesaplamasında kullanılan temel kaydırma değeri (varsayılan: 0,95) | FLOAT | Evet | 0,0 - 100,0 |
| `gizli` | Kaydırma hesaplaması için token sayısını belirlemek amacıyla kullanılan isteğe bağlı latent girişi. Sağlanmazsa, varsayılan token sayısı olarak 4096 kullanılır | LATENT | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Uygulanan örnekleme parametreleriyle birlikte değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/tr.md)

---
**Source fingerprint (SHA-256):** `2325754df1b2541a6adbdebecefde92e08535af0e179d7444093a61eb35cb24c`
