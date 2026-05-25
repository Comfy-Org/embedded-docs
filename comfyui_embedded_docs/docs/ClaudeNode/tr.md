> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/tr.md)

## Genel Bakış

Bir Anthropic Claude modelinden metin yanıtları oluşturun. Bu düğüm, bir metin istemi ve isteğe bağlı görselleri bir Claude modeline gönderir ve oluşturulan metin yanıtını döndürür.

## Girdiler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `istem` | STRING | Evet | Yok | Modele gönderilecek metin girişi. (varsayılan: boş dize) |
| `model` | COMBO | Evet | `"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` | Yanıtı oluşturmak için kullanılan Claude modeli. |
| `tohum` | INT | Evet | 0 ile 2147483647 arası | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) |
| `görseller` | IMAGE | Hayır | 0 ile 20 görsel arası | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). En fazla 20 görsel. |
| `sistem_istemi` | STRING | Hayır | Yok | Modelin davranışını belirleyen temel talimatlar. (varsayılan: boş dize) |

### Parametre Kısıtlamaları

- **Görsel Sınırı**: İstek başına en fazla 20 görsel sağlanabilir.
- **Sıcaklık (Temperature) Yönetimi**: Düşünme etkinleştirildiğinde veya "Opus 4.7" modeli kullanıldığında, sıcaklık parametresi Anthropic API'sinin gerektirdiği şekilde otomatik olarak ayarlanmaz (varsayılan olarak 1.0 değerine döner). Diğer modeller için sıcaklık, model yapılandırması aracılığıyla ayarlanabilir.
- **Düşünme/Mantık Yürütme**: Model yapılandırması, düşünmenin etkinleştirilip etkinleştirilmediğini kontrol eden bir `reasoning_effort` ayarı içerir. Etkinleştirildiğinde, düğüm seçilen modele bağlı olarak uygun düşünme modunu (uyarlanabilir veya bütçe tabanlı) otomatik olarak yapılandırır.

## Çıktılar

| Çıktı Adı | Veri Türü | Açıklama |
|-------------|-----------|-------------|
| `output` | STRING | Claude modelinden oluşturulan metin yanıtı. Hiç metin oluşturulmazsa "Claude modelinden boş yanıt." döndürür. |

---
**Source fingerprint (SHA-256):** `e3bab004535d4d406582aa42f28bb64a2988f8331788d51ec1fa4e943d8d4382`
