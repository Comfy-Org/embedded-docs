Kling Çift Karakterli Video Efekt Düğümü, seçilen sahneye göre özel efektler içeren videolar oluşturur. İki görüntü alır ve ilk görüntüyü bileşik videonun sol tarafına, ikinci görüntüyü sağ tarafına yerleştirir. Seçilen efekt sahnesine bağlı olarak farklı görsel efektler uygulanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `sol_görüntü` | Sol taraftaki görüntü | IMAGE | Evet | - |
| `sağ_görüntü` | Sağ taraftaki görüntü | IMAGE | Evet | - |
| `efekt_sahnesi` | Video oluşturmaya uygulanacak özel efekt sahnesinin türü | COMBO | Evet | `"chat"`<br>`"dance"`<br>`"hug"`<br>`"kill"`<br>`"kiss"`<br>`"pat"`<br>`"punch"`<br>`"shrug"`<br>`"slap"`<br>`"tickle"` |
| `model_adı` | Karakter efektleri için kullanılacak model (varsayılan: "kling-v1") | COMBO | Hayır | `"kling-v1"`<br>`"kling-v1-5"`<br>`"kling-v1-6"` |
| `mod` | Video oluşturma modu (varsayılan: "std") | COMBO | Hayır | `"std"`<br>`"pro"` |
| `süre` | Oluşturulan videonun saniye cinsinden süresi | COMBO | Evet | `"5"`<br>`"10"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `süre` | Çift karakter efektleriyle oluşturulan video | VIDEO |
| `süre` | Oluşturulan videonun süre bilgisi | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/tr.md)

---
**Source fingerprint (SHA-256):** `4ee0c3cd834e1c70e41b40b66ac98d15a8b88993e7dc9d9df9fb4fadb868f079`
