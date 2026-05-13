> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/tr.md)

ElevenLabs Ses Seçici düğümü, önceden tanımlanmış ElevenLabs metin-ses dönüştürme sesleri listesinden belirli bir ses seçmenizi sağlar. Girdi olarak bir ses adı alır ve ses oluşturma için gereken karşılık gelen ses tanımlayıcısını çıktı olarak verir. Bu düğüm, diğer ElevenLabs ses düğümleriyle kullanılmak üzere uyumlu bir ses seçme sürecini basitleştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `ses` | STRING | Evet | `"Adam"`<br>`"Antoni"`<br>`"Arnold"`<br>`"Bella"`<br>`"Domi"`<br>`"Elli"`<br>`"Josh"`<br>`"Rachel"`<br>`"Sam"` | Önceden tanımlanmış ElevenLabs sesleri arasından bir ses seçin. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `ses` | STRING | Seçilen ElevenLabs sesi için benzersiz tanımlayıcı. Bu tanımlayıcı, metin-ses dönüştürme işlemi için diğer düğümlere aktarılabilir. |

---
**Source fingerprint (SHA-256):** `b87f5b2b8accca87d0593ab1f4bcfccaa84b393ddb3fd9121758a87871592cee`
