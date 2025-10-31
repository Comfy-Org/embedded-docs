> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/tr.md)

TripleCLIPLoader düğümü, üç farklı metin kodlayıcı modelini aynı anda yükler ve bunları tek bir CLIP modelinde birleştirir. Bu, clip-l, clip-g ve t5 modellerinin birlikte çalışmasını gerektiren SD3 iş akışları gibi, birden fazla metin kodlayıcının gerekli olduğu gelişmiş metin kodlama senaryolarında kullanışlıdır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip_name1` | STRING | Evet | Birden fazla seçenek mevcut | Mevcut metin kodlayıcılar arasından yüklenecek ilk metin kodlayıcı modeli |
| `clip_name2` | STRING | Evet | Birden fazla seçenek mevcut | Mevcut metin kodlayıcılar arasından yüklenecek ikinci metin kodlayıcı modeli |
| `clip_name3` | STRING | Evet | Birden fazla seçenek mevcut | Mevcut metin kodlayıcılar arasından yüklenecek üçüncü metin kodlayıcı modeli |

**Not:** Üç metin kodlayıcı parametresinin de sisteminizde mevcut olan metin kodlayıcı modelleri arasından seçilmesi gerekir. Düğüm, her üç modeli de yükleyecek ve işleme için bunları tek bir CLIP modelinde birleştirecektir.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Yüklenen her üç metin kodlayıcıyı da içeren birleşik bir CLIP modeli |