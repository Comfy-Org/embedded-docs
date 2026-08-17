# CFG Geçersiz Kılma

CFG Override düğümü, örnekleme sürecinin belirli bir aralığı için toplam adımların yüzdesi olarak tanımlanan sabit bir CFG (Classifier-Free Guidance) ölçek değeri ayarlamanızı sağlar. Birden fazla CFG Override düğümü bağlandığında, zincirde örnekleyiciye en yakın olan, çakışan aralıklarda öncelik alır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | CFG geçersiz kılmanın uygulanacağı model | MODEL | Evet | |
| `cfg` | Geçersiz kılma aralığı boyunca kullanılacak sabit CFG ölçek değeri (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 100.0 |
| `start_percent` | Geçersiz kılma aralığının başlangıç noktası, örnekleme sürecinin yüzdesi olarak (varsayılan: 0.0) | FLOAT | Evet | 0.0 to 1.0 |
| `end_percent` | Geçersiz kılma aralığının bitiş noktası, örnekleme sürecinin yüzdesi olarak (varsayılan: 1.0) | FLOAT | Evet | 0.0 to 1.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | CFG geçersiz kılma sarmalayıcısı uygulanmış model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/tr.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
