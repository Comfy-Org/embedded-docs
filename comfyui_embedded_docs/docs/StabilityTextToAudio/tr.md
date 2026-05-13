> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/tr.md)

Metin açıklamalarından yüksek kaliteli müzik ve ses efektleri üretir. Bu düğüm, metin istemlerinize dayalı olarak ses içeriği oluşturmak için Stability AI'nın ses üretim teknolojisini kullanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | COMBO | Evet | `"stable-audio-2.5"` | Kullanılacak ses üretim modeli (varsayılan: "stable-audio-2.5") |
| `prompt` | STRING | Evet | - | Ses içeriği oluşturmak için kullanılan metin açıklaması (varsayılan: boş dize) |
| `süre` | INT | Hayır | 1-190 | Oluşturulan sesin saniye cinsinden süresini kontrol eder (varsayılan: 190) |
| `tohum` | INT | Hayır | 0-4294967294 | Üretim için kullanılan rastgele tohum değeri (varsayılan: 0) |
| `adımlar` | INT | Hayır | 4-8 | Örnekleme adımlarının sayısını kontrol eder (varsayılan: 8) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `audio` | AUDIO | Metin istemine göre oluşturulan ses dosyası |

---
**Source fingerprint (SHA-256):** `5185241ca7a9b4bc38dfa8bafdae63ec3c151a3038a26ffe8e35492c0550fa88`
