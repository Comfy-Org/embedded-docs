# SeedVR2TemporalChunk

Bu düğüm, bir SeedVR2 video latentini daha küçük, örtüşen zamansal parçalara böler; böylece her bir parça mevcut VRAM içinde tek tek işlenebilir. Parçalar, hem Apply SeedVR2 Conditioning düğümüne hem de örnekleyici latent girdisine aktarılmak ve daha sonra Merge SeedVR2 Latents düğümü kullanılarak yeniden birleştirilmek üzere tasarlanmıştır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `latent` | Bölünecek VAE kodlu SeedVR2 latent | LATENT | Evet | - |
| `temporal_overlap` | Bitişik parçalar arasında paylaşılan ve birleştirmede çapraz geçiş yapılan latent kareler; 0 örtüşme olmadığı anlamına gelir (varsayılan: 0) | INT | Hayır | 0 ile 16384 |
| `chunking_mode` | manual = frames_per_chunk değerini tam olarak kullanır; auto = boş VRAM'e sığacak en büyük parçayı tahmin eder | COMBO | Evet | "auto"<br>"manual" |

`chunking_mode` "manual" olarak ayarlandığında aşağıdaki parametre kullanılabilir hale gelir:

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `frames_per_chunk` | Zamansal parça başına piksel karesi (4n+1 olmalıdır: 1, 5, 9, 13, ...) (varsayılan: 21) | INT | Evet | 1 ile 16384, adım 4 |

**Parametre kısıtlamalarına ilişkin notlar:**
- Girdi `latent`, (B, C, T, H, W) şeklinde 5 boyutlu bir video latent olmalı ve tam olarak 4 latent kanala sahip olmalıdır
- "manual" modu kullanılırken `frames_per_chunk` bir 4n+1 değeri olmalıdır (1, 5, 9, 13, 17, 21, ...)
- `temporal_overlap` otomatik olarak parça boyutundan daha küçük olacak şekilde sınırlandırılır
- "auto" modunda düğüm, mevcut boş VRAM'e göre en uygun parça boyutunu hesaplar

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `latents` | Sıralı düzende zamansal parçalar | LATENT |
| `temporal_overlap` | Merge SeedVR2 Latents için bitişik parçalar arasındaki etkin latent-kare örtüşmesi | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalChunk/tr.md)

---
**Source fingerprint (SHA-256):** `40af2b690f74555efbe38f4cf76825417f52735ce90296a9ad662f78cfe4c6bf`
