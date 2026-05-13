> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/tr.md)

ModelSamplingLTXV düğümü, token sayısına bağlı olarak bir modele gelişmiş örnekleme parametreleri uygular. Temel ve maksimum kaydırma değerleri arasında doğrusal enterpolasyon kullanarak bir kaydırma değeri hesaplar; bu hesaplama, giriş latenti içindeki token sayısına bağlıdır. Düğüm daha sonra özelleştirilmiş bir model örnekleme yapılandırması oluşturur ve bunu giriş modeline uygular.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-----------|
| `model` | MODEL | Evet | - | Örnekleme parametrelerinin uygulanacağı giriş modeli |
| `max_shift` | FLOAT | Evet | 0,0 - 100,0 | Doğrusal enterpolasyon hesaplamasında kullanılan maksimum kaydırma değeri (varsayılan: 2,05) |
| `base_shift` | FLOAT | Evet | 0,0 - 100,0 | Doğrusal enterpolasyon hesaplamasında kullanılan temel kaydırma değeri (varsayılan: 0,95) |
| `latent` | LATENT | Hayır | - | Kaydırma hesaplaması için token sayısını belirlemek amacıyla kullanılan isteğe bağlı latent girişi. Sağlanmazsa, varsayılan token sayısı olarak 4096 kullanılır |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Uygulanan örnekleme parametreleriyle birlikte değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `2325754df1b2541a6adbdebecefde92e08535af0e179d7444093a61eb35cb24c`
