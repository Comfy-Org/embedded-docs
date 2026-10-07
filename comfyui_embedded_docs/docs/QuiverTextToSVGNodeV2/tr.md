# Quiver Text to SVG

Quiver AI ile bir metin isteminden ölçeklenebilir vektör grafiği (SVG) oluşturun. İsteğe bağlı referans görselleri ve stil talimatları oluşturmayı yönlendirebilir.

Bir `model` seçmek, aşağıda listelenen modele özgü parametreleri ortaya çıkarır ve maksimum referans görseli sayısı da seçilen modele bağlıdır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | SVG oluşturmak için kullanılacak model. | DYNAMIC_COMBO | Evet | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `prompt` | İstenen SVG çıktısının metin açıklaması. En az bir boşluk olmayan karakter içermelidir (varsayılan: boş). | STRING | Evet | Herhangi bir metin |
| `instructions` | Ek stil veya biçimlendirme rehberliği. İsteğe bağlı gelişmiş parametre (varsayılan: boş). | STRING | Hayır | Herhangi bir metin |
| `reference_images` | Büyütülebilir yuva: oluşturmayı yönlendiren bir veya daha fazla isteğe bağlı referans görseli (`ref_1`, `ref_2`, ...) bağlayın. Maksimum görsel sayısı seçilen modele bağlıdır. | IMAGE | Hayır | En fazla 14<br>En fazla 4 |
| `width` | Çıktı SVG tuvalinin (viewBox) genişliği, kullanıcı birimleri cinsinden. Çıktı boyutunu ve en-boy oranını kontrol etmek için hem `width` hem de `height` değerlerini ayarlayın; modelin seçmesine izin vermek için herhangi birini 0 olarak bırakın, bu genellikle kare bir tuval verir. Gelişmiş parametre (varsayılan: 0). | INT | Evet | 0 ile 8192 arası |
| `height` | Çıktı SVG tuvalinin (viewBox) yüksekliği, kullanıcı birimleri cinsinden. Çıktı boyutunu ve en-boy oranını kontrol etmek için hem `width` hem de `height` değerlerini ayarlayın; modelin seçmesine izin vermek için herhangi birini 0 olarak bırakın, bu genellikle kare bir tuval verir. Gelişmiş parametre (varsayılan: 0). | INT | Evet | 0 ile 8192 arası |
| `seed` | Düğümün yeniden çalışıp çalışmayacağını belirleyen tohum; gerçek sonuçlar tohum değerinden bağımsız olarak deterministik değildir. Bu parametre "oluşturma sonrası kontrol" işlevine sahiptir (varsayılan: 42). | INT | Evet | 0 ile 2147483647 arası |

### Modele Özgü Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Modelin çizim yapmadan önce ne kadar akıl yürütme harcadığı. Daha yüksek seviyeler ayrıntıyı artırır ve daha fazla token maliyeti getirir. Yalnızca `"arrow-2"` ve `"arrow-2-telos"` modelleri tarafından kullanılır (varsayılan: `"high"`). | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | Rastgelelik kontrolü. Daha yüksek değerler rastgeleliği artırır. `"arrow-2-telos"` modeli tarafından kullanılmaz. Gelişmiş parametre (varsayılan: 1.0). | FLOAT | Evet | 0.0 ile 2.0 arası (adım: 0.1) |
| `top_p` | Çekirdek örnekleme parametresi. `"arrow-2-telos"` modeli tarafından kullanılmaz. Gelişmiş parametre (varsayılan: 1.0). | FLOAT | Evet | 0.05 ile 1.0 arası (adım: 0.05) |
| `presence_penalty` | Token varlık cezası. `"arrow-2-telos"` modeli tarafından kullanılmaz. Gelişmiş parametre (varsayılan: 0.0). | FLOAT | Evet | -2.0 ile 2.0 arası (adım: 0.1) |

**Not:** `reference_images` için maksimum sayı `"arrow-2"`, `"arrow-2-telos"` ve `"arrow-1.1-max"` için 14, `"arrow-1.1"` ve `"arrow-preview"` için 4'tür. Tuval boyutunu modelin seçmesine izin vermek için `width` veya `height` değerini 0 olarak bırakın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `SVG` | Oluşturulan SVG çıktısı. | SVG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `809d2e5bd62386723e36b7649af2f8dda40b437dc39bac9236529db5b52d32e9`
