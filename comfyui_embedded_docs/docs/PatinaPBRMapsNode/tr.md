# Patina PBR Material Maps

Mevcut bir doku görüntüsünden bir dizi PBR malzeme haritası türetir: basecolor, normal, roughness, metalness ve height. Yalnızca ihtiyaç duyduğunuz haritaları etkinleştirin; çünkü etkinleştirilen her harita maliyeti artırır. Henüz malzeme haritaları olmayan bir dokuyu tamamlamak veya tek bir bozuk haritayı yeniden oluşturmak için kullanın.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | PBR haritalarının türetileceği fotoğraf veya render. | IMAGE | Evet | - |
| `basecolor` | basecolor (albedo) haritasını oluşturun. Varsayılan: True. | BOOLEAN | Evet | true<br>false |
| `normal` | Normal haritasını oluşturun. Varsayılan: True. | BOOLEAN | Evet | true<br>false |
| `roughness` | Pürüzlülük haritasını oluşturun. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `metalness` | Metaliklik haritasını oluşturun. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `height` | Yükseklik (yer değiştirme) haritasını oluşturun. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `seed` | Tekrarlanabilir gürültü giderme için tohum. Varsayılan: 42. | INT | Evet | 0 ile 2147483646 arası |
| `safety_checker` | Sağlayıcının içerik güvenliği denetimini istekte çalıştırın. Gelişmiş ayar. Varsayılan: False. | BOOLEAN | Evet | true<br>false |
| `auto_downscale` | En uzun kenarı modelin girdi sınırı olan 2048 pikseli aşan bir girdi görüntüsünü, en-boy oranını koruyarak otomatik olarak küçültün; daha küçük görüntüler olduğu gibi bırakılır. Aşırı boyutlu görüntülerde bunun yerine hata verilmesi için devre dışı bırakın. Gelişmiş ayar. Varsayılan: True. | BOOLEAN | Hayır | true<br>false |

**Kısıtlamalar ve davranış:**

* En az bir harita etkinleştirilmelidir, aksi halde çalıştırma başarısız olur.
* Girdi görüntüsü en uzun kenarında 2048 piksel ile sınırlıdır; ya `auto_downscale` ile küçültülmesine izin verin ya da aşırı boyutlu bir görüntüde çalıştırma başarısız olur.
* Devre dışı bırakılan her harita yine de bir çıktı döndürür, ancak 1x1 yer tutucu görüntü olarak; bu nedenle yalnızca gerçekten oluşturduğunuz çıktıları bağlayın.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `basecolor` | Oluşturulan basecolor (albedo) haritası veya o harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `normal` | Oluşturulan normal haritası veya o harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `roughness` | Oluşturulan pürüzlülük haritası veya o harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `metalness` | Oluşturulan metaliklik haritası veya o harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |
| `height` | Oluşturulan yükseklik (yer değiştirme) haritası veya o harita devre dışı bırakıldığında 1x1 yer tutucu. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaPBRMapsNode/tr.md)

---
**Source fingerprint (SHA-256):** `813c5bb3336c5ca54a9ca9ee95e84e7f27791170650248d0169acee39c4b3ce1`
