> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/tr.md)

**DisableNoise** düğümü, örnekleme işlemlerinde gürültü oluşturmayı devre dışı bırakmak için kullanılabilecek boş bir gürültü yapılandırması sağlar. İçinde hiçbir gürültü verisi bulunmayan özel bir gürültü nesnesi döndürerek, bu çıkışa bağlandığında diğer düğümlerin gürültü ile ilgili işlemleri atlamasına olanak tanır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| *Giriş parametresi yok* | - | - | - | Bu düğüm herhangi bir giriş parametresi gerektirmez. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `NOISE` | NOISE | Örnekleme işlemlerinde gürültü oluşturmayı devre dışı bırakmak için kullanılabilecek boş bir gürültü yapılandırması döndürür. |