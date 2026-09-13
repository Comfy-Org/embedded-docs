# BriaAddObject

Bu düğüm, düz metinle açıklanan bir nesneyi Bria kullanarak bir görüntüye ekler. Bria tüm kareyi yaklaşık 1 megapikselde yeniden oluşturur; bu nedenle sonuç, girişle piksel hizalı değildir.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Açıklanan nesnenin ekleneceği görüntü. Görüntü yüklenmeden önce alfa kanalı kaldırılır. | IMAGE | Evet | - |
| `instruction` | Neyin ve nereye ekleneceği; örneğin 'Masanın üzerine çiçekli kırmızı bir vazo yerleştir'. Boş olmamalıdır. Varsayılan: "" (boş dize). | STRING | Evet | - |
| `seed` | Bria burada seed almaz ve düzenlemeyi her çağrıda yeniden yorumlar; bu nedenle tekrarlanan çalıştırmalar farklılık gösterebilir. Değer hiçbir zaman gönderilmez: yalnızca bu düğümün önbellek anahtarını değiştirir, böylece aksi halde aynı olan bir grafik önbelleğe alınmış sonucu döndürmek yerine düzenlemeyi yeniden çalıştırır. Varsayılan: 42. | INT | Evet | 0 - 2147483647 |
| `moderation` | Moderasyon ayarları. Aşağıdaki moderasyon bayraklarını göstermek için "true" seçeneğini belirleyin. | DYNAMIC_COMBO | Evet | "false"<br>"true" |

### Moderasyon Etkinleştirildiğinde Girdiler

`moderation` "true" olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Giriş görüntüsünde içerik moderasyonunu etkinleştirir. Varsayılan: False. | BOOLEAN | Hayır | True / False |
| `visual_output_moderation` | Oluşturulan çıktı görüntüsünde içerik moderasyonunu etkinleştirir. Varsayılan: False. | BOOLEAN | Hayır | True / False |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Açıklanan nesnenin eklendiği düzenlenmiş görüntü. | IMAGE |
| `structured_prompt` | Düzenlenmiş görüntünün yapılandırılmış açıklaması; Bria FIBO Image Edit ile yapılacak sonraki düzenleme için. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaAddObject/tr.md)

---
**Source fingerprint (SHA-256):** `41c9a3e511763372d8dc8be9da4f70158e53d5156a88eb3c66f81149efdbd566`
