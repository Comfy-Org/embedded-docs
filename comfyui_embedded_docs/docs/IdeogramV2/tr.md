> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/tr.md)

Ideogram V2 düğümü, Ideogram V2 yapay zeka modelini kullanarak görseller oluşturur. Bir API hizmeti aracılığıyla görseller oluşturmak için metin istemleri ve çeşitli oluşturma ayarlarını alır. Düğüm, çıktı görsellerini özelleştirmek için farklı en-boy oranlarını, çözünürlükleri ve stil seçeneklerini destekler.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Görsel oluşturma için istem (varsayılan: boş dize) |
| `turbo` | BOOLEAN | Hayır | - | Turbo modunun kullanılıp kullanılmayacağı (daha hızlı oluşturma, potansiyel olarak daha düşük kalite) (varsayılan: False) |
| `en_boy_oranı` | COMBO | Hayır | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | Görsel oluşturma için en-boy oranı. Çözünürlük AUTO olarak ayarlanmamışsa yok sayılır. (varsayılan: "1:1") |
| `çözünürlük` | COMBO | Hayır | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | Görsel oluşturma için çözünürlük. AUTO olarak ayarlanmamışsa, bu ayar aspect_ratio ayarını geçersiz kılar. (varsayılan: "Auto") |
| `sihirli_istem_seçeneği` | COMBO | Hayır | "AUTO"<br>"ON"<br>"OFF" | MagicPrompt'un oluşturmada kullanılıp kullanılmayacağını belirler (varsayılan: "AUTO") |
| `tohum` | INT | Hayır | 0-2147483647 | Oluşturma için rastgele tohum (varsayılan: 0) |
| `stil_türü` | COMBO | Hayır | "AUTO"<br>"GENERAL"<br>"REALISTIC"<br>"DESIGN"<br>"RENDER_3D"<br>"ANIME" | Oluşturma için stil türü (yalnızca V2) (varsayılan: "NONE") |
| `negatif_istem` | STRING | Hayır | - | Görselden çıkarılacak öğelerin açıklaması (varsayılan: boş dize) |
| `görüntü_sayısı` | INT | Hayır | 1-8 | Oluşturulacak görsel sayısı (varsayılan: 1) |

**Not:** `resolution` "Auto" olarak ayarlanmadığında, `aspect_ratio` ayarını geçersiz kılar. `num_images` parametresinin oluşturma başına maksimum 8 görsel sınırı vardır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Ideogram V2 modelinden oluşturulan görsel(ler) |

---
**Source fingerprint (SHA-256):** `c0ba21cb62ad75212c960e2bf6730a39c6479c7389a58c50968c66cc8964f5e3`
