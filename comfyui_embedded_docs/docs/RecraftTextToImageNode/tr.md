# Recraft Metinden Görüntüye

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Görüntü üretimi için prompt. (varsayılan: "") | STRING | Evet | - |
| `size` | Üretilen görüntünün boyutu. (varsayılan: "1024x1024") | COMBO | Evet | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `n` | Üretilecek görüntü sayısı. (varsayılan: 1) | INT | Evet | 1-6 |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0-18446744073709551615 |
| `recraft_style` | Görüntü üretimi için isteğe bağlı stil seçimi. Sağlanmadığında, gerçekçi görüntü stiline varsayılan olarak ayarlanır. | RECRAFT_STYLE | Hayır | Birden fazla seçenek mevcuttur |
| `negative_prompt` | Görüntüde istenmeyen öğelerin isteğe bağlı metin açıklaması. (varsayılan: "") | STRING | Hayır | - |
| `recraft_controls` | Recraft Controls düğümü aracılığıyla üretim üzerinde isteğe bağlı ek kontroller. | RECRAFT_CONTROLS | Hayır | Birden fazla seçenek mevcuttur |

**Not:** `seed` parametresi yalnızca düğümün ne zaman yeniden çalışacağını kontrol eder, görüntü üretimini deterministik yapmaz. Aynı tohum değeriyle bile gerçek çıktı görüntüleri değişiklik gösterecektir.

**Not:** `prompt` parametresi 1 ile 1000 karakter arasında olmalıdır.

**Not:** Infinite Style Library'den bir `style_id` kullanıyorsanız, bunun Vector sanat stili olmadığından emin olun; aksi takdirde görüntü yerine SVG verisi döner ve hataya neden olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Toplu tensör çıktısı olarak üretilen görüntü(ler). Birden fazla görüntü üretildiğinde (n > 1), toplu iş boyutu boyunca birleştirilirler. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `d75b7dd2d8cee70c3bc1d2c64fb07ce814a3672619e8647f4c4c2cdc2635945c`
