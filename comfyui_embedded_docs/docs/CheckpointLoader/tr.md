CheckpointLoader düğümü, önceden eğitilmiş bir model kontrol noktasını (checkpoint) ve yapılandırma dosyasını yükler. Giriş olarak bir yapılandırma dosyası ve bir kontrol noktası dosyası alır; çıktı olarak ise ana model, CLIP modeli ve VAE modeli dahil olmak üzere yüklenen model bileşenlerini iş akışında kullanılmak üzere döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `yapılandırma_adı` | Model mimarisini ve ayarlarını tanımlayan yapılandırma dosyası | STRING | Evet | Kullanılabilir yapılandırma dosyaları |
| `ckpt_adı` | Eğitilmiş model ağırlıklarını ve parametrelerini içeren kontrol noktası dosyası | STRING | Evet | Kullanılabilir kontrol noktası dosyaları |

**Not:** Bu düğüm, hem bir yapılandırma dosyası hem de bir kontrol noktası dosyasının seçilmesini gerektirir. Yapılandırma dosyası, yüklenen kontrol noktası dosyasının mimarisiyle eşleşmelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Çıkarım için hazır, yüklenmiş ana model bileşeni | MODEL |
| `CLIP` | Metin kodlama için yüklenmiş CLIP model bileşeni | CLIP |
| `VAE` | Görüntü kodlama ve kod çözme için yüklenmiş VAE model bileşeni | VAE |

**Önemli Not:** Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir ve gelecek sürümlerde kaldırılabilir. Yeni iş akışları için alternatif yükleme düğümlerini kullanmayı değerlendirin.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/tr.md)

---
**Source fingerprint (SHA-256):** `9977bda5e124a9d10566839cbee868c74fab120c454141f27ce145efa60105e9`
