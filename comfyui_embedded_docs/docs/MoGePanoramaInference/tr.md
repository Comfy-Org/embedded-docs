> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/tr.md)

# Genel Bakış

Bu düğüm, eşdikdörtgen panorama görüntülerinde derinlik tahmini gerçekleştirir. Panaromayı 12 perspektif görüntüye bölerek, her bir görüntü üzerinde MoGe derinlik tahmin modelini çalıştırır ve ardından sonuçları orijinal panorama için tek ve eksiksiz bir derinlik haritasında birleştirir.

# Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `moge_model` | MOGE_MODEL | Evet | | Çıkarım için kullanılacak MoGe modeli. |
| `image` | GÖRÜNTÜ | Evet | | Eşdikdörtgen panorama görüntüsü (herhangi bir en-boy oranı). |
| `resolution_level` | TAMSAYI | Evet | 0 ile 9 | Görüntü başına detay seviyesi. Daha yüksek değerler daha ayrıntılı derinlik haritaları üretir (varsayılan: 9). |
| `split_resolution` | TAMSAYI | Evet | 256 ile 1024 | Panorama bölündükten sonra her bir perspektif görüntünün çözünürlüğü (varsayılan: 512). |
| `merge_resolution` | TAMSAYI | Evet | 256 ile 8192 | Birleştirilmiş eşdikdörtgen derinlik haritasının uzun kenar çözünürlüğü (varsayılan: 1920). |
| `batch_size` | TAMSAYI | Evet | 1 ile 12 | Her çıkarım grubunda işlenecek perspektif görüntü sayısı. Toplam görüntü sayısı 12'dir (varsayılan: 4). |

# Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `moge_geometry` | MOGE_GEOMETRY | Tahmini geometriyi içeren bir sözlük: `points` (3B nokta bulutu), `depth` (derinlik haritası), `mask` (geçerli alan maskesi) ve `image` (giriş görüntüsü). |

---
**Source fingerprint (SHA-256):** `3a701e3679bc35cd5fddc54868ac9c4bc9b4e23a5b97bbf61e46b7309e43600b`
