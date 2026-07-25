# Video Kare Örneği

`VideoFrameSample` düğümü, bir videodan dört stratejiden birini kullanarak sabit sayıda kare çıkarır. "head" ve "tail" ardışık stratejileri için çıktı, tembel bir video referansıdır (karelerin kodu çözülmez); "uniform" ve "random" ardışık olmayan stratejiler için yalnızca seçilen karelerin kodu çözülür.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `video` | Giriş videosu. | VIDEO | Evet | – |
| `kare_sayısı` | Örklenecek kare sayısı (varsayılan: 16). | INT | Evet | 1 – 9999 |
| `strateji` | Örnekleme stratejisi (varsayılan: "uniform"). | COMBO | Evet | `"uniform"`<br>`"head"`<br>`"tail"`<br>`"random"` |
| `tohum` | Rastgele tohum, yalnızca "random" stratejisi ile kullanılır (varsayılan: 0). | INT | Evet | 0 – 18446744073709551615 |

- `num_frames`, giriş videosunun toplam kare sayısına otomatik olarak sınırlanır.
- `seed` parametresinin, `strategy` `"random"` olarak ayarlanmadığı sürece hiçbir etkisi yoktur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `video` | Örneklenmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoFrameSample/tr.md)

---
**Source fingerprint (SHA-256):** `727504a9cf7fe5505c33da071cb8f21a38e1b7c0f964c5da172d9cedfc2f2300`
