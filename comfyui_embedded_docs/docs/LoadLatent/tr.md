# GizliYükle

LoadLatent düğümü, giriş dizinindeki .latent dosyalarından önceden kaydedilmiş gizli (latent) temsilleri yükler. Dosyadaki gizli tensör verilerini okur ve gerekli ölçeklendirme ayarlamalarını uygulayarak, gizli verileri diğer düğümlerde kullanılmak üzere döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `gizli` | Giriş dizinindeki mevcut dosyalar arasından hangi .latent dosyasının yükleneceğini seçer | STRING | Evet | Giriş dizinindeki tüm .latent dosyaları |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `LATENT` | Seçilen dosyadan yüklenen gizli temsil verilerini döndürür | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/tr.md)

---
**Source fingerprint (SHA-256):** `020185a6066263b75b2417411f07af54d31a2a3a056d650eacfff188dc2cb87e`
