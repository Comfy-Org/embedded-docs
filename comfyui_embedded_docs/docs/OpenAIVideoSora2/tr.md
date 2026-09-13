# OpenAI Sora - Video

OpenAIVideoSora2 düğümü, OpenAI'nin Sora modelleriyle video üretir. Bir metin istemi ile isteğe bağlı tek bir referans görseli alır, isteği OpenAI'ye gönderir, üretimin tamamlanmasını bekler ve ortaya çıkan videoyu döndürür. Desteklenen süreler ve çözünürlükler seçilen modele bağlıdır.

**KULLANIMDAN KALDIRMA UYARISI:** OpenAI, Sora v2 API'sini sunmayı Eylül 2026'da durduracaktır. Bu düğüm o zaman ComfyUI'dan kaldırılacaktır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video üretimi için kullanılacak OpenAI Sora modeli (varsayılan: "sora-2") | COMBO | Evet | "sora-2"<br>"sora-2-pro" |
| `komut istemi` | Yönlendirici metin; bir girdi görseli varsa boş olabilir (varsayılan: boş dize) | STRING | Evet | - |
| `boyut` | Oluşturulan videonun çözünürlüğü (varsayılan: "1280x720") | COMBO | Evet | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `süre` | Oluşturulan videonun saniye cinsinden süresi (varsayılan: 8) | COMBO | Evet | 4<br>8<br>12 |
| `görsel` | Video üretimi için kullanılan isteğe bağlı girdi referans görseli; yalnızca tek bir görsel desteklenir | IMAGE | Hayır | - |
| `tohum` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirlemek için tohum; gerçek sonuçlar tohumdan bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Hayır | 0 - 2147483647 |

**Kısıtlamalar ve Sınırlamalar:**

- "sora-2" modeli yalnızca "720x1280" ve "1280x720" boyutlarını destekler; "sora-2" ile "1024x1792" veya "1792x1024" seçmek hata verir. Daha büyük boyutlar yalnızca "sora-2-pro" ile kullanılabilir.
- Bir görsel bağlandığında, tam olarak bir görsel içermelidir; birden fazla görsel bağlamak hata verir.
- Sonuçlar, tohum değerinden bağımsız olarak deterministik değildir.
- Görüntülenen fiyat tahmini seçilen `model`, `size` ve `duration` değerlerine bağlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | OpenAI Sora tarafından oluşturulan video | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/tr.md)

---
**Source fingerprint (SHA-256):** `d19eb6b65d7f712278828e4b1f7105068cc5e7cb72813b7549ab24520e7719fc`
