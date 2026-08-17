# Eğitim Veri Setini Kaydet

Bu düğüm, hazırlanmış bir eğitim veri kümesini bilgisayarınızın sabit diskine kaydeder. Görüntü latentlerini ve bunlara karşılık gelen metin koşullandırmasını içeren kodlanmış veriyi alır ve daha kolay yönetim için bunları shard adı verilen birden çok küçük dosyaya düzenler. Düğüm, datasets dizininde otomatik olarak bir klasör oluşturur ve hem shard veri dosyalarını hem de veri kümesini açıklayan bir meta veri dosyasını kaydeder.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `latents` | MakeTrainingDataset'ten latent sözlüklerinin listesi. | LATENT | Evet | N/A |
| `conditioning` | MakeTrainingDataset'ten koşullandırma listelerinin listesi. | CONDITIONING | Evet | N/A |
| `folder_name` | Veri kümesinin kaydedileceği, datasets dizini içindeki klasörün adı. 'project/run1' gibi alt klasörlere izin verilir. (varsayılan: "training_dataset") | STRING | Evet | N/A |
| `shard_size` | Shard dosyası başına örnek sayısı. (varsayılan: 1000) | INT | Evet | 1 to 100000 |

**Not:** `latents` listesindeki öğe sayısı, `conditioning` listesindeki öğe sayısıyla tam olarak eşleşmelidir. Bu sayılar eşleşmezse düğüm bir hata verir. `folder_name`, datasets dizininin bir alt klasörünü adlandırmalıdır: datasets kök klasörünün kendisi ve onun dışına çıkan herhangi bir yol ('..' veya mutlak bir yol gibi) reddedilir.

## Çıktılar

Bu düğüm herhangi bir çıktı verisi üretmez. Veri kümesini, datasets dizinindeki seçilen klasöre numaralı shard dosyaları (örneğin `shard_0000.pkl`) ve bir `metadata.json` dosyası olarak kaydeder.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/tr.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
