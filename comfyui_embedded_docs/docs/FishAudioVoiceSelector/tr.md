# Fish Audio Ses Seçici

Fish Audio Voice Selector düğümü, metinden sese üretim için Fish Audio kütüphanesinden bir ses seçer. Yerleşik hazır seslerden birini seçebilir veya fish.audio'dan herhangi bir ses modeli kimliğini girmek üzere "custom" seçeneğini seçebilirsiniz.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `voice` | Bir ses seçin veya herhangi bir fish.audio ses modeli kimliğini girmek için 'custom' seçeneğini seçin. | DYNAMIC_COMBO | Evet | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

Hazır ses seçenekleri İngilizce (en), Çince (zh) ve Japonca (ja) sesleri kapsar ve herhangi bir ek girdi gerektirmez.

### Özel Girdiler

Bu girdiler `voice` "custom" olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `voice_id` | fish.audio'dan ses modeli kimliği, örn. https://fish.audio/m/<id>/ içindeki kimlik. Varsayılan: boş dize. | STRING | Evet | Herhangi bir geçerli Fish Audio ses modeli kimliği |

Not: `voice` "custom" olarak ayarlandığında, boşluklar kırpıldıktan sonra `voice_id` boş olmamalıdır; aksi takdirde düğüm bir "Custom voice ID is empty." hatası verir. Tanınmayan bir ses seçeneği aktarılırsa, düğüm bir "Unknown voice" hatası verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `voice` | Seçilen Fish Audio ses modeli kimliği. Hazır bir ses için Fish Audio kütüphanesinden karşılık gelen ses kimliği döndürülür; "custom" için girilen `voice_id` değeri döndürülür. | FISHAUDIO_VOICE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/tr.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
