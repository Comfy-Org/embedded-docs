# Recraft V4 Stil Oluştur

Bu düğüm, 1 ila 10 referans görüntüsünden yeniden kullanılabilir bir Recraft V4 stili oluşturur. Döndürülen stil kimliği, aynı çıktı türündeki her Recraft V4 ve V4.1 modeliyle çalışır ve sonraki görüntü oluşturma adımlarında yeniden kullanılabilir. Tüm referans görüntülerinin toplam boyutu 10 MB ile sınırlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Stilin oluşturulduğu çıktı türü: raster görüntüler için `recraftv4_styles`, SVG için `recraftv4_styles_vector`. | COMBO | Evet | "recraftv4_styles"<br>"recraftv4_styles_vector" |
| `images` | Stili tanımlayan referans görüntüleri. Benzer referanslar eşleşmeyi keskinleştirir, çeşitli referanslar ise onu genişletir. Genişletilebilir yuva: 1 ila 10 görüntü bağlayın (`image_1` ile `image_10` arası). | IMAGE | Evet | 1 ila 10 görüntü |

### Notlar

- En az bir referans görüntüsü zorunludur; hiçbiri sağlanmazsa düğüm bir hata verir.
- En fazla 10 referans görüntüsüne izin verilir.
- Tüm referans görüntülerinin toplam kodlanmış boyutu 10 MB'ı aşmamalıdır; sınır aşılırsa düğüm bir hata verir.
- Her referans görüntüsü, Recraft API'sine gönderilmeden önce en fazla 2048×2048 piksel boyutuna küçültülür ve WebP olarak kodlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `style_id` | Oluşturulan stilin benzersiz kimliği; aynı çıktı türündeki her Recraft V4 ve V4.1 modeliyle kullanılabilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4CreateStyleNode/tr.md)

---
**Source fingerprint (SHA-256):** `63b31ff08d5cfe7c0d4de6987f2ee5a34bd491237ed0fb4c93c225e33b7cede3`
