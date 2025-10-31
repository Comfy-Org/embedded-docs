> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/tr.md)

ChromaRadianceOptions düğümü, Chroma Radiance modeli için gelişmiş ayarları yapılandırmanıza olanak tanır. Mevcut bir modeli sarar ve sigma değerlerine dayalı olarak gürültü giderme işlemi sırasında belirli seçenekleri uygular, böylece NeRF döşeme boyutu ve diğer radyansla ilgili parametreler üzerinde hassas kontrol sağlar.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | Gerekli | - | - | Chroma Radiance seçeneklerinin uygulanacağı model |
| `preserve_wrapper` | BOOLEAN | İsteğe Bağlı | True | - | Etkinleştirildiğinde, mevcutsa var olan bir model fonksiyon sarmalayıcısına yetki devreder. Genellikle etkin bırakılmalıdır. |
| `start_sigma` | FLOAT | İsteğe Bağlı | 1.0 | 0.0 - 1.0 | Bu seçeneklerin geçerli olacağı ilk sigma değeri. |
| `end_sigma` | FLOAT | İsteğe Bağlı | 0.0 | 0.0 - 1.0 | Bu seçeneklerin geçerli olacağı son sigma değeri. |
| `nerf_tile_size` | INT | İsteğe Bağlı | -1 | -1 ve üzeri | Varsayılan NeRF döşeme boyutunun geçersiz kılınmasına izin verir. -1, varsayılan değerin (32) kullanılacağı anlamına gelir. 0, döşeme olmayan modun kullanılacağı anlamına gelir (çok fazla VRAM gerektirebilir). |

**Not:** Chroma Radiance seçenekleri yalnızca mevcut sigma değeri `end_sigma` ve `start_sigma` (dahil) arasında olduğunda geçerli olur. `nerf_tile_size` parametresi yalnızca 0 veya daha yüksek değerlere ayarlandığında uygulanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Chroma Radiance seçenekleri uygulanmış olarak değiştirilmiş model |