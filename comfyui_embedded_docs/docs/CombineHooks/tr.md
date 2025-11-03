> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks/tr.md)

**## Genel Bakış**

Combine Hooks [2] düğümü, iki kanca grubunu tek bir birleşik kanca grubunda birleştirir. İki isteğe bağlı kanca girişi alır ve bunları ComfyUI'nin kanca birleştirme işlevselliğini kullanarak birleştirir. Bu, birden fazla kanca yapılandırmasını, süreçleri daha verimli hale getirmek için birleştirmenize olanak tanır.

## ## Girdiler

| Parametre | Veri Türü | Giriş Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `hooks_A` | HOOKS | İsteğe Bağlı | Yok | - | Birleştirilecek ilk kanca grubu |
| `hooks_B` | HOOKS | İsteğe Bağlı | Yok | - | Birleştirilecek ikinci kanca grubu |

**Not:** Her iki giriş de isteğe bağlıdır, ancak düğümün çalışması için en az bir kanca grubu sağlanmalıdır. Eğer sadece bir kanca grubu sağlanırsa, bu grup değiştirilmeden döndürülür.

## ## Çıktılar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `hooks` | HOOKS | Her iki giriş grubundaki tüm kancaları içeren birleşik kanca grubu |