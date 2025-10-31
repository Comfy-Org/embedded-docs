> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/tr.md)

LoadLatent düğümü, giriş dizinindeki .latent dosyalarından önceden kaydedilmiş gizli temsilleri yükler. Dosyadan gizli tensör verilerini okur ve diğer düğümlerde kullanılmak üzere gizli verileri döndürmeden önce gerekli ölçeklendirme ayarlamalarını uygular.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `latent` | STRING | Evet | Giriş dizinindeki tüm .latent dosyaları | Giriş dizinindeki mevcut dosyalardan hangi .latent dosyasının yükleneceğini seçer |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Seçilen dosyadan yüklenen gizli temsil verilerini döndürür |