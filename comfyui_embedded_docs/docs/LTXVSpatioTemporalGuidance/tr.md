# LTXV Uzamsal-Zamansal Yönlendirme (STG)

Bu düğüm, her örnekleme adımında ek bir geçiş çalıştırarak LTXV video üretiminin uzamsal ayrıntısını ve hareket tutarlılığını iyileştirir. Bu geçiş sırasında, seçili transformatör bloklarının öz-dikkat mekanizması değer geçişli (value-passthrough) durumuna düşürülür ve üretim, bozulmuş sonuçtan uzağa yönlendirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Uzamsal-zamansal yönlendirmenin uygulanacağı temel model. Model kopyalanır ve CFG sonrası bir yönlendirme işleviyle değiştirilir. | MODEL | Evet | — |
| `ölçek` | Gürültüsü giderilmiş sonuca uygulanan yönlendirmenin gücü. 0 olarak ayarlandığında yönlendirmenin etkisi olmaz. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 100.0 (adım 0.01) |
| `bloklar` | Bozulacak virgülle ayrılmış transformatör blok dizinleri. Yalnızca sayısal değerler kullanılır; diğer tüm karakterler yok sayılır. (varsayılan: "29") | STRING | Evet | — |
| `başlangıç_yüzdesi` | Yönlendirmenin başladığı örnekleme sürecinin oranı. Bu gelişmiş bir parametredir. (varsayılan: 0.0) | FLOAT | Evet | 0.0 ile 1.0 (adım 0.001) |
| `bitiş_yüzdesi` | Yönlendirmenin sona erdiği örnekleme sürecinin oranı. Bu gelişmiş bir parametredir. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 (adım 0.001) |

Not: Yönlendirme yalnızca `start_percent` ile `end_percent` arasındaki örnekleme aralığında uygulanır. `scale` 0 ise veya `blocks` sayısal değer içermiyorsa, yönlendirilmiş geçişin örnekleme süreci üzerinde etkisi olmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | Uzamsal-zamansal yönlendirme işlevi eklenmiş kopyalanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`
