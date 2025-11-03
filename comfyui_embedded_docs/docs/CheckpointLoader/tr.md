> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/tr.md)

CheckpointLoader düğümü, önceden eğitilmiş bir model kontrol noktasını ve yapılandırma dosyasını yükler. Bir yapılandırma dosyası ve bir kontrol noktası dosyasını girdi olarak alır ve iş akışında kullanılmak üzere yüklenen ana model, CLIP modeli ve VAE modeli bileşenlerini döndürür.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `yapılandırma_adı` | STRING | COMBO | - | Mevcut yapılandırma dosyaları | Model mimarisini ve ayarlarını tanımlayan yapılandırma dosyası |
| `ckpt_adı` | STRING | COMBO | - | Mevcut kontrol noktası dosyaları | Eğitilmiş model ağırlıklarını ve parametrelerini içeren kontrol noktası dosyası |

**Not:** Bu düğümün çalışması için hem bir yapılandırma dosyasının hem de bir kontrol noktası dosyasının seçilmesi gerekmektedir. Yapılandırma dosyası, yüklenen kontrol noktası dosyasının mimarisiyle eşleşmelidir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `MODEL` | MODEL | Çıkarım için hazır yüklenmiş ana model bileşeni |
| `CLIP` | CLIP | Metin kodlama için yüklenmiş CLIP modeli bileşeni |
| `VAE` | VAE | Görüntü kodlama ve kod çözme için yüklenmiş VAE modeli bileşeni |

**Önemli Not:** Bu düğüm kullanımdan kaldırılmış (deprecated) olarak işaretlenmiştir ve gelecek sürümlerde kaldırılabilir. Yeni iş akışları için alternatif yükleme düğümlerini kullanmayı düşünün.