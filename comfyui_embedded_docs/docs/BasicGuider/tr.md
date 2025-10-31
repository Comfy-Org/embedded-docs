> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/tr.md)

BasicGuider düğümü, örnekleme süreci için basit bir kılavuzluk mekanizması oluşturur. Bir model ve koşullandırma verisini girdi olarak alır ve örnekleme sırasında üretim sürecini yönlendirmek için kullanılabilecek bir kılavuz nesnesi üretir. Bu düğüm, kontrollü üretim için gerekli temel kılavuzluk işlevselliğini sağlar.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | gerekli | - | - | Kılavuzluk için kullanılacak model |
| `conditioning` | CONDITIONING | gerekli | - | - | Üretim sürecine kılavuzluk eden koşullandırma verisi |

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | Örnekleme sürecinde üretimi yönlendirmek için kullanılabilecek bir kılavuz nesnesi |