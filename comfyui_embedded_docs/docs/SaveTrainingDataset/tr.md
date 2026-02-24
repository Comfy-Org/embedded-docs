> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/tr.md)

Bu düğüm, hazırlanmış bir eğitim veri kümesini bilgisayarınızın sabit diskine kaydeder. Görüntü gizli temsillerini (latents) ve bunlara karşılık gelen metin koşullandırmalarını içeren kodlanmış verileri alır ve daha kolay yönetim için bunları parça (shard) adı verilen birden fazla küçük dosyaya düzenler. Düğüm, çıktı dizininizde otomatik olarak bir klasör oluşturur ve hem veri dosyalarını hem de veri kümesini tanımlayan bir meta veri dosyasını kaydeder.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Evet | Yok | MakeTrainingDataset düğümünden gelen gizli temsil (latent) sözlüklerinin listesi. |
| `conditioning` | CONDITIONING | Evet | Yok | MakeTrainingDataset düğümünden gelen koşullandırma (conditioning) listelerinin listesi. |
| `folder_name` | STRING | Hayır | Yok | Veri kümesini kaydetmek için kullanılacak klasör adı (çıktı dizini içinde). (varsayılan: "training_dataset") |
| `shard_size` | INT | Hayır | 1 - 100000 | Her bir parça (shard) dosyasına düşen örnek sayısı. (varsayılan: 1000) |

**Not:** `latents` listesindeki öğe sayısı, `conditioning` listesindeki öğe sayısıyla tam olarak eşleşmelidir. Bu sayılar eşleşmezse düğüm bir hata verecektir.

## Çıkışlar

Bu düğüm herhangi bir çıktı verisi üretmez. İşlevi, dosyaları diskinize kaydetmektir.
