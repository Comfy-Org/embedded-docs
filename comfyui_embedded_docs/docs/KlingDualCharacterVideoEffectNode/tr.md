> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/tr.md)

Kling Çift Karakterli Video Efekt Düğümü, seçilen sahneye göre özel efektler içeren videolar oluşturur. İki görüntü alır ve ilk görüntüyü bileşik videonun sol tarafına, ikinci görüntüyü sağ tarafına yerleştirir. Seçilen efekt sahnesine bağlı olarak farklı görsel efektler uygulanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `image_left` | IMAGE | Evet | - | Sol taraftaki görüntü |
| `image_right` | IMAGE | Evet | - | Sağ taraftaki görüntü |
| `effect_scene` | COMBO | Evet | `"chat"`<br>`"dance"`<br>`"hug"`<br>`"kill"`<br>`"kiss"`<br>`"pat"`<br>`"punch"`<br>`"shrug"`<br>`"slap"`<br>`"tickle"` | Video oluşturmaya uygulanacak özel efekt sahnesinin türü |
| `model_name` | COMBO | Hayır | `"kling-v1"`<br>`"kling-v1-5"`<br>`"kling-v1-6"` | Karakter efektleri için kullanılacak model (varsayılan: "kling-v1") |
| `mode` | COMBO | Hayır | `"std"`<br>`"pro"` | Video oluşturma modu (varsayılan: "std") |
| `duration` | COMBO | Evet | `"5"`<br>`"10"` | Oluşturulan videonun saniye cinsinden süresi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | VIDEO | Çift karakter efektleriyle oluşturulan video |
| `duration` | STRING | Oluşturulan videonun süre bilgisi |

---
**Source fingerprint (SHA-256):** `4ee0c3cd834e1c70e41b40b66ac98d15a8b88993e7dc9d9df9fb4fadb868f079`
