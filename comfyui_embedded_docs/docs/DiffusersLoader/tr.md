# Diffusers Yükleyici

DiffusersLoader düğümü kullanımdan kaldırılmıştır. Hugging Face diffusers formatında kaydedilmiş önceden eğitilmiş modelleri yükler ve boru hattının ihtiyaç duyduğu üç standart bileşeni döndürür: MODEL, CLIP ve VAE. Düğüm, yapılandırılmış diffusers klasörlerini geçerli model dizinleri için otomatik olarak tarar (`model_index.json` dosyası içeren klasörler) ve hangisinin yükleneceğini seçmenize olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_path` | Yüklenecek diffusers model dizininin yolu. Düğüm, yapılandırılmış diffusers klasörlerini tarar ve `model_index.json` dosyası içeren her dizini listeler. | COMBO | Evet | Yapılandırılmış diffusers klasörlerinden otomatik doldurulur (`model_index.json` dosyası içeren her alt dizin) |

Not: Seçilen yol, keşfedilen modellerin listesine karşı doğrulanır. Yol artık listede değilse veya model dizini bulunamazsa yükleme bir hatayla başarısız olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| MODEL | Diffusers formatından yüklenen model bileşeni | MODEL |
| CLIP | Diffusers formatından yüklenen CLIP metin kodlama modeli bileşeni | CLIP |
| VAE | Diffusers formatından yüklenen VAE (Varyasyonel Otomatik Kodlayıcı) bileşeni | VAE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/tr.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
