# ByteDanceVideoEnhanceNode

Bu düğüm, ByteDance vCube kullanarak videoları yükseltir ve onarır. Çözünürlüğü 8K'ya kadar artırabilir, sıkıştırma artefaktlarını ve gürültüyü giderir, renk ve keskinliği iyileştirir ve isteğe bağlı olarak daha yüksek kare hızı için kare enterpolasyonu yapar. Video, vCube hizmetine yüklenir, seçilen iyileştirme ön ayarıyla işlenir ve geliştirilmiş bir video dosyası olarak döndürülür.

## Girdiler

### Ortak Girdiler

Bu girdiler her zaman görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | İyileştirilecek video. Kaynak çözünürlük en fazla 2560x1440 (2K) olmalıdır; çıktı boyutu, çözünürlük girdisi tarafından belirlenir. | VIDEO | Evet | En fazla 2560x1440 (2K) |
| `tool_version` | 'standard', 10'dan fazla iyileştirme algoritmasıyla hız ve kaliteyi dengeler. 'professional', sinema kalitesinde restorasyon için 30'dan fazla algoritma kullanır, yaklaşık 3 kat daha uzun sürer ve 10 kat daha pahalıdır. | DYNAMIC_COMBO | Evet | "standard"<br>"professional" |
| `resolution` | Çıktı çözünürlüğü. Kısa kenar seçilen seviyeye ayarlanır ve uzun kenar kaynak en-boy oranını izler. 'source' kaynak boyutunu korur, 'custom' kısa kenarı piksel cinsinden ayarlar. Yaklaşık 2.2:1'den daha geniş veya daha uzun kaynaklar, bir çözünürlük kademesi daha yüksek faturalandırılır. | DYNAMIC_COMBO | Evet | "720p"<br>"1080p"<br>"2k"<br>"4k"<br>"8k"<br>"source"<br>"custom" |
| `fps` | Çıktı kare hızı. Kaynaktan daha yüksek bir hız, AI kare enterpolasyonunu etkinleştirir; daha düşük bir hız kareleri düşürür. 'source', kaynak hızını 120 fps'ye kadar korur. 30 fps'nin üzerindeki hızlar 2 kat, 60 fps'nin üzerindekiler 4 kat maliyetlidir. (varsayılan: "source") | COMBO | Evet | "source" (varsayılan)<br>120 fps'ye kadar sayısal kare hızları |
| `bitrate_level` | Teslim edilen dosyanın hedef bit hızı; çıktı çözünürlüğüne ve kare hızına göre ölçeklenir. (varsayılan: "medium") | COMBO | Evet | "low"<br>"medium"<br>"high" |

### Standart Girdiler

`tool_version` "standard" olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `scene` | İçeriğe göre ayarlanmış ön ayar: 'aigc' AI tarafından üretilen görüntüler için, 'common' genel video için, 'ugc' sıkıştırılmış telefon klipleri için, 'short_series' yüz içeren dramalar için, 'old_film' çizilmiş veya titreyen arşiv görüntüleri için. (varsayılan: "aigc") | COMBO | Evet | "aigc"<br>"common"<br>"ugc"<br>"short_series"<br>"old_film" |
| `enhance_style` | 'hd' daha keskin bir iyileştirme uygular; 'natural', daha yumuşak ve daha az keskinleştirilmiş bir görünüm için gücü azaltır. (varsayılan: "hd") | COMBO | Evet | "hd"<br>"natural" |

### Profesyonel Girdiler

`tool_version` "professional" olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `enhance_style` | 'hd' daha keskin bir iyileştirme uygular; 'natural', daha yumuşak ve daha az keskinleştirilmiş bir görünüm için gücü azaltır. (varsayılan: "hd") | COMBO | Evet | "hd"<br>"natural" |

### Özel Çözünürlük Girdileri

`resolution` "custom" olarak ayarlandığında gösterilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `short_side` | Çıktının piksel cinsinden kısa kenarı; uzun kenar kaynak en-boy oranını izler. (varsayılan: 1080) | INT | Evet | Varsayılan 1080; vCube minimum ve maksimum kısa kenar sınırlarıyla sınırlıdır |

### Notlar

- Kaynak video en fazla 2560x1440 (2K) olmalıdır. Bundan büyük videolar reddedilir ve iyileştirmeden önce küçültülmelidir.
- Kaynak video süresi, vCube hizmeti tarafından desteklenen maksimum süreyle sınırlıdır.
- `tool_version` "standard" olduğunda hem `scene` hem de `enhance_style` kullanılabilir. "professional" olduğunda yalnızca `enhance_style` kullanılabilir.
- `resolution` "custom" olduğunda `short_side` değeri zorunludur. Çözünürlük ön ayarları ve "source" `short_side` kullanmaz.
- `resolution` "source" olduğunda çıktı, kaynak çözünürlüğünü korur.
- `fps` "source" olduğunda çıktı kare hızı, kaynak kare hızıyla 120 fps'ye kadar eşleşir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | İyileştirilmiş video; istenen çözünürlük ve kare hızında yükseltilmiş ve onarılmıştır. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/tr.md)

---
**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`
