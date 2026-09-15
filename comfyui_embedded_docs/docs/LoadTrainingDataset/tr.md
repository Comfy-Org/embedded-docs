# Eğitim Verisetini Yükle

Bu düğüm, daha önce diske kaydedilmiş kodlanmış bir eğitim veri kümesini (latentler ve koşullandırma) yükler. Veri kümeleri dizinindeki seçili bir veri kümesi klasöründen tüm `shard_*.pkl` veri parçası dosyalarını okur ve eğitim iş akışlarında kullanılmak üzere birleştirilmiş latent vektörlerini ve koşullandırma verilerini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `folder_name` | Veri kümeleri dizininden yüklenecek kayıtlı veri kümesi. | COMBO | Evet | Veri kümeleri dizininde bulunan her veri kümesi klasörü için bir seçenek |

Not: `folder_name` seçenekleri, veri kümeleri dizini taranarak otomatik olarak oluşturulur. Bir alt klasör, bir `metadata.json` dosyası veya en az bir `.safetensors` dosyası içerdiğinde veri kümesi olarak listelenir (tarama, eşleşen bir klasörün içine girmez). Seçilen veri kümesi klasörü, yapılandırılmış tüm veri kümesi kök dizinlerinde aranır ve klasör adı bu köklerden birinin içindeki bir alt klasöre çözümlenmelidir. Düğüm, seçilen klasördeki `shard_*.pkl` adlı tüm dosyaları sıralı düzende okur ve hiç parça dosyası bulunamazsa veya klasör bulunamazsa bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latents` | Her biri tensör içeren bir `"samples"` anahtarı barındıran latent sözlüklerinin listesi (çıktı listesi). | LATENT |
| `conditioning` | Koşullandırma listelerinin listesi (çıktı listesi); burada her iç liste, karşılık gelen örnek için koşullandırma verilerini içerir. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/tr.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
