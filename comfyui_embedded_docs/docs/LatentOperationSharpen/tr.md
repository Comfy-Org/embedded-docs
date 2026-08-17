# GizliİşlemKeskinleştirme

LatentOperationSharpen düğümü, Gauss çekirdeği kullanarak latent gösterimlere keskinleştirme efekti uygular. Latent verilerini normalleştirir, özel bir keskinleştirme çekirdeği ile konvolüsyon uygular ve ardından orijinal parlaklığı geri yükler. Bu, latent uzay gösterimindeki ayrıntıları ve kenarları geliştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `sharpen_radius` | Keskinleştirme çekirdeğinin yarıçapı. Tam çekirdek boyutu, bu değerin iki katı artı bir olarak hesaplanır (varsayılan: 9). | INT | Evet | 1-31 |
| `sigma` | Gauss çekirdeğinin standart sapması (varsayılan: 1.0). | FLOAT | Evet | 0.1-10.0 |
| `alpha` | Efektin gücünü kontrol eden keskinleştirme yoğunluk faktörü (varsayılan: 0.1). | FLOAT | Evet | 0.0-5.0 |

Tüm girdiler gelişmiş parametrelerdir. Bu düğüm deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `operation` | Latent verilere uygulanabilen bir keskinleştirme işlemi. Bir latente uygulandığında, orijinal parlaklığı korunmuş keskinleştirilmiş bir sürüm döndürür. | LATENT_OPERATION |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/tr.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
