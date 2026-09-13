# CFG Geçersiz Kılma

CFG Override düğümü, örnekleme sürecinin bir yüzde (sigma) aralığı boyunca CFG (Sınıflandırıcısız Yönlendirme) ölçeğini sabit bir değere geçersiz kılar. Birden fazla CFG Override düğümü kullanıldığında, çakışan aralıklarda örnekleyiciye en yakın geçersiz kılma kazanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | CFG geçersiz kılma işleminin uygulanacağı model. | MODEL | Evet | |
| `cfg` | Geçersiz kılma aralığı boyunca kullanılacak sabit CFG ölçeği değeri. Varsayılan: 1.0. | FLOAT | Evet | 0.0 ile 100.0 (step: 0.1) |
| `başlangıç_yüzdesi` | Geçersiz kılma aralığının, örnekleme sürecinin yüzdesi olarak başlangıç noktası. Varsayılan: 0.0. | FLOAT | Evet | 0.0 ile 1.0 (step: 0.001) |
| `bitiş_yüzdesi` | Geçersiz kılma aralığının, örnekleme sürecinin yüzdesi olarak bitiş noktası. Varsayılan: 1.0. | FLOAT | Evet | 0.0 ile 1.0 (step: 0.001) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | CFG geçersiz kılma sarmalayıcısı uygulanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/tr.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
