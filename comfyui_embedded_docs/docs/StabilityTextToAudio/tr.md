# Stability AI Metin'den Ses'e

Metin açıklamalarından yüksek kaliteli müzik ve ses efektleri üretir. Bu düğüm, metin istemlerinize dayalı olarak ses içeriği oluşturmak için Stability AI'nın ses üretim teknolojisini kullanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak ses üretim modeli (varsayılan: "stable-audio-2.5") | COMBO | Evet | `"stable-audio-2.5"` |
| `prompt` | Ses içeriği oluşturmak için kullanılan metin açıklaması (varsayılan: boş dize) | STRING | Evet | - |
| `süre` | Oluşturulan sesin saniye cinsinden süresini kontrol eder (varsayılan: 190) | INT | Hayır | 1-190 |
| `tohum` | Üretim için kullanılan rastgele tohum değeri (varsayılan: 0) | INT | Hayır | 0-4294967294 |
| `adımlar` | Örnekleme adımlarının sayısını kontrol eder (varsayılan: 8) | INT | Hayır | 4-8 |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Metin istemine göre oluşturulan ses dosyası | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/tr.md)

---
**Source fingerprint (SHA-256):** `5185241ca7a9b4bc38dfa8bafdae63ec3c151a3038a26ffe8e35492c0550fa88`
