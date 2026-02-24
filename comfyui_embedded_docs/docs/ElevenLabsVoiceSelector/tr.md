> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/tr.md)

ElevenLabs Ses Seçici düğümü, önceden tanımlanmış ElevenLabs metinden sese dönüştürme sesleri listesinden belirli bir ses seçmenizi sağlar. Bir ses adını girdi olarak alır ve ses oluşturma için gerekli olan karşılık gelen ses tanımlayıcısını çıktı olarak verir. Bu düğüm, diğer ElevenLabs ses düğümleriyle kullanım için uyumlu bir ses seçme sürecini basitleştirir.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `voice` | STRING | Evet | `"Adam"`<br>`"Antoni"`<br>`"Arnold"`<br>`"Bella"`<br>`"Domi"`<br>`"Elli"`<br>`"Josh"`<br>`"Rachel"`<br>`"Sam"` | Önceden tanımlanmış ElevenLabs seslerinden bir ses seçin. |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `voice` | STRING | Seçilen ElevenLabs sesinin benzersiz tanımlayıcısı. Bu tanımlayıcı, metinden sese dönüştürme işlemi için diğer düğümlere aktarılabilir. |