> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/tr.md)

İşte belgenin Türkçe çevirisi:

## Genel Bakış

İstem ve çözünürlüğe göre eşzamanlı olarak görseller oluşturur. Bu düğüm, Recraft API'sine bağlanarak metin açıklamalarından, belirtilen boyutlarda ve isteğe bağlı stil ve kontrol parametreleriyle görseller oluşturur.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | - | Görsel oluşturma için istem. (varsayılan: "") |
| `boyut` | COMBO | Evet | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | Oluşturulan görselin boyutu. (varsayılan: "1024x1024") |
| `n` | INT | Evet | 1-6 | Oluşturulacak görsel sayısı. (varsayılan: 1) |
| `tohum` | INT | Evet | 0-18446744073709551615 | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum değeri; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir. (varsayılan: 0) |
| `recraft_stili` | RECRAFT_STYLE | Hayır | Birden çok seçenek mevcut | Görsel oluşturma için isteğe bağlı stil seçimi. Sağlanmadığında varsayılan olarak "realistic_image" stili kullanılır. |
| `negatif_istem` | STRING | Hayır | - | Görselde istenmeyen öğelerin isteğe bağlı metin açıklaması. (varsayılan: "") |
| `recraft_kontrolleri` | RECRAFT_CONTROLS | Hayır | Birden çok seçenek mevcut | Recraft Kontrolleri düğümü aracılığıyla oluşturma üzerinde isteğe bağlı ek kontroller. |

**Not:** `seed` parametresi yalnızca düğümün ne zaman yeniden çalıştırılacağını kontrol eder, görsel oluşturmayı deterministik hale getirmez. Aynı tohum değeriyle bile gerçek çıktı görselleri farklılık gösterecektir.

**Not:** `prompt` parametresi 1 ile 1000 karakter arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Toplu tensör çıktısı olarak oluşturulan görsel(ler). Birden çok görsel oluşturulduğunda (n > 1), toplu boyut boyunca birleştirilirler. |

---
**Source fingerprint (SHA-256):** `28c510ccfad13ddb50700b465af14deaa3c7c1f8597fef048d89094fd24fcd7d`
