# Yapılandırmayla Kontrol Noktası Yükle (ESKİ)

CheckpointLoader düğümü, önceden eğitilmiş bir model checkpoint'ini yapılandırma dosyasıyla birlikte yükler. Girdi olarak bir yapılandırma dosyası ve bir checkpoint dosyası alır ve iş akışında kullanılmak üzere yüklenen model bileşenlerini — ana model, CLIP modeli ve VAE modeli — döndürür. Bu düğüm kullanımdan kaldırılmıştır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `yapılandırma_adı` | Model mimarisini ve ayarlarını tanımlayan yapılandırma dosyası | COMBO | Evet | Mevcut yapılandırma dosyaları |
| `ckpt_adı` | Eğitilmiş model ağırlıklarını ve parametrelerini içeren checkpoint dosyası | COMBO | Evet | Mevcut checkpoint dosyaları |

**Not:** Bu düğüm, hem bir yapılandırma dosyası hem de bir checkpoint dosyası seçilmesini gerektirir. Yapılandırma dosyası, yüklenen checkpoint dosyasının mimarisiyle eşleşmelidir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Çıkarım için hazır yüklenmiş ana model bileşeni | MODEL |
| `CLIP` | Metin kodlama için yüklenmiş CLIP model bileşeni | CLIP |
| `VAE` | Görüntü kodlama ve kod çözme için yüklenmiş VAE model bileşeni | VAE |

**Önemli Not:** Bu düğüm kullanımdan kaldırılmış olarak işaretlenmiştir ve gelecekteki sürümlerde kaldırılabilir. Yeni iş akışları için alternatif yükleme düğümlerini kullanmayı değerlendirin.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/tr.md)

---
**Source fingerprint (SHA-256):** `820cd9f7a5ccd5a70d2b29906c8deca3632d2ccba84ca51022717e061afb72b3`
