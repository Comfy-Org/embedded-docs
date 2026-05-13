> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyTxt2VideoNode/tr.md)

Moonvalley Marey Metinden Videoya düğümü, Moonvalley API'sini kullanarak metin açıklamalarından video içeriği oluşturur. Bir metin istemi alır ve bunu çözünürlük, kalite ve stil için özelleştirilebilir ayarlarla bir videoya dönüştürür. Düğüm, oluşturma isteğinin gönderilmesinden nihai video çıktısının indirilmesine kadar tüm süreci yönetir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Evet | - | Oluşturulacak video içeriğinin metin açıklaması |
| `negative_prompt` | STRING | Hayır | - | Olumsuz istem metni (varsayılan: sentetik, sahne kesmesi, yapaylıklar, gürültü vb. gibi hariç tutulan öğelerin kapsamlı listesi) |
| `resolution` | STRING | Hayır | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)"<br>"21:9 (2560 x 1080)" | Çıktı videosunun çözünürlüğü (varsayılan: "16:9 (1920 x 1080)") |
| `prompt_adherence` | FLOAT | Hayır | 1.0-20.0 | Oluşturma kontrolü için yönlendirme ölçeği (varsayılan: 4.0) |
| `seed` | INT | Hayır | 0-4294967295 | Rastgele tohum değeri (varsayılan: 9) |
| `steps` | INT | Hayır | 1-100 | Çıkarım adımları (varsayılan: 33) |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `video` | VIDEO | Metin istemine dayalı olarak oluşturulan video çıktısı |

---
**Source fingerprint (SHA-256):** `3654043567d7aca3af741d706ee07a8d2e28dbeb4b5b8755514b790aa7c1bd41`
