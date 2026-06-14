# Runway Aleph2 Ana Kare Düğümü

Bu düğüm, bir yönlendirme görüntüsünü giriş videonuzun belirli bir anına sabitler, böylece Aleph2 modeli düzenlemeyi görüntünüzdeki o noktaya yönlendirir. Bu düğümü Runway Aleph2 Video'dan Video'ya düğümünün "keyframes" girişine bağlayın ve isteğe bağlı "keyframes" girişi aracılığıyla birkaçını (en fazla 5) birbirine zincirleyin.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `image` | Giriş videosunun seçilen anında uygulanacak yönlendirme görüntüsü. | IMAGE | Evet | - |
| `timing` | Bu görüntünün giriş videosunun zaman çizelgesine nasıl yerleştirileceği. | COMBO | Evet | Aşağıya bakın |
| `keyframes` | Bu ana kareyle zincirlenecek isteğe bağlı önceki ana kareler. | KEYFRAME | Hayır | - |

### Zamanlama Parametre Seçenekleri

`timing` parametresinin iki modu vardır:

| Mod | Alt parametre | Açıklama | Aralık |
|-----|---------------|----------|--------|
| "Mutlak saniye" | `seconds` | Bu görüntünün uygulandığı, giriş videosunun başlangıcından itibaren saniye cinsinden süre (varsayılan: 0.0) | 0.0 ila 30.0, adım 0.1 |
| "Sürenin kesri" | `fraction` | Bu görüntünün uygulandığı, giriş videosundaki konum, süresinin bir kesri olarak (0.0 = başlangıç, 1.0 = bitiş) (varsayılan: 0.0) | 0.0 ila 1.0, adım 0.01 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `keyframes` | Bu ana kareyi ve önceden bağlanmış tüm ana kareleri içeren bir ana kare zinciri. | KEYFRAME |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2KeyframeNode/tr.md)

---
**Source fingerprint (SHA-256):** `b5ac6553166b7366fd35f97740861be163f91bc2353f5f83bdc2f04bf40f8478`
