**Kancaları Birleştir [2]** düğümü, iki kanca grubunu tek bir birleşik kanca grubunda birleştirir. İki isteğe bağlı kanca girişi alır ve ComfyUI'nin kanca birleştirme işlevini kullanarak bunları birleştirir. Bu, işlemleri kolaylaştırmak için birden çok kanca yapılandırmasını tek bir noktada toplamanıza olanak tanır.

## Girişler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `hooks_A` | Birleştirilecek ilk kanca grubu | HOOKS | Hayır | - |
| `hooks_B` | Birleştirilecek ikinci kanca grubu | HOOKS | Hayır | - |

**Not:** Her iki giriş de isteğe bağlıdır, ancak düğümün çalışması için en az bir kanca grubu sağlanmalıdır. Yalnızca bir kanca grubu sağlanırsa, bu grup değiştirilmeden döndürülür.

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `hooks` | Her iki giriş grubundaki tüm kancaları içeren birleşik kanca grubu | HOOKS |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks/tr.md)

---
**Source fingerprint (SHA-256):** `558ceef1cebedd0b7e045b7d1eb1afa4316ea6a3c35f982968af132dca164126`
