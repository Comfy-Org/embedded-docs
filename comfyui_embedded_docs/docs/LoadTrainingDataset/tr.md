# Eğitim Verisetini Yükle

Bu düğüm, daha önce diske kaydedilmiş kodlanmış bir eğitim veri kümesini (latentler ve koşullandırma) yükler. Veri kümeleri dizinindeki seçili veri kümesi klasöründeki tüm veri parçası dosyalarını okur ve eğitim iş akışlarında kullanılmak üzere birleştirilmiş latent vektörlerini ve koşullandırma verilerini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `folder_name` | Veri kümeleri dizininden yüklenecek kaydedilmiş veri kümesi. | COMBO | Evet | Veri kümeleri dizininde bulunan her veri kümesi klasörü için bir seçenek |

Not: `folder_name` seçenekleri, veri kümeleri dizini taranarak otomatik olarak oluşturulur. Bir alt klasör, bir `metadata.json` dosyası veya en az bir `.safetensors` dosyası içerdiğinde veri kümesi olarak listelenir. Seçili veri kümesi klasörü, yapılandırılmış tüm veri kümesi kök dizinlerinde aranır. Bu düğüm, seçili klasördeki `shard_*.pkl` adlı tüm dosyaları okur ve hiçbir parça dosyası bulunmazsa bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latents` | Her biri bir `"samples"` anahtarı ve bir tensör içeren latent sözlüklerinin listesi. | LATENT |
| `conditioning` | Her bir iç liste, ilgili örnek için koşullandırma verilerini içeren koşullandırma listelerinin listesi. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/tr.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
