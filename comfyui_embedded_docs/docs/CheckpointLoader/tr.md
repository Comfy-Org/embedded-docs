# Yapılandırmayla Kontrol Noktası Yükle (ESKİ)

CheckpointLoader düğümü, önceden eğitilmiş bir model kontrol noktasını (checkpoint) yapılandırma dosyasıyla birlikte yükler. Girdi olarak bir yapılandırma dosyası ve bir kontrol noktası dosyası alır; iş akışında kullanılmak üzere ana model, CLIP modeli ve VAE modeli dahil yüklenen model bileşenlerini döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `config_name` | Model mimarisini ve ayarlarını tanımlayan yapılandırma dosyası | STRING | Evet | Available config files |
| `ckpt_name` | Eğitilmiş model ağırlıklarını ve parametrelerini içeren kontrol noktası dosyası | STRING | Evet | Available checkpoint files |

**Not:** Bu düğüm, hem bir yapılandırma dosyası hem de bir kontrol noktası dosyası seçilmesini gerektirir. Yapılandırma dosyası, yüklenen kontrol noktası dosyasının mimarisiyle eşleşmelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Çıkarım için hazır, yüklenmiş ana model bileşeni | MODEL |
| `CLIP` | Metin kodlama için yüklenmiş CLIP model bileşeni | CLIP |
| `VAE` | Görüntü kodlama ve kod çözme için yüklenmiş VAE model bileşeni | VAE |

**Önemli Not:** Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir ve gelecek sürümlerde kaldırılabilir. Yeni iş akışları için alternatif yükleme düğümlerini kullanmayı değerlendirin.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/tr.md)

---
**Source fingerprint (SHA-256):** `820cd9f7a5ccd5a70d2b29906c8deca3632d2ccba84ca51022717e061afb72b3`
