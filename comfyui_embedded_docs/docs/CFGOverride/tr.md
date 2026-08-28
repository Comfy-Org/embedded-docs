# CFG Geçersiz Kılma

CFG Override düğümü, toplam adımların yüzdesi olarak tanımlanan, örnekleme sürecinin belirli bir aralığı için sabit bir CFG (Classifier-Free Guidance) ölçek değeri ayarlamanızı sağlar. Birden fazla CFG Override düğümü bağlandığında, zincirde örnekleyiciye en yakın olan düğüm, çakışan aralıklarda önceliğe sahiptir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | CFG geçersiz kılmanın uygulanacağı model | MODEL | Evet | |
| `cfg` | Geçersiz kılma aralığı boyunca kullanılacak sabit CFG ölçek değeri (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 100.0 |
| `başlangıç_yüzdesi` | Geçersiz kılma aralığının, örnekleme sürecinin yüzdesi olarak başlangıç noktası (varsayılan: 0.0) | FLOAT | Evet | 0.0 ile 1.0 |
| `bitiş_yüzdesi` | Geçersiz kılma aralığının, örnekleme sürecinin yüzdesi olarak bitiş noktası (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | CFG geçersiz kılma sarmalayıcısı uygulanmış model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/tr.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
