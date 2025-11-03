> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/tr.md)

Ideogram V2 düğümü, Ideogram V2 AI modelini kullanarak görüntüler oluşturur. Bir API servisi aracılığıyla metin prompt'ları ve çeşitli oluşturma ayarlarını alarak görüntüler oluşturur. Düğüm, çıktı görüntülerini özelleştirmek için farklı en-boy oranları, çözünürlükler ve stil seçeneklerini destekler.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Görüntü oluşturma için prompt (varsayılan: boş string) |
| `turbo` | BOOLEAN | Hayır | - | Turbo modunun kullanılıp kullanılmayacağı (daha hızlı oluşturma, potansiyel olarak daha düşük kalite) (varsayılan: False) |
| `en_boy_oranı` | COMBO | Hayır | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | Görüntü oluşturma için en-boy oranı. Çözünürlük AUTO olarak ayarlanmamışsa dikkate alınmaz. (varsayılan: "1:1") |
| `çözünürlük` | COMBO | Hayır | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | Görüntü oluşturma için çözünürlük. AUTO olarak ayarlanmazsa, bu ayar aspect_ratio ayarını geçersiz kılar. (varsayılan: "Auto") |
| `sihirli_istem_seçeneği` | COMBO | Hayır | "AUTO"<br>"ON"<br>"OFF" | Oluşturmada MagicPrompt'un kullanılıp kullanılmayacağını belirler (varsayılan: "AUTO") |
| `tohum` | INT | Hayır | 0-2147483647 | Oluşturma için rastgele seed değeri (varsayılan: 0) |
| `stil_türü` | COMBO | Hayır | "AUTO"<br>"GENERAL"<br>"REALISTIC"<br>"DESIGN"<br>"RENDER_3D"<br>"ANIME" | Oluşturma için stil türü (sadece V2) (varsayılan: "NONE") |
| `negatif_istem` | STRING | Hayır | - | Görüntüde nelerin hariç tutulacağının açıklaması (varsayılan: boş string) |
| `görüntü_sayısı` | INT | Hayır | 1-8 | Oluşturulacak görüntü sayısı (varsayılan: 1) |

**Not:** `resolution` "Auto" olarak ayarlanmadığında, `aspect_ratio` ayarını geçersiz kılar. `num_images` parametresinin oluşturma başına maksimum 8 görüntü limiti vardır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | IMAGE | Ideogram V2 modelinden oluşturulan görüntü(ler) |