> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/tr.md)

ElevenLabs Ses Yalıtımı düğümü, bir ses dosyasından arka plan gürültüsünü kaldırarak vokalleri veya konuşmayı izole eder. Sesi işlenmek üzere ElevenLabs API'sine gönderir ve temizlenmiş sesi döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|---------|--------|----------|
| `ses` | AUDIO | Evet | | Arka plan gürültüsü temizliği için işlenecek ses. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `ses` | AUDIO | Arka plan gürültüsü temizlenmiş işlenmiş ses. |

---
**Source fingerprint (SHA-256):** `eca7919ff853fe48f8419a4135a99589e350d3d113631e27f6e7cb3cbb3faa3b`
