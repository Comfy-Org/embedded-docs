> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitAudioChannels/tr.md)

SplitAudioChannels düğümü, stereo sesi ayrı sol ve sağ kanallara ayırır. İki kanallı bir stereo ses girişi alır ve sol kanal ve sağ kanal için olmak üzere iki ayrı ses akışı çıktısı verir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Evet | - | Kanallara ayrılacak stereo ses girişi |

**Not:** Giriş sesinin tam olarak iki kanalı (stereo) olmalıdır. Giriş sesinin yalnızca bir kanalı varsa, düğüm bir hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `left` | AUDIO | Ayrılmış sol kanal sesi |
| `right` | AUDIO | Ayrılmış sağ kanal sesi |