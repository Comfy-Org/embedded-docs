# LtxApi25AudioToVideo

Bu düğüm, LTX 2.5 modelini kullanarak bir ses parçasına uygun video oluşturur. Ses, video süresini belirler (2-20 saniye arası) ve isteğe bağlı olarak ilk kare olarak kullanılacak bir görüntü sağlayabilirsiniz. Video, LTX 2.5 API hizmeti aracılığıyla oluşturulur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ses` | Videoyu yönlendiren ses parçası. Uzunluğu (2-20 saniye) video süresini belirler. | AUDIO | Evet | 2-20 seconds |
| `model` | Kullanılacak LTX 2.5 model sürümü. Çözünürlük modelle birlikte seçilir; her iki model de aynı çözünürlük seçeneklerini sunar (1920x1080 veya 1080x1920). | COMBO | Evet | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `prompt` | Oluşturulan videonun içeriğini yönlendiren metin açıklaması (varsayılan: ""). En az 1 karakter ve en fazla 10000 karakter içermelidir. | STRING | Evet | 1-10000 characters |
| `tohum` | Üretimin rastgeleliğini kontrol eden bir sayı. Aynı seed aynı sonucu üretir (varsayılan: 42). | INT | Evet | Any integer |
| `görsel` | Video için kullanılacak isteğe bağlı ilk kare. Yalnızca bir görüntü desteklenir. | IMAGE | Hayır | Single image |

Kısıtlamalara ilişkin notlar:
- Ses süresi 2 ila 20 saniye arasında olmalıdır; düğüm bu aralığın dışında bir değerde hata verir.
- Prompt zorunludur ve boş olamaz.
- `image` sağlandığında yalnızca tek bir girdi görüntüsü kabul edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Sağlanan ses parçası tarafından yönlendirilen oluşturulmuş video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25AudioToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `ae0d0123c0421f645448496d30a53a21aba1728310180719a4c4599eca8351c5`
