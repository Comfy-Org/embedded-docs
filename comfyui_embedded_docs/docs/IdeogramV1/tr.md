> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/tr.md)

İşte ComfyUI IdeogramV1 düğüm belgesinin Türkçe çevirisi:

IdeogramV1 düğümü, bir API aracılığıyla Ideogram V1 modelini kullanarak görseller oluşturur. Metin istemleri ve çeşitli oluşturma ayarlarını alarak, girdinize bağlı olarak bir veya daha fazla görsel oluşturur. Düğüm, çıktıyı özelleştirmek için farklı en-boy oranlarını ve oluşturma modlarını destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `prompt` | STRING | Evet | - | Görsel oluşturma için istem (varsayılan: boş) |
| `turbo` | BOOLEAN | Evet | - | Turbo modunun kullanılıp kullanılmayacağı (daha hızlı oluşturma, potansiyel olarak daha düşük kalite) (varsayılan: False) |
| `aspect_ratio` | COMBO | Hayır | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | Görsel oluşturma için en-boy oranı (varsayılan: "1:1") |
| `magic_prompt_option` | COMBO | Hayır | "AUTO"<br>"ON"<br>"OFF" | Oluşturmada MagicPrompt kullanılıp kullanılmayacağını belirler (varsayılan: "AUTO") |
| `seed` | INT | Hayır | 0-2147483647 | Oluşturma için rastgele tohum değeri (varsayılan: 0) |
| `negative_prompt` | STRING | Hayır | - | Görselden çıkarılacak öğelerin açıklaması (varsayılan: boş) |
| `num_images` | INT | Hayır | 1-8 | Oluşturulacak görsel sayısı (varsayılan: 1) |

**Not:** `num_images` parametresinin oluşturma isteği başına maksimum 8 görsel sınırı vardır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | IMAGE | Ideogram V1 modelinden oluşturulan görsel(ler) |

---
**Source fingerprint (SHA-256):** `7e453cd54b5db48588ed899b0754e0d06fdcfbaed248d13fb74b7049f0f25b8f`
