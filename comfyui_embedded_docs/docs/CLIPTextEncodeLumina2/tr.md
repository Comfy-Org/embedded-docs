> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/tr.md)

CLIP Text Encode for Lumina2 düğümü, bir sistem istemi ve kullanıcı istemini bir CLIP modeli kullanarak, difüzyon modelini belirli görüntüler oluşturmaya yönlendirmek için kullanılabilecek bir gömme verisine dönüştürür. Önceden tanımlanmış bir sistem istemini özel metin isteminizle birleştirir ve bunları CLIP modeli aracılığıyla işleyerek görüntü oluşturma için koşullandırma verisi yaratır.

## Girdiler

| Parametre | Veri Türü | Girdi Türü | Varsayılan | Aralık | Açıklama |
|-----------|-----------|------------|---------|-------|-------------|
| `sistem_istemi` | STRING | COMBO | - | "superior", "alignment" | Lumina2 iki tür sistem istemi sağlar: Superior: Metin istemleri veya kullanıcı istemlerine dayanarak üstün derecede görüntü-metin uyumuna sahip üstün görüntüler oluşturmak için tasarlanmış bir asistansınız. Alignment: Metin istemlerine dayanarak en yüksek derecede görüntü-metin uyumuna sahip yüksek kaliteli görüntüler oluşturmak için tasarlanmış bir asistansınız. |
| `kullanıcı_istemi` | STRING | STRING | - | - | Kodlanacak metin. |
| `clip` | CLIP | CLIP | - | - | Metni kodlamak için kullanılan CLIP modeli. |

**Not:** `clip` girdisi gereklidir ve None olamaz. Eğer clip girdisi geçersizse, düğüm kontrol noktasının geçerli bir CLIP veya metin kodlayıcı modeli içermeyebileceğini belirten bir hata verecektir.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Difüzyon modelini yönlendirmek için kullanılan gömülü metni içeren bir koşullandırma. |