# Ideogram 4.5 Precise Edit

Ideogram 4.5 hassas düzenleme ile bir görseli metin istemi kılavuzluğunda düzenleyin: yalnızca istemin istediği değişir, dokunulmayan pikseller birebir aynı kalır ve çıktı görsel 1'in boyutunu korur. Görsel 1 düzenlenecek görseldir ve referans olarak en fazla 4 görsel daha bağlanabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. (varsayılan: `"ideogram-4.5"`) | DYNAMIC_COMBO | Evet | `"ideogram-4.5"` |
| `images` | Genişletilebilir yuva: görsel 1 düzenlenecek görseldir ve görsel 2 ile 5 isteğe bağlı referanslardır (`image_1` ... `image_5`). İstemde bunlara @Image1, @Image2, ... olarak başvurun; toplu bir girdi her görsel için bir kez sayılır. Her görselin en-boy oranı 1:6 ile 6:1 arasında olmalıdır. | IMAGE | Evet | 1 ile 5 görsel |
| `prompt` | Düzenleme talimatları. Bağlı görsellere @Image1 tarzı başvuruları destekler. (varsayılan: boş dize) | STRING | Evet | 1 ile 10000 karakter |
| `quality` | Kalite kademesi. Daha yüksek kademeler daha pahalıdır ve daha uzun sürer. (varsayılan: `"medium"`) | COMBO | Evet | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Üretim için tohum. Aynı görseller, istem, ayarlar ve tohum aynı sonucu verir. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 |

### Parametre Kısıtlamaları

- **Görsel sayısı:** en az 1, en fazla 5 görsel; toplu bir girdi her görsel için bir kez sayılır. Görsel 1 düzenlenecek görseldir ve görsel 2 ile 5 referanstır.
- **Çıktı boyutu:** sonuç görsel 1'in boyutunu korur, bu nedenle bu düğümde boyut, genişlik veya yükseklik girdisi yoktur.
- **Görsel en-boy oranı:** her görsel, yüksekliğinin 6 katından daha geniş ve genişliğinin 6 katından daha uzun olmamalıdır (1:6 ile 6:1 arasında).
- **İstem etiketleri:** `@ImageN` büyük/küçük harfe duyarsız olarak eşleştirilir ve bağlı görsel sayısını aşmamalıdır; istem yalnızca boşluklardan oluşmamalı ve en fazla 10000 karakter olmalıdır.
- **Yükleme ölçekleme:** yaklaşık 4 MP'den büyük veya uzun kenarı 4608 px'den büyük görseller gönderilmeden önce küçültülür.
- **İçerik güvenliği:** Ideogram'ın içerik güvenliği filtresi sonucu engellerse, düğüm görsel döndürmek yerine hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Düzenlenen görsel, görsel 1 boyutunda toplu halde. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `74ba429ac93e4528e44c864ccfd3928f6c42108cfcc83577c8963a099a66f527`
