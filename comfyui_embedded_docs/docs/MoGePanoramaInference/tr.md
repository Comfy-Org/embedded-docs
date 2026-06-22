# MoGe Panorama Çıkarımı

Bu düğüm, eşdikdörtgen panorama görüntülerinde derinlik tahmini gerçekleştirir. Panaromayı 12 perspektif görüntüye bölerek, her bir görüntü üzerinde MoGe derinlik tahmin modelini çalıştırır ve ardından sonuçları orijinal panorama için tek ve eksiksiz bir derinlik haritasında birleştirir.

# Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `moge_model` | Çıkarım için kullanılacak MoGe modeli. | MOGE_MODEL | Evet |  |
| `image` | Eşdikdörtgen panorama görüntüsü (herhangi bir en-boy oranı). | GÖRÜNTÜ | Evet |  |
| `resolution_level` | Görüntü başına detay seviyesi. Daha yüksek değerler daha ayrıntılı derinlik haritaları üretir (varsayılan: 9). | TAMSAYI | Evet | 0 ile 9 |
| `split_resolution` | Panorama bölündükten sonra her bir perspektif görüntünün çözünürlüğü (varsayılan: 512). | TAMSAYI | Evet | 256 ile 1024 |
| `merge_resolution` | Birleştirilmiş eşdikdörtgen derinlik haritasının uzun kenar çözünürlüğü (varsayılan: 1920). | TAMSAYI | Evet | 256 ile 8192 |
| `batch_size` | Her çıkarım grubunda işlenecek perspektif görüntü sayısı. Toplam görüntü sayısı 12'dir (varsayılan: 4). | TAMSAYI | Evet | 1 ile 12 |

# Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `moge_geometry` | Tahmini geometriyi içeren bir sözlük: `points` (3B nokta bulutu), `depth` (derinlik haritası), `mask` (geçerli alan maskesi) ve `image` (giriş görüntüsü). | MOGE_GEOMETRY |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/tr.md)

---
**Source fingerprint (SHA-256):** `3a701e3679bc35cd5fddc54868ac9c4bc9b4e23a5b97bbf61e46b7309e43600b`
