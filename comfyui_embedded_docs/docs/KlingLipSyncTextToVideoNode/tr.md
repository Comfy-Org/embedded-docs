# Kling Dudak Senkronizasyonu Video ile Metin

Kling Lip Sync Text to Video Düğümü, bir video dosyasındaki ağız hareketlerini bir metin istemiyle eşleşecek şekilde senkronize eder. Bir girdi videosu alır ve karakterin dudak hareketlerinin sağlanan metinle hizalandığı yeni bir video üretir. Düğüm, doğal görünümlü konuşma senkronizasyonu oluşturmak için ses sentezini kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `video` | Dudak senkronizasyonu için girdi video dosyası. Video yükseklik/genişlik olarak 720px ile 1920px arasında, süre olarak 2 sn ile 10 sn arasında olmalı ve 100MB'den büyük olmamalıdır. | VIDEO | Evet | - |
| `text` | Dudak Senkronizasyonu Video Üretimi için Metin İçeriği. Mod text2video olduğunda gereklidir. Maksimum uzunluk 120 karakterdir. | STRING | Evet | - |
| `voice` | Dudak senkronizasyonu sesi için ses seçimi (varsayılan: "Melody"). Hem İngilizce hem de Çince ses seçeneklerini içerir. | COMBO | Hayır | "Melody"<br>"Sunny"<br>"Sage"<br>"Ace"<br>"Blossom"<br>"Peppy"<br>"Dove"<br>"Shine"<br>"Anchor"<br>"Lyric"<br>"Tender"<br>"Siren"<br>"Zippy"<br>"Bud"<br>"Sprite"<br>"Candy"<br>"Beacon"<br>"Rock"<br>"Titan"<br>"Grace"<br>"Helen"<br>"Lore"<br>"Crag"<br>"Prattle"<br>"Hearth"<br>"The Reader"<br>"Commercial Lady"<br>"阳光少年"<br>"懂事小弟"<br>"运动少年"<br>"青春少女"<br>"温柔小妹"<br>"元气少女"<br>"阳光男生"<br>"幽默小哥"<br>"文艺小哥"<br>"甜美邻家"<br>"温柔姐姐"<br>"职场女青"<br>"活泼男童"<br>"俏皮女童"<br>"稳重老爸"<br>"温柔妈妈"<br>"严肃上司"<br>"优雅贵妇"<br>"慈祥爷爷"<br>"唠叨爷爷"<br>"唠叨奶奶"<br>"和蔼奶奶"<br>"东北老铁"<br>"重庆小伙"<br>"四川妹子"<br>"潮汕大叔"<br>"台湾男生"<br>"西安掌柜"<br>"天津姐姐"<br>"新闻播报男"<br>"译制片男"<br>"撒娇女友"<br>"刀片烟嗓"<br>"乖巧正太" |
| `voice_speed` | Konuşma Hızı. Geçerli aralık: 0.8~2.0, bir ondalık basamağa kadar hassas. (varsayılan: 1) | FLOAT | Hayır | 0.8-2.0 |

**Video Gereksinimleri:**

- Video dosyası 100MB'den büyük olmamalıdır
- Yükseklik/genişlik 720px ile 1920px arasında olmalıdır
- Süre 2 sn ile 10 sn arasında olmalıdır

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Dudak senkronizasyonlu ses içeren üretilmiş video | VIDEO |
| `video_id` | Üretilen video için benzersiz tanımlayıcı | STRING |
| `duration` | Üretilen video için süre bilgisi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `28a7be92d7e8a57efeb7e2913124e4373dfc75fbdba6ff7036fafb3a8ae43a60`
