ChromaRadianceOptions düğümü, Chroma Radiance modeli için gelişmiş ayarları yapılandırmanıza olanak tanır. Mevcut bir modeli sarar ve sigma değerlerine bağlı olarak gürültü giderme işlemi sırasında belirli seçenekleri uygulayarak NeRF döşeme boyutu ve diğer radyansla ilgili parametreler üzerinde ince ayarlı kontrol sağlar.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Chroma Radiance seçeneklerinin uygulanacağı model | MODEL | Evet | - |
| `sarmalayıcıyı koru` | Etkinleştirildiğinde, mevcut bir model fonksiyon sarmalayıcısı varsa ona devreder. Genellikle etkin bırakılmalıdır. (varsayılan: True) | BOOLEAN | Hayır | - |
| `başlangıç sigma` | Bu seçeneklerin etkili olacağı ilk sigma değeri. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 ile 1.0 arası |
| `bitiş sigma` | Bu seçeneklerin etkili olacağı son sigma değeri. (varsayılan: 0.0) | FLOAT | Hayır | 0.0 ile 1.0 arası |
| `nerf döşeme boyutu` | Varsayılan NeRF döşeme boyutunu geçersiz kılmayı sağlar. -1 varsayılan değeri (32) kullanmak anlamına gelir. 0 döşeme olmayan modu kullanmak anlamına gelir (çok fazla VRAM gerektirebilir). (varsayılan: -1) | INT | Hayır | -1 ve üzeri |

**Not:** Chroma Radiance seçenekleri yalnızca mevcut sigma değeri `end_sigma` ile `start_sigma` arasında (bu değerler dahil) olduğunda etkili olur. `nerf_tile_size` parametresi yalnızca 0 veya daha yüksek değerlere ayarlandığında uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `model` | Chroma Radiance seçenekleri uygulanmış değiştirilmiş model | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/tr.md)

---
**Source fingerprint (SHA-256):** `b49a12e9aba59e4669c59e05a6aeff6d4ae5a4b656ca5b0de4bdf71291dca095`
