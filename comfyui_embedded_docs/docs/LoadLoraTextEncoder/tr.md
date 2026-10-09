# Load LoRA (Text Encoder)

Tek bir düğümde bir CLIP metin kodlayıcısına bir LoRA yığını uygulayın. `loras` öğesinin her satırı bir LoRA dosyası, gücü ve bir açık/kapalı anahtarı tutar; satırlar yukarıdan aşağıya uygulanır, böylece her satır kendisinden önceki satırın sonucuna yama uygular. Metin kodlayıcıyı değiştiren LoRA dosyaları genellikle modele de uygulanır, bu nedenle bu düğüm normalde aynı satırlar kullanılarak Load LoRA (Model) ile eşleştirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `clip` | LoRA'ların uygulanacağı CLIP metin kodlayıcısı. | CLIP | Evet | - |
| `loras` | Metin kodlayıcıya satır sırasına göre uygulanan büyütülebilir LoRA grubu (`loras.0`, `loras.1` vb.). Her LoRA için bir satır ekleyin; her satır bir dosya, bir güç ve bir açma/kapama anahtarı tutar. | DYNAMIC_GROUP | Evet | 1 ila 20 satır |

### `loras` Satır Alanları

Her satır aşağıdaki alanları yineler ve gönderilen bir satırda her alan gereklidir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `lora_name` | Uygulanacak LoRA dosyasının adı. | COMBO | Evet | Birden çok seçenek mevcut |
| `strength` | Bu LoRA'nın metin kodlayıcıya ne kadar güçlü uygulanacağı. `0` onu kapatır ve negatif bir değer etkiyi tersine çevirir. (varsayılan: 1.0) | FLOAT | Evet | -100 ila 100 (adım 0.01) |
| `enabled` | Dosyasını veya gücünü değiştirmeden bu LoRA'yı atlamak için kapatın. (varsayılan: true) | BOOLEAN | Evet | false / true |

### Parametre Kısıtlamaları

- **Satır sayısı:** en az bir satır gönderilmelidir ve en fazla 20 satır kabul edilir, bu nedenle en yüksek satır dizini 19'dur.
- **Atlanan satırlar:** bir satırın dosyası boş olduğunda, `enabled` kapalı olduğunda veya `strength` `0` olduğunda o satır atlanır. Negatif bir güç, atlanmak yerine olduğu gibi aktarılır.
- **Satır sırası:** satırlar göründükleri sıraya göre uygulanır ve her satır, önceki satır tarafından döndürülen metin kodlayıcıdan başlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `CLIP` | Etkinleştirilmiş her LoRA satırı uygulanmış CLIP metin kodlayıcısı. | CLIP |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraTextEncoder/tr.md)

---
**Source fingerprint (SHA-256):** `0b290d2caddc3937e962e65c70a5c99cbd4cdb40ab6f86bba8f0c270e5cebf00`
