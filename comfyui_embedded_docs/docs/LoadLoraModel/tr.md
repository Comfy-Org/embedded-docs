# Load LoRA (Model)

Bir difüzyon modeline tek bir düğümde bir LoRA yığını uygulayın. `loras` öğesinin her satırı bir LoRA dosyasını, gücünü ve bir açık/kapalı anahtarını tutar; satırlar yukarıdan aşağıya uygulanır, böylece her satır üstündeki satırın sonucuna yama uygular. Bir iş akışı aynı modele uzun bir LoRA listesi uyguladığında, birkaç tekli LoRA yükleyiciyi zincirlemek yerine bu düğümü kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | LoRA'ların uygulanacağı difüzyon modeli. | MODEL | Evet | - |
| `loras` | Modele satır sırasıyla (`loras.0`, `loras.1`, vb.) uygulanan genişletilebilir LoRA grubu. Her LoRA için bir satır ekleyin; her satır bir dosya, bir güç ve bir açık/kapalı anahtarı tutar. | DYNAMIC_GROUP | Evet | 1 ila 20 satır |

### `loras` Satır Alanları

Her satır aşağıdaki alanları yineler ve gönderilen bir satırda her alan zorunludur.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `lora_name` | Uygulanacak LoRA dosyasının adı. | COMBO | Evet | Birden çok seçenek mevcut |
| `strength` | Bu LoRA'nın ne kadar güçlü uygulanacağı. `0` onu kapatır ve negatif bir değer etkiyi tersine çevirir. (varsayılan: 1.0) | FLOAT | Evet | -100 ile 100 arası (adım: 0.01) |
| `enabled` | Dosyasını veya gücünü değiştirmeden bu LoRA'yı atlamak için kapatın. (varsayılan: true) | BOOLEAN | Evet | false / true |

### Parametre Kısıtları

- **Satır sayısı:** en az bir satır gönderilmelidir ve en fazla 20 satır kabul edilir, bu nedenle en yüksek satır dizini 19'dur.
- **Atlanan satırlar:** bir satırın dosyası boş olduğunda, `enabled` kapalı olduğunda veya `strength` `0` olduğunda atlanır. Negatif bir güç değeri atlanmak yerine geçirilir.
- **Satır sırası:** satırlar göründükleri sırayla uygulanır ve her satır bir önceki satırın döndürdüğü modelden başlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL` | Atlanmayan LoRA satırları uygulandıktan sonraki difüzyon modeli. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraModel/tr.md)

---
**Source fingerprint (SHA-256):** `a656bba0248d2f6d4eb65e15e3a19f2e76edecd4b34710921a02f3ba5c598e1d`
