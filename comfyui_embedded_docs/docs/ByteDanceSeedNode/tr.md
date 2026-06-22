# ByteDance Seed

## Genel Bakış ByteDance'ın Seed 2.0 modellerini kullanarak metin yanıtları oluşturun. Çok modlu bağlam için bir metin istemi sağlayın ve isteğe bağlı olarak görseller veya videolar ekleyin.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Modele verilen metin girişi. | STRING | Evet | Yok |
| `model` | Yanıtı oluşturmak için kullanılan Seed modeli. | COMBO | Evet | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `seed` | Seed, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar seed'den bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |
| `system_prompt` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: "") | STRING | Hayır | Yok |

**`model` parametresi hakkında not:** `model` parametresi aynı zamanda görselleri ve videoları kabul eden dinamik bir kombinasyon kutusudur. Çok modlu bağlam sağlamak için bu parametreye görsel ve video girişleri bağlayabilirsiniz. Her istekte en fazla 20 görsel ve 4 video desteklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Seed modelinden oluşturulan metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/tr.md)

---
**Source fingerprint (SHA-256):** `d1ef73cf72e88216d40c0cf727f90c40cf783cecabe3be0e7530fe72dba6c172`
