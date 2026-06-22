# Kanca Anahtar Karesi Oluştur

Create Hook Keyframe düğümü, üretim sürecinde kanca davranışının değiştiği belirli noktaları tanımlamanızı sağlar. Üretim ilerlemesinin belirli yüzdelerinde kancaların gücünü değiştiren anahtar kareler oluşturur ve bu anahtar kareler karmaşık zamanlama desenleri oluşturmak için birbirine zincirlenebilir.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `güç_çarpanı` | Bu anahtar karedeki kanca gücü çarpanı (varsayılan: 1.0) | FLOAT | Evet | -20.0 ila 20.0 |
| `başlangıç_yüzdesi` | Bu anahtar karenin etkili olduğu üretim sürecindeki yüzde noktası (varsayılan: 0.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `önceki_kanca_kf` | Bu anahtar kareyi eklemek için isteğe bağlı önceki kanca anahtar kare grubu | HOOK_KEYFRAMES | Hayır | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `HOOK_KF` | Yeni oluşturulan anahtar kareyi içeren bir kanca anahtar kare grubu | HOOK_KEYFRAMES |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/tr.md)

---
**Source fingerprint (SHA-256):** `51893311a0623cafcf8c2d8af00e4005ca2fea2df9474e87d7d4b332b38435c3`
