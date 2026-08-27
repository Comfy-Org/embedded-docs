# LTXVSpatioTemporalGuidance

Bu düğüm, her örnekleme adımında ekstra bir geçiş çalıştırarak LTXV video üretiminin uzamsal ayrıntısını ve hareket tutarlılığını iyileştirir. Bu geçiş sırasında, seçilen transformatör bloklarının öz-dikkati bir değer-doğrudan iletimine indirgenir ve üretim, indirgenmiş sonuçtan uzağa yönlendirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Uzamsal-zamansal rehberliğin uygulanacağı temel model. Model kopyalanır ve CFG sonrası rehberlik işleviyle değiştirilir. | MODEL | Evet | — |
| `ölçek` | Gürültü giderme sonucuna uygulanan rehberliğin gücü. 0 olarak ayarlandığında rehberliğin etkisi olmaz. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 100.0 (adım 0.01) |
| `bloklar` | Bozulacak virgülle ayrılmış transformatör blok dizinleri. Yalnızca sayısal değerler kullanılır; diğer tüm karakterler yok sayılır. (varsayılan: "29") | STRING | Evet | — |
| `başlangıç_yüzdesi` | Rehberliğin başladığı örnekleme sürecinin kesri. (varsayılan: 0.0) | FLOAT | Evet | 0.0 ila 1.0 (adım 0.001) |
| `bitiş_yüzdesi` | Rehberliğin bittiği örnekleme sürecinin kesri. (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 (adım 0.001) |

Not: Rehberlik yalnızca `start_percent` ile `end_percent` arasındaki örnekleme aralığında uygulanır. `scale` 0 ise veya `blocks` sayısal değer içermiyorsa, rehberli geçişin örnekleme sürecine etkisi olmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | Uzamsal-zamansal rehberlik işlevi eklenmiş kopyalanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`
