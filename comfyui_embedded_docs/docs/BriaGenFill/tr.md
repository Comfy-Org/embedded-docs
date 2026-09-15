# Bria Üretken Doldurma

Bu düğüm, Bria kullanarak bir görüntünün maskelenmiş bölgesi içinde nesneler veya manzaralar oluşturur. Görüntüyü ve maskeyi yükler, istemi Bria üretken doldurma hizmetine gönderir, işlemin tamamlanmasını bekler ve düzenlenmiş görüntüyü döndürür. Bu ücretli bir API işlemidir (istek başına 0,0429 ABD doları).

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Düzenlenecek giriş görüntüsü. | IMAGE | Evet | - |
| `mask` | Beyaz alanlar oluşturulan içerikle doldurulur, siyah alanlar korunur. Maske gönderilmeden önce ikili hale getirilir, bu nedenle kısmen boyanmış alanlar beyaz sayılır. Görüntüyle aynı en-boy oranına sahip olmalıdır. | MASK | Evet | - |
| `prompt` | Maskelenmiş bölge içinde ne oluşturulacağının açıklaması. En az 1 karakter içermelidir. (varsayılan: "") | STRING | Evet | - |
| `negative_prompt` | Oluşturulan sonuçta kaçınılacak içeriği açıklayan bir istem. Boş bırakılırsa API'ye gönderilmez. (varsayılan: "") | STRING | Evet | - |
| `refine_prompt` | Daha iyi sonuçlar için istemi otomatik olarak ayarlar; istemi tam olarak yazıldığı gibi kullanmak için devre dışı bırakın. (varsayılan: true) | BOOLEAN | Evet | true<br>false |
| `seed` | Oluşturma işlemi için tohum. (varsayılan: 42) | INT | Evet | 1 - 2147483647 |
| `moderation` | Moderasyon ayarları. "true" olarak ayarlandığında aşağıdaki moderasyon seçenekleri uygulanır. (varsayılan: "false") | DYNAMIC_COMBO | Evet | "false"<br>"true" |

### Moderasyon Girdileri (`moderation` = "true" olduğunda)

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | İsteme içerik moderasyonu uygular. (varsayılan: false) | BOOLEAN | Hayır | true<br>false |
| `visual_input_moderation` | Giriş görüntüsüne içerik moderasyonu uygular. (varsayılan: false) | BOOLEAN | Hayır | true<br>false |
| `visual_output_moderation` | Çıktı görüntüsüne içerik moderasyonu uygular. (varsayılan: false) | BOOLEAN | Hayır | true<br>false |

**Not:** `prompt` boş olmamalıdır. `mask`, `image` ile aynı en-boy oranına sahip olmalıdır. Maske %50 opaklıkta ikili hale getirilir, bu nedenle yarıdan daha az opaklıkta boyanmış alanlar yok sayılır; ikili hale getirmeden sonra maskede beyaz alan yoksa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Maskelenmiş bölgenin oluşturulan içerikle doldurulduğu sonuç görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/tr.md)

---
**Source fingerprint (SHA-256):** `b23e29d4457f859181d68eaeb4b0238de28f4b18932d68438fa2954739cdc66a`
