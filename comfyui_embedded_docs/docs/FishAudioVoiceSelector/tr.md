# FishAudioVoiceSelector

Fish Audio Ses Seçici düğümü, metinden konuşmaya (text-to-speech) üretimi için Fish Audio kütüphanesinden bir ses seçer. Yerleşik hazır seslerden birini seçebilir veya fish.audio'dan herhangi bir ses modeli kimliği girmek için "custom" seçeneğini belirleyebilirsiniz.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ses` | Bir ses seçin veya herhangi bir fish.audio ses modeli kimliği girmek için 'custom' seçeneğini belirleyin. | DYNAMIC_COMBO | Evet | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

Hazır ses seçenekleri İngilizce (en), Çince (zh) ve Japonca (ja) seslerini kapsar ve ek girdi gerektirmez.

### Özel Girdiler

Bu girdiler, `voice` "custom" olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `voice_id` | fish.audio'dan ses modeli kimliği, örn. https://fish.audio/m/<id>/ içindeki kimlik. Varsayılan: boş dize. | STRING | Evet | Geçerli herhangi bir Fish Audio ses modeli kimliği |

Not: `voice` "custom" olarak ayarlandığında, `voice_id` boşluklar temizlendikten sonra boş olmamalıdır; aksi takdirde düğüm "Custom voice ID is empty." (Özel ses kimliği boş) hatası verir. Tanınmayan bir ses seçeneği iletilirse düğüm "Unknown voice" (Bilinmeyen ses) hatası verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `ses` | Seçilen Fish Audio ses modeli kimliği. Hazır bir ses için Fish Audio kütüphanesinden ilgili ses kimliği döndürülür; "custom" için girilen `voice_id` değeri döndürülür. | FISHAUDIO_VOICE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/tr.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
