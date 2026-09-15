# BriaReplaceObject

Düz metinle açıklanan farklı bir nesneyle bir görüntüdeki nesneyi değiştirir; Bria'nın metin güdümlü görüntü düzenlemesini kullanır. Bria tüm kareyi yaklaşık 1 megapiksel olarak yeniden oluşturur, bu nedenle sonuç girdiyle piksel hizalı değildir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Değiştirilecek nesneyi içeren görüntü. Görüntü yüklenmeden önce alfa kanalı kaldırılır. | IMAGE | Evet | - |
| `talimat` | Neyin neyle değiştirileceği, örneğin "Kırmızı elmayı yeşil bir armutla değiştir". En az 1 karakter uzunluğunda olmalıdır. | STRING | Evet | Çok satırlı metin; varsayılan: "" (boş) |
| `seed` | Bria burada seed kabul etmez ve düzenlemeyi her çağrıda yeniden yorumlar; bu nedenle tekrarlanan çalıştırmalar farklılık gösterebilir. Değer hiçbir zaman gönderilmez: yalnızca bu düğümün önbellek anahtarını değiştirir; böylece aksi halde aynı olan bir grafik, önbelleğe alınmış sonucu döndürmek yerine düzenlemeyi yeniden çalıştırır. | INT | Evet | 0 ile 2147483647 arası, adım 1; varsayılan: 42; oluşturma sonrası denetim etkin |

### Moderasyon Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `moderasyon` | Moderasyon ayarları. "true" seçildiğinde, aksi halde gösterilmeyen aşağıdaki moderasyon alt seçenekleri görünür. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |
| `visual_input_moderation` | Girdi görüntüsünün moderasyonunu etkinleştirir. Yalnızca `moderation` "true" olarak ayarlandığında kullanılabilir. | BOOLEAN | Hayır | `true` / `false`; varsayılan: false |
| `visual_output_moderation` | Oluşturulan çıktı görüntüsünün moderasyonunu etkinleştirir. Yalnızca `moderation` "true" olarak ayarlandığında kullanılabilir. | BOOLEAN | Hayır | `true` / `false`; varsayılan: false |

Not: `instruction`, istek gönderilmeden önce doğrulanır ve en az 1 karakter içermelidir. `seed` değeri Bria'ya iletilmez; yalnızca düğümün düzenlemeyi yeniden çalıştırıp çalıştırmayacağını veya önbelleğe alınmış bir sonucu döndürüp döndürmeyeceğini etkiler.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `image` | Açıklanan nesne değişikliği uygulanmış düzenlenmiş görüntü. | IMAGE |
| `structured_prompt` | Bria FIBO Image Edit ile sonraki bir düzenleme için düzenlenmiş görüntünün yapılandırılmış açıklaması. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReplaceObject/tr.md)

---
**Source fingerprint (SHA-256):** `75a45d5c0d6cde96a1e961db627edc1a59c07cc37b974402745cefc62864cc26`
