# LTX 2.5 Ses'ten Videoya

Bu düğüm, LTX 2.5 modelini kullanarak bir ses parçasını takip eden bir video üretir. Ses, video süresini (2 ila 20 saniye arasında) belirler ve isteğe bağlı olarak ilk kare olarak kullanılacak bir görsel sağlayabilirsiniz. Video, LTX 2.5 API hizmeti aracılığıyla üretilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ses` | Videoyu yönlendiren ses parçası. Uzunluğu (2-20 saniye) video süresini belirler. | AUDIO | Evet | 2-20 saniye |
| `model` | Kullanılacak LTX 2.5 model sürümü. Video çözünürlüğü (1920x1080 veya 1080x1920) modelle birlikte seçilir; her iki model de aynı çözünürlük seçeneklerini sunar. | COMBO | Evet | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `prompt` | Üretilen videonun içeriğini yönlendiren metin açıklaması (varsayılan: ""). En az 1 karakter ve en fazla 10000 karakter içermelidir. | STRING | Evet | 1-10000 karakter |
| `tohum` | Üretimin rastgeleliğini kontrol eden sayı. Aynı seed aynı sonucu üretir (varsayılan: 42). | INT | Evet | Herhangi bir tam sayı |
| `görsel` | Video için kullanılacak isteğe bağlı ilk kare. Yalnızca bir görsel desteklenir. | IMAGE | Hayır | Tek görsel |

Kısıtlamalara ilişkin notlar:
- Ses süresi 2 ila 20 saniye arasında olmalıdır; bu aralığın dışındaysa düğüm bir hata verir.
- Prompt gereklidir ve boş olamaz; 1 ila 10000 karakter arasında olmalıdır.
- `image` sağlandığında yalnızca tek bir giriş görseli kabul edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Sağlanan ses parçası tarafından yönlendirilen üretilmiş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25AudioToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `ae0d0123c0421f645448496d30a53a21aba1728310180719a4c4599eca8351c5`
