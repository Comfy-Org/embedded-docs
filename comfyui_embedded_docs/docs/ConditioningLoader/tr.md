# Koşullandırmayı Yükle

Bu düğüm, Save Conditioning düğümüyle daha önce kaydedilmiş bir conditioning verisini veya `conditioning` tensörü içeren herhangi bir safetensors dosyasını embeddings klasöründen yükler. Ayrıca conditioning ile birlikte saklanan tüm ek seçenekleri ve numaralı liste değerlerini geri yükler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `conditioning_name` | embeddings klasöründen yüklenecek dosya. Seçenek listesi, o klasörde hâlihazırda bulunan dosyalardan oluşturulur. | COMBO | Evet | embeddings klasöründeki tüm dosyalar |

**Not:** Seçilen dosya bir `conditioning` tensörü içermelidir. Dosyada saklanan ek anahtarlar geri yüklenir: numaralı anahtarlar (örneğin `key.0`, `key.1`) sıralı listeler halinde yeniden gruplandırılır ve diğer anahtarlar düz seçenekler olarak geri yüklenir. Ek seçenekler, mevcut olduğunda dosyanın `conditioning_options` meta verisinden okunur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `CONDITIONING` | Dosyadan yüklenen conditioning, geri yüklenen seçeneklerle birlikte. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningLoader/tr.md)

---
**Source fingerprint (SHA-256):** `08fc58bcaa2309fcf03d4e4cc634b930aaf6ccf8097181fd3d45924abda144eb`
