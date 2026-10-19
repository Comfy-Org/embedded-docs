# HeyGen Voice 1.0 Instant Clone

HeyGen'in Voice 1.0 motoruyla tek konuşmacılı bir kayıttan ses klonlayın. Düğüm kaydı yükler, anında bir ses klonu oluşturur, HeyGen işlemeyi bitirene kadar bekler ve `voice_id` değerini döndürür. Bunu HeyGen Voice 1.0 Text to Speech'e veya HeyGen Avatar Video ve HeyGen Talking Photo içindeki `custom_voice_id` alanına bağlayın. Klon oluşturmak ücretsizdir; sesle oluşturduğunuz konuşma için faturalandırılırsınız.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `audio` | Tek konuşmacı kaydı. En az 10 saniye net konuşma kullanın; yalnızca ilk 3 dakika kullanılır. | AUDIO | Evet | N/A |
| `language` | Kayıtta konuşulan dil (varsayılan: "auto"). | COMBO | Evet | `"auto"`<br>Birden çok dil ön ayarı |
| `similarity` | Sesin kaydı ne kadar yakından takip ettiği (varsayılan: "max"). | COMBO | Evet | `"medium"`<br>`"high"`<br>`"extra_high"`<br>`"max"` |
| `remove_background_noise` | Klonlamadan önce kayıttaki arka plan gürültüsünü temizleyin (varsayılan: True). | BOOLEAN | Evet | True<br>False |
| `seed` | Kaydı yeniden klonlamak için tohumu değiştirin; her klon biraz farklı bir sestir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

**Not:** Ses, HeyGen hesabınızda "ComfyUI Voice" olarak oluşturulur ve düğüm, yeniden kullanmak üzere kopyalayabilmeniz için `voice_id` değerini arayüzde yazdırır. Konuşmacı, yakından ilişkili bir dille kolayca karıştırılabilecek bir dil konuşmuyorsa `language` değerini "auto" olarak bırakın. `seed` girdisi, arayüzde sabit bir Control After Generate kontrolü içerir, bu nedenle başka bir klon istediğinizde onu elle değiştirin.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `voice_id` | Klonlanan sesin kimliği; HeyGen Voice 1.0 Text to Speech düğümünde veya `custom_voice_id` olarak yeniden kullanım için. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneNode/tr.md)

---
**Source fingerprint (SHA-256):** `0bf5c7170d140936841cc4afd28022574df8e4c2280137607dcfca8e36862317`
