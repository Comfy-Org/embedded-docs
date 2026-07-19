# SeedVR2TemporalChunk

Bu düğüm, bir SeedVR2 video latentini, mevcut VRAM içinde tek tek işlenebilecek daha küçük zamansal parçalara böler. GPU belleğinize göre en uygun parça boyutunu otomatik olarak hesaplar veya parça boyutunu manuel olarak belirlemenize olanak tanır ve parçaları işleme için sırayla çıktı olarak verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `latent` | Bölünecek VAE kodlanmış SeedVR2 latentidir. | LATENT | Evet | - |
| `temporal_overlap` | Bitişik parçalar arasında paylaşılan ve birleştirmede çapraz geçiş yapılan latent karelerdir; 0, örtüşme olmadığı anlamına gelir (varsayılan: 0). | INT | Hayır | 0 ila 16384 |
| `chunking_mode` | Manuel mod, `frames_per_chunk` değerini tam olarak kullanır; otomatik mod, boş VRAM'e sığan en büyük parçayı tahmin eder. | COMBO | Evet | "auto"<br>"manual" |

`chunking_mode` "manual" olarak ayarlandığında, ek bir parametre kullanılabilir hale gelir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|----------|--------|
| `frames_per_chunk` | Zamansal parça başına piksel karesidir. 4n+1 değerinde olmalıdır (1, 5, 9, 13, 17, 21, ...) (varsayılan: 21). | INT | Evet | 1 ila 16384 |

Not: `frames_per_chunk` parametresi yalnızca `chunking_mode` "manual" olarak ayarlandığında görünür. Değer, `(frames_per_chunk - 1) % 4 == 0` formülünü karşılamalıdır, yani şunlardan biri olmalıdır: 1, 5, 9, 13, 17, 21, vb.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `latents` | Zamansal parçalar sıra düzenindedir. | LATENT |
| `temporal_overlap` | Merge SeedVR2 Latents için, bitişik parçalar arasındaki etkin latent-kare örtüşmesidir. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalChunk/tr.md)

---
**Source fingerprint (SHA-256):** `40af2b690f74555efbe38f4cf76825417f52735ce90296a9ad662f78cfe4c6bf`
