# BriaEraseByText

Bu düğüm, Bria kullanarak düz metinle tanımlanan bir nesneyi görüntüden kaldırır. Bria tüm kareyi yaklaşık 1 megapiksel olarak yeniden işler, bu nedenle sonuç girdiyle piksel düzeyinde hizalı değildir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Adlandırılan nesnenin kaldırılacağı görüntü. | IMAGE | Evet | - |
| `object_name` | Kaldırılacak nesnenin adı, örneğin 'the lamp'. Birden fazla nesne aynı anda adlandırılabilir, örneğin 'the phone and the pencils'. Resimde olmayan bir şeyin adlandırılması yine de yeniden işlenmiş bir görüntü döndürür ve faturalandırılır. En az 1 karakter uzunluğunda olmalıdır (varsayılan: boş). | STRING | Evet | - |
| `moderasyon` | Moderasyon ayarları. İsteğe bağlı moderasyon denetimlerinin gösterilip gösterilmeyeceğini seçer. | DYNAMIC_COMBO | Evet | `"false"`<br>`"true"` |

### Moderasyon Girdileri

Bu parametreler `moderation` `"true"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Girdi görüntüsünde içerik moderasyonunu etkinleştirir (varsayılan: false). | BOOLEAN | Hayır | true<br>false |
| `visual_output_moderation` | Oluşturulan çıktı görüntüsünde içerik moderasyonunu etkinleştirir (varsayılan: false). | BOOLEAN | Hayır | true<br>false |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Adlandırılan nesnenin kaldırıldığı yeniden işlenmiş görüntü. | IMAGE |
| `structured_prompt` | Düzenlenen görüntünün yapılandırılmış açıklaması; Bria FIBO Image Edit ile sonraki bir düzenleme için. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseByText/tr.md)

---
**Source fingerprint (SHA-256):** `51ac362bea731251c99905172c41cdebb5165e7564c508f13aa43cf9072964ef`
