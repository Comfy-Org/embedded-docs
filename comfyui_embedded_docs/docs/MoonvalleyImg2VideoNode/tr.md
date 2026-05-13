> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyImg2VideoNode/tr.md)

Moonvalley Marey Görüntüden Videoya düğümü, Moonvalley API'sini kullanarak bir referans görüntüyü videoya dönüştürür. Bir giriş görüntüsü ve metin istemi alarak belirtilen çözünürlük, kalite ayarları ve yaratıcı kontrollerle video oluşturur. Düğüm, görüntü yüklemeden video oluşturma ve indirmeye kadar tüm süreci yönetir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `image` | IMAGE | Evet | - | Videoyu oluşturmak için kullanılan referans görüntü |
| `prompt` | STRING | Evet | - | Video oluşturma için metin açıklaması (çok satırlı giriş) |
| `negative_prompt` | STRING | Hayır | - | İstenmeyen öğeleri hariç tutmak için negatif istem metni (varsayılan: kapsamlı negatif istem listesi) |
| `resolution` | COMBO | Hayır | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)" | Çıktı videosunun çözünürlüğü (varsayılan: "16:9 (1920 x 1080)") |
| `prompt_adherence` | FLOAT | Hayır | 1,0 - 20,0 | Oluşturma kontrolü için yönlendirme ölçeği (varsayılan: 4,5, adım: 1,0) |
| `seed` | INT | Hayır | 0 - 4294967295 | Rastgele tohum değeri (varsayılan: 9, oluşturma sonrası kontrol etkin) |
| `steps` | INT | Hayır | 1 - 100 | Gürültü giderme adım sayısı (varsayılan: 33, adım: 1) |

**Kısıtlamalar:**

- Giriş görüntüsünün boyutları 300x300 piksel ile izin verilen maksimum yükseklik/genişlik arasında olmalıdır
- İstem ve negatif istem metin uzunluğu, Moonvalley Marey maksimum istem uzunluğu ile sınırlıdır

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `output` | VIDEO | Oluşturulan video çıktısı |

---
**Source fingerprint (SHA-256):** `674e69a7f106f6f961f10c179008b7bb1147bf0e569c72d207a105f3fab2aaf5`
