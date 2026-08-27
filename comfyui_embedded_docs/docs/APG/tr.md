# Uyarlanabilir Projeksiyonlu Kılavuzluk

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Adaptif projeksiyonlu kılavuzun uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `eta` | Paralel kılavuz vektörünün ölçeğini kontrol eder. 1 ayarında varsayılan CFG davranışı (varsayılan: 1.0). | FLOAT | Evet | -10.0 ile 10.0 |
| `norm_threshold` | Kılavuz vektörünü bu değere normalleştirir; 0 ayarında normalleştirme devre dışıdır (varsayılan: 5.0). | FLOAT | Evet | 0.0 ile 50.0 |
| `momentum` | Difüzyon sırasında kılavuzun hareketli ortalamasını kontrol eder; 0 ayarında devre dışıdır (varsayılan: 0.0). | FLOAT | Evet | -5.0 ile 1.0 |

Not: Örnekleme sırasında gürültü seviyesi (`sigma`) arttığında, momentum hareketli ortalaması sıfıra sıfırlanır. Model yalnızca tek bir koşullandırma çıktısı sağlıyorsa (ayrı bir koşulsuz koşullandırma yoksa), kılavuz ayarlaması atlanır ve koşullandırma değiştirilmeden bırakılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `model` | Örnekleme sürecine adaptif projeksiyonlu kılavuz uygulanmış değiştirilmiş modeli döndürür | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/tr.md)

---
**Source fingerprint (SHA-256):** `df0c76aee28479d49c4e471e54d1d32082adc6921a6a50b506675144a79e018a`
