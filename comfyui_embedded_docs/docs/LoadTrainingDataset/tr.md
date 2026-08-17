# Eğitim Verisetini Yükle

Bu düğüm, eğitimde kullanılmak üzere diskten kodlanmış bir eğitim veri kümesini (latentler ve koşullandırma) yükler. Önceden kaydedilmiş bir veri kümesi klasörü seçtikten sonra, içindeki tüm parça dosyalarını okur ve birleştirilmiş latent vektörlerini ve koşullandırma verilerini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `folder_name` | Yüklenecek kaydedilmiş veri kümesi, veri kümeleri dizininden. | COMBO | Evet | Kayıtlı veri kümesi dizinlerinde bulunan tüm veri kümesi klasörleriyle dinamik olarak doldurulur. Yalnızca `metadata.json` dosyası veya `.safetensors` dosyaları içeren klasörler listelenir. |

**Not:** Seçilen veri kümesi klasörü, kayıtlı bir veri kümesi dizininin alt klasörü olmalı ve en az bir `shard_*.pkl` parça dosyası içermelidir; aksi takdirde düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `latents` | Veri kümesi parçalarından yüklenen latent sözlüklerinin listesi; her biri bir `samples` tensörü içerir. | LATENT |
| `conditioning` | Veri kümesi parçalarından yüklenen koşullandırma listelerinin listesi; her örnek için bir tane. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/tr.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
