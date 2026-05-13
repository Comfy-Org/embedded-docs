> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/tr.md)

ChromaRadianceOptions düğümü, Chroma Radiance modeli için gelişmiş ayarları yapılandırmanıza olanak tanır. Mevcut bir modeli sarar ve sigma değerlerine bağlı olarak gürültü giderme işlemi sırasında belirli seçenekleri uygulayarak NeRF döşeme boyutu ve diğer radyansla ilgili parametreler üzerinde ince ayarlı kontrol sağlar.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Evet | - | Chroma Radiance seçeneklerinin uygulanacağı model |
| `preserve_wrapper` | BOOLEAN | Hayır | - | Etkinleştirildiğinde, mevcut bir model fonksiyon sarmalayıcısı varsa ona devreder. Genellikle etkin bırakılmalıdır. (varsayılan: True) |
| `start_sigma` | FLOAT | Hayır | 0.0 ile 1.0 arası | Bu seçeneklerin etkili olacağı ilk sigma değeri. (varsayılan: 1.0) |
| `end_sigma` | FLOAT | Hayır | 0.0 ile 1.0 arası | Bu seçeneklerin etkili olacağı son sigma değeri. (varsayılan: 0.0) |
| `nerf_tile_size` | INT | Hayır | -1 ve üzeri | Varsayılan NeRF döşeme boyutunu geçersiz kılmayı sağlar. -1 varsayılan değeri (32) kullanmak anlamına gelir. 0 döşeme olmayan modu kullanmak anlamına gelir (çok fazla VRAM gerektirebilir). (varsayılan: -1) |

**Not:** Chroma Radiance seçenekleri yalnızca mevcut sigma değeri `end_sigma` ile `start_sigma` arasında (bu değerler dahil) olduğunda etkili olur. `nerf_tile_size` parametresi yalnızca 0 veya daha yüksek değerlere ayarlandığında uygulanır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `model` | MODEL | Chroma Radiance seçenekleri uygulanmış değiştirilmiş model |

---
**Source fingerprint (SHA-256):** `b49a12e9aba59e4669c59e05a6aeff6d4ae5a4b656ca5b0de4bdf71291dca095`
