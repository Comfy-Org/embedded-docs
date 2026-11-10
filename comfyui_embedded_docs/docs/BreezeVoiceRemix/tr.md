# Breeze Voice Remix

Aynı dilde bir sesin değiştirilmiş bir kopyasını, değişikliğin yazılı açıklamasından ya da adlandırılmış bir ön ayardan oluşturur. Kopya hesabınıza kaydedilir ve bir ses önizlemesiyle birlikte döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `voice` | Değiştirilecek Breeze sesi. | BREEZE_VOICE | Evet | - |
| `change` | `custom` değişikliği metin olarak açıklar, `preset` adlandırılmış bir değişikliği seçer. Varsayılan: `"custom"`. | DYNAMIC_COMBO | Evet | `"custom"`<br>`"preset"` |
| `strength` | Daha yüksek değerler sesi daha fazla değiştirir. Varsayılan: 4.0. | FLOAT | Hayır | 1.0 ile 10.0 arası (adım: 0.1) |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını kontrol eder; sonuçlar seed değerinden bağımsız olarak deterministik değildir. Varsayılan: 42. | INT | Hayır | 0 ile 2147483647 arası |

### Değişiklik "custom" Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `prompt` | Sesin nasıl değişmesi gerektiği; örneğin daha yaşlı ve boğuk. Varsayılan: boş. | STRING | Evet | Çok satırlı metin |

### Değişiklik "preset" Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `preset` | Adlandırılmış değişiklik; yaş, cinsiyet, perde, tempo, enerji ve duyguya göre gruplandırılmıştır. | COMBO | Evet | Birden çok seçenek mevcut |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `voice` | Sesin değiştirilmiş kopyası. | BREEZE_VOICE |
| `preview` | Yeniden mikslenmiş sesin işitsel önizlemesi. | AUDIO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceRemix/tr.md)

---
**Source fingerprint (SHA-256):** `1bb135706fa760c6a6e8f4b9cb12a3f1506db375ee09cbd511b62d2bb24a9d2c`
