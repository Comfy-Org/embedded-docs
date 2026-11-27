# Recraft Görüntüyü Vektörleştir

Bir giriş görüntüsünden SVG vektör grafikleri oluşturur. Bu düğüm, her görüntüyü Recraft API'sine göndererek ve sonuçları tek bir SVG çıktısında döndürerek raster görüntüleri ölçeklenebilir vektör formatına dönüştürür. Bu çıktı, işlenen her görüntü için ayrı bir SVG belgesi içerir; belgeler tek bir belgede birleştirilmez.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | SVG formatına dönüştürülecek giriş görüntüsü. Birden çok görüntünün toplu işlenmesini destekler. | IMAGE | Evet | - |
| `sürüm` | Vektörleştirici sürümü: `v1` standart sürümdür ve `v1_pro` (Vectorizer Pro) pürüzsüz eğriler, düz çizgiler ve keskin köşelerle daha temiz SVG'ler üretir; yazı ve karmaşık şekiller için en iyisidir (varsayılan: "v1"). | COMBO | Hayır | "v1"<br>"v1_pro" |
| `shape_stacking` | Şekillerin SVG içinde nasıl istiflendiği: `hierarchical` şekilleri üst üste katmanlar; `cut_out` asla üst üste binmeyen şekiller oluşturur; çiziciler, vinil kesiciler ve serigrafi için uygundur (varsayılan: "hierarchical"). | COMBO | Hayır | "hierarchical"<br>"cut_out" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `SVG` | Oluşturulan vektör grafikleri. Tek SVG çıktısı, işlenen her görüntü için ayrı bir SVG belgesi içerir. | SVG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `b7f8245de0597e8d3ceeef5a15b378e0903965a7e15c1825cacdf2387b278c7e`
