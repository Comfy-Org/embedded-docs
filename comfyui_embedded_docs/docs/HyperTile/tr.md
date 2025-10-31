> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/tr.md)

HyperTile düğümü, görüntü oluşturma sırasında bellek kullanımını optimize etmek için yayılım modellerindeki dikkat mekanizmasına bir döşeme tekniği uygular. Gizli uzayı daha küçük karolara böler ve bunları ayrı ayrı işler, ardından sonuçları yeniden birleştirir. Bu, bellek tükenmeden daha büyük görüntü boyutlarıyla çalışmaya olanak tanır.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | HyperTile optimizasyonunun uygulanacağı yayılım modeli |
| `döşeme_boyutu` | INT | Hayır | 1-2048 | İşleme için hedef karoların boyutu (varsayılan: 256) |
| `değiştirme_boyutu` | INT | Hayır | 1-128 | İşleme sırasında karoların nasıl yeniden düzenleneceğini kontrol eder (varsayılan: 2) |
| `maks_derinlik` | INT | Hayır | 0-10 | Döşemenin uygulanacağı maksimum derinlik seviyesi (varsayılan: 0) |
| `ölçek_derinliği` | BOOLEAN | Hayır | - | Karonun boyutunun derinlik seviyesine göre ölçeklenip ölçeklenmeyeceği (varsayılan: False) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | HyperTile optimizasyonu uygulanmış, değiştirilmiş model |