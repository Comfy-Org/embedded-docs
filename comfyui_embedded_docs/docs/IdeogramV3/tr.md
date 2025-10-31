> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV3/tr.md)

Ideogram V3 düğümü, Ideogram V3 modelini kullanarak görüntüler oluşturur. Hem metin istemlerinden düzenli görüntü oluşturmayı hem de bir görüntü ve maske sağlandığında görüntü düzenlemeyi destekler. Düğüm, en-boy oranı, çözünürlük, oluşturma hızı ve isteğe bağlı karakter referans görüntüleri için çeşitli kontroller sunar.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Görüntü oluşturma veya düzenleme için istem (varsayılan: boş) |
| `görüntü` | IMAGE | Hayır | - | Görüntü düzenleme için isteğe bağlı referans görüntüsü |
| `maske` | MASK | Hayır | - | İç boyama için isteğe bağlı maske (beyaz alanlar değiştirilecektir) |
| `en_boy_oranı` | COMBO | Hayır | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | Görüntü oluşturma için en-boy oranı. Çözünürlük Otomatik olarak ayarlanmamışsa dikkate alınmaz (varsayılan: "1:1") |
| `çözünürlük` | COMBO | Hayır | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | Görüntü oluşturma için çözünürlük. Otomatik olarak ayarlanmazsa, bu ayar `en_boy_oranı` ayarını geçersiz kılar (varsayılan: "Auto") |
| `sihirli_istem_seçeneği` | COMBO | Hayır | "AUTO"<br>"ON"<br>"OFF" | Oluşturmada MagicPrompt'un kullanılıp kullanılmayacağını belirler (varsayılan: "AUTO") |
| `tohum` | INT | Hayır | 0-2147483647 | Oluşturma için rastgele tohum (varsayılan: 0) |
| `görüntü_sayısı` | INT | Hayır | 1-8 | Oluşturulacak görüntü sayısı (varsayılan: 1) |
| `oluşturma_hızı` | COMBO | Hayır | "DEFAULT"<br>"TURBO"<br>"QUALITY" | Oluşturma hızı ve kalitesi arasındaki dengeyi kontrol eder (varsayılan: "DEFAULT") |
| `character_image` | IMAGE | Hayır | - | Karakter referansı olarak kullanılacak görüntü |
| `character_mask` | MASK | Hayır | - | Karakter referans görüntüsü için isteğe bağlı maske |

**Parametre Kısıtlamaları:**

- Hem `image` hem de `mask` sağlandığında, düğüm düzenleme moduna geçer
- Yalnızca `image` veya `mask`'tan biri sağlanırsa, bir hata oluşur
- `character_mask`, `character_image`'ın mevcut olmasını gerektirir
- `aspect_ratio` parametresi, `resolution` "Auto" olarak ayarlanmadığında dikkate alınmaz
- Maskedeki beyaz alanlar iç boyama sırasında değiştirilecektir
- Karakter maskesi ve karakter görüntüsü aynı boyutta olmalıdır

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Oluşturulan veya düzenlenen görüntü(ler) |