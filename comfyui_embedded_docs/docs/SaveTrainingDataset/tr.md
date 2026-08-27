# Eğitim Veri Setini Kaydet

Bu düğüm, eğitim sırasında verimli yükleme için kodlanmış bir eğitim veri kümesini diske kaydeder. Görüntü latentlerini ve bunlarla eşleşen metin conditioning verilerini alır, bunları shard adı verilen daha küçük dosyalara böler ve datasets dizini içindeki bir klasöre depolar. Ayrıca veri kümesini tanımlayan bir metadata dosyası da yazar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `latents` | MakeTrainingDataset'ten latent sözlüklerinin listesi. | LATENT | Evet | YOK |
| `conditioning` | MakeTrainingDataset'ten conditioning listelerinin listesi. | CONDITIONING | Evet | YOK |
| `folder_name` | Veri kümesinin kaydedileceği, datasets dizini içindeki klasörün adı. 'project/run1' gibi alt klasörlere izin verilir. (varsayılan: "training_dataset") | STRING | Evet | YOK |
| `shard_size` | Shard dosyası başına örnek sayısı. (varsayılan: 1000) | INT | Evet | 1 ile 100000 arası |

**Not:** `latents` içindeki öğe sayısı, `conditioning` içindeki öğe sayısıyla tam olarak eşleşmelidir; bu sayılar eşleşmezse düğüm bir hata verir. `folder_name`, datasets dizininin bir alt klasörünü adlandırmalıdır (örneğin `my_dataset`) — datasets dizininin kendisi olamaz ve datasets dizini dışına çözümlenen klasör adları reddedilir.

## Çıktılar

Bu düğüm herhangi bir çıktı verisi üretmez. İşlevi, dosyaları diskinize kaydetmektir. Her shard, seçilen klasöre `shard_XXXX.pkl` dosyası olarak kaydedilir ve bir `metadata.json` dosyası toplam örnek sayısını, shard sayısını ve shard boyutunu kaydeder.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/tr.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
