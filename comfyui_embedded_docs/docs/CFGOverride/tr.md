# CFG Geçersiz Kılma

CFG Geçersiz Kılma düğümü, toplam adımların yüzdesi olarak tanımlanan, örnekleme sürecinin belirli bir aralığı için sabit bir CFG (Sınıflandırıcısız Kılavuzluk) ölçeği değeri belirlemenizi sağlar. Birden fazla CFG Geçersiz Kılma düğümü bağlandığında, zincirde örnekleyiciye en yakın olan düğüm, çakışan aralıklar için öncelik alır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model` | CFG geçersiz kılmanın uygulanacağı model | MODEL | Evet | |
| `cfg` | Geçersiz kılma aralığı boyunca kullanılacak sabit CFG ölçeği değeri (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 100.0 arası |
| `başlangıç_yüzdesi` | Örnekleme sürecinin yüzdesi olarak geçersiz kılma aralığının başlangıç noktası (varsayılan: 0.0) | FLOAT | Evet | 0.0 ile 1.0 arası |
| `bitiş_yüzdesi` | Örnekleme sürecinin yüzdesi olarak geçersiz kılma aralığının bitiş noktası (varsayılan: 1.0) | FLOAT | Evet | 0.0 ile 1.0 arası |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `MODEL` | CFG geçersiz kılma sarmalayıcısı uygulanmış model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/tr.md)

---
**Source fingerprint (SHA-256):** `1fe57a4e78a2f18c4e7da49fa7a6c473d64dc0ebf6662535dfb5379c37936662`
