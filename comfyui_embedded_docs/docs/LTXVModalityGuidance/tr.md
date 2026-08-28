# LTXV Mod Modu Yönlendirme (A/V eşleşmesi)

Bu düğüm, bir LTXV-AV modeline modaliteler arası (ses-görüntü) rehberlik uygular. Örnekleme sırasında, ses-görüntü ve görüntü-ses çapraz dikkat bağlantıları devre dışı bırakılmış halde her adımda fazladan bir ileri geçiş çalıştırır ve sonucu eşleştirilmiş tahmine doğru iterek dudak senkronizasyonu gibi ses-görüntü senkronizasyonunu güçlendirir. `modality_scale` için referans varsayılan değeri 3.0'dır; 1.0'a ayarlamak ekstra geçişi devre dışı bırakır ve bu, çift-CFG kılavuzu ve STG ile birlikte çalışır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Modalite rehberliğinin uygulanacağı temel model. Dahili olarak kopyalanır ve orijinal model değişmeden kalır. | MODEL | Evet | - |
| `modality_scale` | Ses-görüntü birleştirme rehberliğinin gücü. Varsayılan 3.0'dır. Ekstra ileri geçişi devre dışı bırakmak için 1.0'a ayarlayın. | FLOAT | Evet | 1.0 ila 100.0 (varsayılan: 3.0) |
| `başlangıç_yüzdesi` | Örnekleme sürecinde modalite rehberliğinin başladığı nokta (0.0 ile 1.0 arasında bir yüzde olarak). Bu gelişmiş bir parametredir. Varsayılan 0.0'dır. | FLOAT | Evet | 0.0 ila 1.0 (varsayılan: 0.0) |
| `bitiş_yüzdesi` | Örnekleme sürecinde modalite rehberliğinin bittiği nokta (0.0 ile 1.0 arasında bir yüzde olarak). Bu gelişmiş bir parametredir. Varsayılan 1.0'dır. | FLOAT | Evet | 0.0 ila 1.0 (varsayılan: 1.0) |

Rehberlik yalnızca sigma değerleri `start_percent` ve `end_percent` tarafından tanımlanan aralığa giren örnekleme adımlarına uygulanır. Bu aralığın dışında, düğüm gürültüden arındırılmış sonucu değiştirmeden döndürür. `modality_scale` değerinin 1.0 olması da ekstra ileri geçişi tamamen devre dışı bırakır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | CFG sonrası rehberlik işlevi eklenmiş kopyalanmış model. Bu değiştirilmiş model, örnekleme sırasında modalite rehberliği uygular. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVModalityGuidance/tr.md)

---
**Source fingerprint (SHA-256):** `038be607c42e626a8a8f5fe336ee466d0847d43835edb71e20ff38f668069cfb`
