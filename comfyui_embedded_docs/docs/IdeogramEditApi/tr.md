# Ideogram 4.5 Edit

Ideogram 4.5 ile bir metin istemi rehberliğinde en fazla 5 görüntüyü düzenleyin veya birleştirin. Görüntü 1 düzenlenecek görüntüdür ve sonraki görüntüler isteğe bağlı referanslardır. Görüntünün tamamı yeniden oluşturulur, bu nedenle sonucun boyutu veya en-boy oranı değişebilir; dokunulmamış pikselleri değişmeden tutmak için bunun yerine Ideogram 4.5 Precise Edit kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model. (varsayılan: `"ideogram-4.5"`) | DYNAMIC_COMBO | Evet | `"ideogram-4.5"` |
| `images` | Büyütülebilir yuva: görüntü 1 düzenlenecek görüntüdür ve görüntü 2 ile 5 arasındakiler isteğe bağlı referanslardır (`image_1` ... `image_5`). İstemde bunlara @Image1, @Image2, ... olarak başvurun; toplu bir girdi her görüntü için bir kez sayılır. Her görüntünün en-boy oranı 1:6 ile 6:1 arasında olmalıdır. | IMAGE | Evet | 1 ile 5 görüntü |
| `prompt` | Düzenleme talimatları. Bağlı görüntülere @Image1 tarzı başvuruları destekler. (varsayılan: boş dize) | STRING | Evet | 1 ile 10000 karakter |
| `size` | Çıktı boyutu. `"auto"` görüntülerden ve istemden yaklaşık 2K boyutunda bir tuval seçer, `"source"` görüntü 1'in boyutunu korur (yaklaşık 4 MP üzerindeki görüntüler önce küçültülür) ve farklı en-boy oranına sahip bir ön ayar sahneyi yeniden düzenler. Aşağıdaki genişlik ve yüksekliği kullanmak için `"custom"` seçeneğini seçin. (varsayılan: `"auto"`) | COMBO | Evet | `"auto"`<br>`"source"`<br>`"(2K) 2048x2048 (1:1)"`<br>`"(2K) 1440x2880 (1:2)"`<br>`"(2K) 2880x1440 (2:1)"`<br>`"(2K) 1664x2496 (2:3)"`<br>`"(2K) 2496x1664 (3:2)"`<br>`"(2K) 1792x2240 (4:5)"`<br>`"(2K) 2240x1792 (5:4)"`<br>`"(2K) 1440x2560 (9:16)"`<br>`"(2K) 2560x1440 (16:9)"`<br>`"(2K) 1600x2560 (5:8)"`<br>`"(2K) 2560x1600 (8:5)"`<br>`"(2K) 1728x2304 (3:4)"`<br>`"(2K) 2304x1728 (4:3)"`<br>`"(2K) 1152x2944 (9:23)"`<br>`"(2K) 2944x1152 (23:9)"`<br>`"(2K) 1248x3328 (3:8)"`<br>`"(2K) 3328x1248 (8:3)"`<br>`"(2K) 1280x3072 (5:12)"`<br>`"(2K) 3072x1280 (12:5)"`<br>`"(2K) 1024x3072 (1:3)"`<br>`"(2K) 3072x1024 (3:1)"`<br>`"(1K) 1024x1024 (1:1)"`<br>`"(1K) 896x1120 (4:5)"`<br>`"(1K) 1120x896 (5:4)"`<br>`"(1K) 864x1152 (3:4)"`<br>`"(1K) 1152x864 (4:3)"`<br>`"(1K) 832x1248 (2:3)"`<br>`"(1K) 1248x832 (3:2)"`<br>`"(1K) 800x1280 (5:8)"`<br>`"(1K) 1280x800 (8:5)"`<br>`"custom"` |
| `width` | Özel çıktı genişliği piksel cinsinden. Yalnızca `size` `"custom"` olduğunda kullanılır. (varsayılan: 2048) | INT | Evet | 256 ile 4608 (adım 32) |
| `height` | Özel çıktı yüksekliği piksel cinsinden. Yalnızca `size` `"custom"` olduğunda kullanılır. (varsayılan: 2048) | INT | Evet | 256 ile 4608 (adım 32) |
| `quality` | Kalite kademesi. Daha yüksek kademeler daha maliyetlidir ve daha uzun sürer. (varsayılan: `"medium"`) | COMBO | Evet | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Üretim için tohum. Aynı görüntüler, istem, ayarlar ve tohum aynı sonucu verir. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 |

### Parametre Kısıtlamaları

- **Görüntü sayısı:** en az 1 ve en fazla 5 görüntü; toplu bir girdi her görüntü için bir kez sayılır. Görüntü 1 düzenlenecek görüntüdür, geri kalanlar referanstır.
- **Görüntü en-boy oranı:** her görüntünün genişliği yüksekliğinin 6 katından, yüksekliği de genişliğinin 6 katından fazla olmamalıdır (1:6 ile 6:1 arasında).
- **İstem etiketleri:** `@ImageN` büyük/küçük harfe duyarsız olarak eşleştirilir ve bağlı görüntü sayısını aşmamalıdır; istem boşluk dışı karakterler içermeli ve en fazla 10000 karakter olmalıdır.
- **Özel boyut:** yalnızca `size` `"custom"` olduğunda kullanılır. Genişlik ile yüksekliğin çarpımı 4194304 pikseli (2048x2048) aşmamalıdır ve uzun kenar kısa kenarın 6 katını aşmamalıdır. Genişlik ve yükseklik 256 ile 4608 arasında olmalıdır ve 32'nin katlarına yuvarlanır.
- **Yükleme ölçekleme:** yaklaşık 4 MP'den büyük veya uzun kenarı 4608 pikselden büyük görüntüler gönderilmeden önce küçültülür.
- **İçerik güvenliği:** Ideogram'ın içerik güvenliği filtresi sonucu engellerse, düğüm bir görüntü döndürmek yerine hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Düzenlenmiş veya birleştirilmiş görüntü(ler) bir toplu iş olarak. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramEditApi/tr.md)

---
**Source fingerprint (SHA-256):** `58c189d65502373ff7b56f5f32d9f2e7ee8019fc58f1bbbb80abc859cf978f67`
