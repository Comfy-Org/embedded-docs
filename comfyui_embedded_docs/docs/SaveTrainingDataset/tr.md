# Eğitim Veri Setini Kaydet

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `latents` | MakeTrainingDataset'ten gelen latent sözlüklerinin listesi. | LATENT | Evet | N/A |
| `conditioning` | MakeTrainingDataset'ten gelen conditioning listelerinin listesi. | CONDITIONING | Evet | N/A |
| `folder_name` | Veri kümesinin kaydedileceği klasörün adı; datasets dizini içinde. 'project/run1' gibi alt klasörlere izin verilir. (varsayılan: "training_dataset") | STRING | Evet | N/A |
| `shard_size` | Parça dosyası başına örnek sayısı. (varsayılan: 1000) | INT | Evet | 1 - 100000 |

**Not:** `latents` içindeki öğe sayısı, `conditioning` içindeki öğe sayısıyla tam olarak eşleşmelidir; bu sayılar eşleşmezse düğüm hata verir. `folder_name`, datasets dizininin bir alt klasörünü adlandırmalıdır (örneğin `my_dataset`) — datasets dizininin kendisi olamaz ve datasets dizini dışında bir yol oluşturacak klasör adları reddedilir. `shard_size` parametresi gelişmiş bir ayardır.

## Çıktılar

Bu düğüm herhangi bir çıktı verisi üretmez. İşlevi, diskinize dosya kaydetmektir. Her parça, seçilen klasörde `shard_XXXX.pkl` dosyası olarak kaydedilir ve bir `metadata.json` dosyası toplam örnek sayısını, parça sayısını ve parça boyutunu kaydeder.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/tr.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
