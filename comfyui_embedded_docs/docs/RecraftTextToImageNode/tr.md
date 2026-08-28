# Recraft Metinden Görüntüye

İstem ve çözünürlüğe dayalı olarak görüntüleri eşzamanlı (senkron) şekilde oluşturur. Bu düğüm, belirtilen boyutlara ve isteğe bağlı stil ile kontrol parametrelerine sahip metin açıklamalarından görüntüler oluşturmak için Recraft API'sine bağlanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istem` | Görüntü oluşturma için istem. (varsayılan: "") | STRING | Evet | - |
| `boyut` | Oluşturulan görüntünün boyutu. (varsayılan: "1024x1024") | COMBO | Evet | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `n` | Oluşturulacak görüntü sayısı. (varsayılan: 1) | INT | Evet | 1-6 |
| `tohum` | Düğümün yeniden çalışıp çalışmayacağını belirleyen seed değeri; seed değeri ne olursa olsun gerçek sonuçlar deterministik değildir. (varsayılan: 0) | INT | Evet | 0-18446744073709551615 |
| `recraft_stili` | Görüntü oluşturma için isteğe bağlı stil seçimi. Sağlanmadığında varsayılan olarak "realistic_image" stili kullanılır. | RECRAFT_STYLE | Hayır | Birden fazla seçenek mevcuttur |
| `negatif_istem` | Görüntüde istenmeyen öğelere ilişkin isteğe bağlı metin açıklaması. (varsayılan: "") | STRING | Hayır | - |
| `recraft_kontrolleri` | Recraft Controls düğümü aracılığıyla oluşturma üzerinde isteğe bağlı ek kontroller. | RECRAFT_CONTROLS | Hayır | Birden fazla seçenek mevcuttur |

**Not:** `seed` parametresi yalnızca düğümün ne zaman yeniden çalışacağını kontrol eder; görüntü oluşturmayı deterministik hale getirmez. Aynı seed değeriyle bile gerçek çıktı görüntüleri değişiklik gösterecektir.

**Not:** `prompt` parametresinin uzunluğu 1 ile 1000 karakter arasında olmalıdır.

**Not:** Infinite Style Library'den bir `style_id` kullanıyorsanız, bunun Vector art stili olmadığından emin olun; aksi halde görüntü yerine SVG verisi döner ve hataya neden olur.

**Not:** Bu, ücretli bir API düğümüdür. Maliyet, `n` değerine bağlı olarak oluşturulan görüntü başına 0,04 $'dır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Oluşturulan görüntü(ler), toplu (batched) bir tensör çıktısı olarak verilir. Birden fazla görüntü oluşturulduğunda (n > 1), bunlar batch boyutu boyunca birleştirilir. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/tr.md)

---
**Source fingerprint (SHA-256):** `d75b7dd2d8cee70c3bc1d2c64fb07ce814a3672619e8647f4c4c2cdc2635945c`
