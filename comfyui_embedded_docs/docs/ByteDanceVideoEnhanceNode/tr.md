# ByteDance vCube Video Geliştirme

Bu düğüm, ByteDance vCube kullanarak videoları üst ölçeklendirir ve geri yükler. Çözünürlüğü 8K'ya kadar artırabilir, sıkıştırma artefaktlarını ve gürültüyü kaldırabilir, renk ve keskinliği iyileştirebilir ve isteğe bağlı olarak daha yüksek kare hızı için kare interpolasyonu yapabilir. Video vCube hizmetine yüklenir, seçilen iyileştirme ön ayarıyla işlenir ve iyileştirilmiş bir video dosyası olarak döndürülür.

## Girdiler

### Ortak Girdiler

Bu girdiler her zaman görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | İyileştirilecek video. Kaynak çözünürlük en fazla 2560x1440 (2K) olmalıdır; çıktı boyutu `resolution` girdisiyle ayarlanır. | VIDEO | Evet | En fazla 2560x1440 (2K) |
| `tool_version` | 'standard' 10'dan fazla iyileştirme algoritmasıyla hız ve kaliteyi dengeler. 'professional' sinema düzeyinde restorasyon için 30'dan fazla algoritma kullanır, yaklaşık 3 kat daha uzun sürer ve 10 kat daha fazla maliyetlidir. | DYNAMIC_COMBO | Evet | "standard"<br>"professional" |
| `resolution` | Çıktı çözünürlüğü. Kısa kenar seçilen düzeye ayarlanır ve uzun kenar kaynak en-boy oranını izler. 'source' kaynak boyutu korur, 'custom' kısa kenarı piksel cinsinden ayarlar. Yaklaşık 2.2:1'den daha geniş veya daha yüksek kaynaklar bir çözünürlük kademesi daha yüksek faturalandırılır. | DYNAMIC_COMBO | Evet | "720p"<br>"1080p"<br>"2k"<br>"4k"<br>"8k"<br>"source"<br>"custom" |
| `fps` | Çıktı kare hızı. Kaynaktan daha yüksek bir hız AI kare interpolasyonunu etkinleştirir; daha düşük bir hız kareleri düşürür. 'source' kaynak hızı korur, 120 fps'ye kadar. 30 fps üzerindeki hızlar 2 kat, 60 fps üzerindekiler 4 kat maliyetlidir. (varsayılan: "source") | COMBO | Evet | "source" (varsayılan)<br>120 fps'ye kadar sayısal kare hızları |
| `bitrate_level` | Teslim edilen dosyanın hedef bit hızı, çıktı çözünürlüğü ve kare hızına göre ölçeklenir. (varsayılan: "medium") | COMBO | Evet | "low"<br>"medium"<br>"high" |

### Standart Girdiler

`tool_version` "standard" olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `scene` | İçeriğe göre ayarlanmış ön ayar: AI tarafından oluşturulan görüntüler için 'aigc', genel video için 'common', sıkıştırılmış telefon klipleri için 'ugc', yüz içeren dramalar için 'short_series', çizik veya titreyen arşiv görüntüleri için 'old_film'. (varsayılan: "aigc") | COMBO | Evet | "aigc"<br>"common"<br>"ugc"<br>"short_series"<br>"old_film" |
| `enhance_style` | 'hd' daha keskin bir iyileştirme uygular; 'natural' daha yumuşak, daha az keskinleştirilmiş bir görünüm için gücü azaltır. (varsayılan: "hd") | COMBO | Evet | "hd"<br>"natural" |

### Profesyonel Girdiler

`tool_version` "professional" olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `enhance_style` | 'hd' daha keskin bir iyileştirme uygular; 'natural' daha yumuşak, daha az keskinleştirilmiş bir görünüm için gücü azaltır. (varsayılan: "hd") | COMBO | Evet | "hd"<br>"natural" |

### Özel Çözünürlük Girdileri

`resolution` "custom" olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `short_side` | Çıktının piksel cinsinden kısa kenarı; uzun kenar kaynak en-boy oranını izler. (varsayılan: 1080) | INT | Evet | Varsayılan 1080; vCube minimum ve maksimum kısa kenar sınırlarıyla sınırlıdır |

### Notlar

- Kaynak video en fazla 2560x1440 (2K) olmalıdır. Bundan daha büyük videolar reddedilir ve iyileştirmeden önce küçültülmelidir.
- Kaynak video süresi, vCube hizmeti tarafından desteklenen maksimum süreyle sınırlıdır.
- `tool_version` "standard" olduğunda hem `scene` hem de `enhance_style` kullanılabilir. "professional" olduğunda yalnızca `enhance_style` kullanılabilir.
- `resolution` "custom" olduğunda `short_side` değeri gereklidir. Çözünürlük ön ayarları ve "source", `short_side` kullanmaz.
- `resolution` "source" olduğunda ve kaynak kısa kenar en az minimum kısa kenar sınırındaysa, çıktı kaynak çözünürlüğü korur.
- `fps` "source" olduğunda, çıktı kare hızı 120 fps'ye kadar kaynak kare hızıyla eşleşir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | İstenen çözünürlük ve kare hızında üst ölçeklenmiş ve geri yüklenmiş, iyileştirilmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/tr.md)

---
**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`
