# Recraft Görüntüyü Vektörleştir

Bir giriş görüntüsünden SVG vektör grafikleri oluşturur. Bu düğüm, her görüntüyü Recraft API'sine göndererek ve sonuçları tek bir SVG çıktısında birleştirerek raster görüntüleri ölçeklenebilir vektör formatına dönüştürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | SVG formatına dönüştürülecek giriş görüntüsü. Birden fazla görüntünün toplu işlenmesini destekler. | IMAGE | Evet | - |
| `version` | Vektörleştirici sürümü: `v1` standart sürümdür ve `v1_pro` (Vectorizer Pro) daha temiz SVG'ler üretir; yumuşak eğriler, düz çizgiler ve keskin köşeler sağlar, özellikle yazılar ve karmaşık şekiller için en iyisidir (varsayılan: "v1"). | COMBO | Hayır | "v1"<br>"v1_pro" |
| `shape_stacking` | Şekillerin SVG'de nasıl katmanlanacağı: `hierarchical` şekilleri üst üste katmanlar; `cut_out`, çiziciler, vinil kesiciler ve serigrafi baskı için şekillerin asla üst üste binmemesini sağlar (varsayılan: "hierarchical"). | COMBO | Hayır | "hierarchical"<br>"cut_out" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `SVG` | İşlenen tüm görüntüleri tek bir SVG belgesinde birleştiren oluşturulmuş vektör grafik çıktısı. | SVG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `b7f8245de0597e8d3ceeef5a15b378e0903965a7e15c1825cacdf2387b278c7e`
