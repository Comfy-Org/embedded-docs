> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV3/tr.md)

**Ideogram V3**

Ideogram V3 düğümü, Ideogram V3 modelini kullanarak görseller oluşturur. Hem metin istemlerinden normal görsel oluşturmayı hem de bir görsel ve maske sağlandığında görsel düzenlemeyi destekler. Düğüm, en boy oranı, çözünürlük, oluşturma hızı ve isteğe bağlı karakter referans görselleri için çeşitli kontroller sunar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Görsel oluşturma veya düzenleme için istem (varsayılan: boş) |
| `görüntü` | IMAGE | Hayır | - | Görsel düzenleme için isteğe bağlı referans görseli |
| `maske` | MASK | Hayır | - | İç boyama (inpainting) için isteğe bağlı maske (beyaz alanlar değiştirilecektir) |
| `en_boy_oranı` | COMBO | Hayır | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | Görsel oluşturma için en boy oranı. Çözünürlük Otomatik olarak ayarlanmamışsa yok sayılır (varsayılan: "1:1") |
| `çözünürlük` | COMBO | Hayır | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | Görsel oluşturma için çözünürlük. Otomatik olarak ayarlanmamışsa, bu değer aspect_ratio ayarını geçersiz kılar (varsayılan: "Auto") |
| `sihirli_istem_seçeneği` | COMBO | Hayır | "AUTO"<br>"ON"<br>"OFF" | Oluşturmada MagicPrompt kullanılıp kullanılmayacağını belirler (varsayılan: "AUTO") |
| `tohum` | INT | Hayır | 0-2147483647 | Oluşturma için rastgele tohum (varsayılan: 0) |
| `görüntü_sayısı` | INT | Hayır | 1-8 | Oluşturulacak görsel sayısı (varsayılan: 1) |
| `oluşturma_hızı` | COMBO | Hayır | "DEFAULT"<br>"TURBO"<br>"QUALITY" | Oluşturma hızı ve kalitesi arasındaki dengeyi kontrol eder (varsayılan: "DEFAULT") |
| `character_image` | IMAGE | Hayır | - | Karakter referansı olarak kullanılacak görsel |
| `character_mask` | MASK | Hayır | - | Karakter referans görseli için isteğe bağlı maske |

**Parametre Kısıtlamaları:**

- Hem `image` hem de `mask` sağlandığında, düğüm düzenleme moduna geçer
- `image` veya `mask`'ten yalnızca biri sağlanırsa bir hata oluşur
- `character_mask`'in kullanılabilmesi için `character_image`'in mevcut olması gerekir
- `resolution` "Auto" olarak ayarlanmadığında `aspect_ratio` parametresi yok sayılır
- Maske içindeki beyaz alanlar iç boyama (inpainting) sırasında değiştirilecektir
- Karakter maskesi ve karakter görseli aynı boyutta olmalıdır

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Oluşturulan veya düzenlenen görsel(ler) |

---
**Source fingerprint (SHA-256):** `0d0058cc8483c453100d8d9dfcb9a31ae5e686f38ced77ed7e472cd083c3464b`
