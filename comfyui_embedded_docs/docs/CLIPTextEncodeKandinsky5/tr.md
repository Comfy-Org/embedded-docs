> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/tr.md)

CLIPTextEncodeKandinsky5 düğümü, Kandinsky 5 modeliyle kullanılmak üzere metin istemlerini hazırlar. Sağlanan bir CLIP modelini kullanarak iki ayrı metin girişini alır, bunları token'larına ayırır ve tek bir koşullandırma çıktısında birleştirir. Bu çıktı, görüntü oluşturma sürecini yönlendirmek için kullanılır.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Evet | | Metin istemlerini token'larına ayırmak ve kodlamak için kullanılan CLIP modeli. |
| `clip_l` | STRING | Evet | | Birincil metin istemi. Bu giriş, çok satırlı metni ve dinamik istemleri destekler. |
| `qwen25_7b` | STRING | Evet | | İkincil bir metin istemi. Bu giriş, çok satırlı metni ve dinamik istemleri destekler. |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Her iki metin isteminden oluşturulan birleşik koşullandırma verisi, görüntü oluşturma için bir Kandinsky 5 modeline beslenmeye hazır. |
