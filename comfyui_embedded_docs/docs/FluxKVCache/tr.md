> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKVCache/tr.md)

Flux KV Cache düğümü, Flux ailesi modelleri için Anahtar-Değer (KV) Önbellek optimizasyonunu etkinleştirir. Bu optimizasyon, referans görseller kullanılırken belirli hesaplamaları önbelleğe alarak performansı artırır ve üretim sürecini hızlandırabilir.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|--------|----------|
| `model` | MODEL | Evet | | KV Önbellek optimizasyonunun uygulanacağı model. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|----------|
| `model` | MODEL | KV Önbellek optimizasyonu etkinleştirilmiş yamalı model. |

---
**Source fingerprint (SHA-256):** `530c660ae23607d4035815826ae73cdcbebe7693ba47a3b0fe98e69f329b9e86`
