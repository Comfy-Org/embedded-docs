# Video Kırp (Zamansal Rastgele)

Giriş videosundan sürekli bir kare aralığını rastgele kırpar. Tutulacak kare sayısı `length` parametresiyle ayarlanır ve başlangıç konumu `seed` parametresi kullanılarak rastgele seçilir. Düğüm tembel bir şekilde çalışır, yani çıktı aşağı akışta kullanılana kadar videonun tamamını işlemez.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Giriş videosu. | VIDEO | Evet | – |
| `uzunluk` | Tutulacak kare sayısı. `uzunluk`, videodaki toplam kare sayısından büyükse videonun tamamı tutulur. (varsayılan: 16) | INT | Evet | min: 1, max: 99999 |
| `tohum` | Rastgele tohum. (varsayılan: 0) | INT | Evet | min: 0, max: 0xFFFFFFFFFFFFFFFF |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Kırpılmış video (tembel). | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoRandomTemporalCrop/tr.md)

---
**Source fingerprint (SHA-256):** `8249feb5ac3607fcabf3de0ec4d2eb90ab4aa46c18613040c341b825c9db1b1e`
