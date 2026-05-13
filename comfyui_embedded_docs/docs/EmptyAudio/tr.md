> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAudio/tr.md)

BoşSes düğümü, belirtilen süre, örnekleme hızı ve kanal yapılandırmasına sahip sessiz bir ses klibi oluşturur. Tümü sıfırlardan oluşan bir dalga formu üreterek belirtilen süre boyunca tam sessizlik sağlar. Bu düğüm, yer tutucu ses oluşturmak veya ses iş akışlarında sessiz bölümler oluşturmak için kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `duration` | FLOAT | Evet | 0,0 ile 1,8446744073709552e+19 arası | Boş ses klibinin saniye cinsinden süresi (varsayılan: 60,0) |
| `sample_rate` | INT | Evet | 1 ile 192000 arası | Boş ses klibinin örnekleme hızı (varsayılan: 44100) |
| `channels` | INT | Evet | 1 ile 2 arası | Ses kanalı sayısı (1 mono, 2 stereo için) (varsayılan: 2) |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `AUDIO` | AUDIO | Dalga formu verileri ve örnekleme hızı bilgilerini içeren oluşturulan sessiz ses klibi |

---
**Source fingerprint (SHA-256):** `61b9cd6c8e518f28533b7586fdd1f909e5c356c7f2f7690da4e1ec7965d53c5d`
