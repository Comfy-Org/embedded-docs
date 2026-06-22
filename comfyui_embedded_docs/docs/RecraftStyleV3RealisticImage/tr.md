# Recraft Stili - Gerçekçi Görüntü

Bu düğüm, Recraft API'sini kullanarak gerçekçi görseller oluşturmak için bir stil yapılandırması oluşturur. `realistic_image` stilini seçer ve çıktı görünümünü ince ayarlamak için isteğe bağlı bir alt stil belirlemenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `alt_stil` | realistic_image stiline uygulanacak belirli alt stildir. "None" olarak ayarlanırsa, hiçbir alt stil uygulanmaz. | STRING | Evet | Birden çok seçenek mevcuttur (Recraft API tarafından belirlenir) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `recraft_style` | `realistic_image` stilini ve seçilen alt stil ayarlarını içeren bir Recraft stil yapılandırma nesnesidir. Bu çıktı, stil girişini kabul eden diğer Recraft düğümlerine bağlanabilir. | STYLEV3 |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/tr.md)

---
**Source fingerprint (SHA-256):** `23eafae0a00f1806052a6583db791a5c1fd418ea940ed6463824dffe843ed0d7`
