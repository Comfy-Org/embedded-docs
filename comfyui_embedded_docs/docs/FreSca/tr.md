> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreSca/tr.md)

FreSca düğümü, örnekleme sürecinde kılavuzluğa frekansa bağlı ölçeklendirme uygular. Fourier filtreleme kullanarak kılavuz sinyalini düşük frekanslı ve yüksek frekanslı bileşenlere ayırır, ardından her frekans aralığına farklı ölçeklendirme faktörleri uygulayarak yeniden birleştirir. Bu, kılavuzluğun oluşturulan çıktının farklı yönlerini nasıl etkilediği üzerinde daha incelikli bir kontrol sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | - | Frekans ölçeklendirmesinin uygulanacağı model |
| `düşük_ölçek` | FLOAT | Hayır | 0 - 10 | Düşük frekanslı bileşenler için ölçeklendirme faktörü (varsayılan: 1,0) |
| `yüksek_ölçek` | FLOAT | Hayır | 0 - 10 | Yüksek frekanslı bileşenler için ölçeklendirme faktörü (varsayılan: 1,25) |
| `frekans_kesme` | INT | Hayır | 1 - 10000 | Merkez etrafında düşük frekans olarak kabul edilecek frekans indekslerinin sayısı (varsayılan: 20) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | Kılavuzluk fonksiyonuna frekansa bağlı ölçeklendirme uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `254a28847e082739f80c9637d9657ef618d40db1862b6856c1cda22436438ded`
