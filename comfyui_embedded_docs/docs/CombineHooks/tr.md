> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks/tr.md)

**Kancaları Birleştir [2]** düğümü, iki kanca grubunu tek bir birleşik kanca grubunda birleştirir. İki isteğe bağlı kanca girişi alır ve ComfyUI'nin kanca birleştirme işlevini kullanarak bunları birleştirir. Bu, işlemleri kolaylaştırmak için birden çok kanca yapılandırmasını tek bir noktada toplamanıza olanak tanır.

## Girişler

| Parametre | Veri Türü | Gerekli | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `hooks_A` | HOOKS | Hayır | - | Birleştirilecek ilk kanca grubu |
| `hooks_B` | HOOKS | Hayır | - | Birleştirilecek ikinci kanca grubu |

**Not:** Her iki giriş de isteğe bağlıdır, ancak düğümün çalışması için en az bir kanca grubu sağlanmalıdır. Yalnızca bir kanca grubu sağlanırsa, bu grup değiştirilmeden döndürülür.

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `hooks` | HOOKS | Her iki giriş grubundaki tüm kancaları içeren birleşik kanca grubu |

---
**Source fingerprint (SHA-256):** `558ceef1cebedd0b7e045b7d1eb1afa4316ea6a3c35f982968af132dca164126`
