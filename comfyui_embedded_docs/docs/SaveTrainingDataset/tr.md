# Eğitim Veri Setini Kaydet

Bu node, hazırlanmış bir eğitim veri kümesini bilgisayarınızın sabit diskine kaydeder. Görüntü gizil değişkenlerini (latents) ve bunlara karşılık gelen metin koşullandırmasını içeren kodlanmış verileri alır ve daha kolay yönetim için bunları parça (shard) adı verilen birden fazla küçük dosyaya düzenler. Node, çıktı dizininizde otomatik olarak bir klasör oluşturur ve hem veri dosyalarını hem de veri kümesini tanımlayan bir meta veri dosyasını kaydeder.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `latents` | MakeTrainingDataset'ten alınan gizil değişken sözlüklerinin listesi. | LATENT | Evet | Yok |
| `conditioning` | MakeTrainingDataset'ten alınan koşullandırma listelerinin listesi. | CONDITIONING | Evet | Yok |
| `folder_name` | Veri kümesinin kaydedileceği klasörün adı (çıktı dizini içinde). (varsayılan: "training_dataset") | STRING | Hayır | Yok |
| `shard_size` | Parça dosyası başına düşen örnek sayısı. (varsayılan: 1000) | INT | Hayır | 1 ile 100000 |

**Not:** `latents` listesindeki öğe sayısı, `conditioning` listesindeki öğe sayısıyla tam olarak eşleşmelidir. Bu sayılar eşleşmezse node bir hata verecektir.

## Çıktılar

Bu node herhangi bir çıktı verisi üretmez. İşlevi, dosyaları diskinize kaydetmektir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/tr.md)

---
**Source fingerprint (SHA-256):** `1b0108be7362c0cb8ba16ffbf94cf42be2d04159aacbabe1ff0890083d1733b3`
