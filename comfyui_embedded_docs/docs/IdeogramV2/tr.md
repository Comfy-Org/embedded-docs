Ideogram V2 düğümü, Ideogram V2 yapay zeka modelini kullanarak görseller oluşturur. Bir API hizmeti aracılığıyla görseller oluşturmak için metin istemleri ve çeşitli oluşturma ayarlarını alır. Düğüm, çıktı görsellerini özelleştirmek için farklı en-boy oranlarını, çözünürlükleri ve stil seçeneklerini destekler.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Görsel oluşturma için istem (varsayılan: boş dize) | STRING | Evet | - |
| `turbo` | Turbo modunun kullanılıp kullanılmayacağı (daha hızlı oluşturma, potansiyel olarak daha düşük kalite) (varsayılan: False) | BOOLEAN | Hayır | - |
| `en_boy_oranı` | Görsel oluşturma için en-boy oranı. Çözünürlük AUTO olarak ayarlanmamışsa yok sayılır. (varsayılan: "1:1") | COMBO | Hayır | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" |
| `çözünürlük` | Görsel oluşturma için çözünürlük. AUTO olarak ayarlanmamışsa, bu ayar aspect_ratio ayarını geçersiz kılar. (varsayılan: "Auto") | COMBO | Hayır | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `sihirli_istem_seçeneği` | MagicPrompt'un oluşturmada kullanılıp kullanılmayacağını belirler (varsayılan: "AUTO") | COMBO | Hayır | "AUTO"<br>"ON"<br>"OFF" |
| `tohum` | Oluşturma için rastgele tohum (varsayılan: 0) | INT | Hayır | 0-2147483647 |
| `stil_türü` | Oluşturma için stil türü (yalnızca V2) (varsayılan: "NONE") | COMBO | Hayır | "AUTO"<br>"GENERAL"<br>"REALISTIC"<br>"DESIGN"<br>"RENDER_3D"<br>"ANIME" |
| `negatif_istem` | Görselden çıkarılacak öğelerin açıklaması (varsayılan: boş dize) | STRING | Hayır | - |
| `görüntü_sayısı` | Oluşturulacak görsel sayısı (varsayılan: 1) | INT | Hayır | 1-8 |

**Not:** `resolution` "Auto" olarak ayarlanmadığında, `aspect_ratio` ayarını geçersiz kılar. `num_images` parametresinin oluşturma başına maksimum 8 görsel sınırı vardır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Ideogram V2 modelinden oluşturulan görsel(ler) | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/tr.md)

---
**Source fingerprint (SHA-256):** `c0ba21cb62ad75212c960e2bf6730a39c6479c7389a58c50968c66cc8964f5e3`
