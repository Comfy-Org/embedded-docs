## Genel Bakış

APG (Uyarlanabilir Projeksiyonlu Yönlendirme) düğümü, difüzyon sırasında yönlendirmenin nasıl uygulandığını ayarlayarak örnekleme sürecini değiştirir. Yönlendirme vektörünü, koşullu çıktıya göre paralel ve dik bileşenlerine ayırarak daha kontrollü görüntü oluşturulmasını sağlar. Düğüm, yönlendirmeyi ölçeklendirmek, büyüklüğünü normalleştirmek ve difüzyon adımları arasında daha yumuşak geçişler için momentum uygulamak üzere parametreler sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Uyarlanabilir projeksiyonlu yönlendirmenin uygulanacağı difüzyon modeli | MODEL | Evet | - |
| `eta` | Paralel yönlendirme vektörünün ölçeğini kontrol eder. 1 değerinde varsayılan CFG davranışı (varsayılan: 1.0). | FLOAT | Evet | -10.0 ile 10.0 |
| `norm_threshold` | Yönlendirme vektörünü bu değere normalleştirir, 0 değerinde normalleştirme devre dışı bırakılır (varsayılan: 5.0). | FLOAT | Evet | 0.0 ile 50.0 |
| `momentum` | Difüzyon sırasında yönlendirmenin hareketli ortalamasını kontrol eder, 0 değerinde devre dışı bırakılır (varsayılan: 0.0). | FLOAT | Evet | -5.0 ile 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Örnekleme sürecine uyarlanabilir projeksiyonlu yönlendirme uygulanmış değiştirilmiş modeli döndürür | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/tr.md)

---
**Source fingerprint (SHA-256):** `89e2486bf08f750f82608db93c389f0b25ce0be766f62faa8704d19bd7e41654`
