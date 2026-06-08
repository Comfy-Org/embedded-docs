SplitAudioChannels düğümü, stereo sesi ayrı sol ve sağ kanallara ayırır. İki kanallı bir stereo ses girişi alır ve biri sol kanal, diğeri sağ kanal için olmak üzere iki ayrı ses akışı çıktısı verir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ses` | Kanallara ayrılacak stereo ses girişi | AUDIO | Evet | - |

**Not:** Giriş sesi tam olarak iki kanallı (stereo) olmalıdır. Giriş sesi yalnızca bir kanallı ise düğüm bir hata verecektir.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `left` | Ayrılmış sol kanal sesi | AUDIO |
| `right` | Ayrılmış sağ kanal sesi | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitAudioChannels/tr.md)

---
**Source fingerprint (SHA-256):** `48f329f3eb9749e75eda1038c43caf42ee63d8a1fa66ab29ad3d34b5d136e323`
