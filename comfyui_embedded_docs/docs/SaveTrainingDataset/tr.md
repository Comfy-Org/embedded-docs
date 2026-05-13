> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/tr.md)

Bu node, hazırlanmış bir eğitim veri kümesini bilgisayarınızın sabit diskine kaydeder. Görüntü gizil değişkenlerini (latents) ve bunlara karşılık gelen metin koşullandırmasını içeren kodlanmış verileri alır ve daha kolay yönetim için bunları parça (shard) adı verilen birden fazla küçük dosyaya düzenler. Node, çıktı dizininizde otomatik olarak bir klasör oluşturur ve hem veri dosyalarını hem de veri kümesini tanımlayan bir meta veri dosyasını kaydeder.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Evet | Yok | MakeTrainingDataset'ten alınan gizil değişken sözlüklerinin listesi. |
| `conditioning` | CONDITIONING | Evet | Yok | MakeTrainingDataset'ten alınan koşullandırma listelerinin listesi. |
| `folder_name` | STRING | Hayır | Yok | Veri kümesinin kaydedileceği klasörün adı (çıktı dizini içinde). (varsayılan: "training_dataset") |
| `shard_size` | INT | Hayır | 1 ile 100000 | Parça dosyası başına düşen örnek sayısı. (varsayılan: 1000) |

**Not:** `latents` listesindeki öğe sayısı, `conditioning` listesindeki öğe sayısıyla tam olarak eşleşmelidir. Bu sayılar eşleşmezse node bir hata verecektir.

## Çıktılar

Bu node herhangi bir çıktı verisi üretmez. İşlevi, dosyaları diskinize kaydetmektir.

---
**Source fingerprint (SHA-256):** `1b0108be7362c0cb8ba16ffbf94cf42be2d04159aacbabe1ff0890083d1733b3`
