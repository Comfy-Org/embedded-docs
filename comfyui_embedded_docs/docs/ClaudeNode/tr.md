# Anthropic Claude

## Genel Bakış

Bir Anthropic Claude modelinden metin yanıtları oluşturun. Bu düğüm, bir metin istemi ve isteğe bağlı görselleri bir Claude modeline gönderir ve oluşturulan metin yanıtını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `istem` | Modele gönderilecek metin girişi. (varsayılan: boş dize) | STRING | Evet | Yok |
| `model` | Yanıtı oluşturmak için kullanılan Claude modeli. | COMBO | Evet | `"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `tohum` | Tohum, düğümün yeniden çalıştırılıp çalıştırılmayacağını kontrol eder; sonuçlar tohumdan bağımsız olarak deterministik değildir. (varsayılan: 0) | INT | Evet | 0 ile 2147483647 arası |
| `görseller` | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). En fazla 20 görsel. | IMAGE | Hayır | 0 ile 20 görsel arası |
| `sistem_istemi` | Modelin davranışını belirleyen temel talimatlar. (varsayılan: boş dize) | STRING | Hayır | Yok |

### Parametre Kısıtlamaları

- **Görsel Sınırı**: İstek başına en fazla 20 görsel sağlanabilir.
- **Sıcaklık (Temperature) Yönetimi**: Düşünme etkinleştirildiğinde veya "Opus 4.7" modeli kullanıldığında, sıcaklık parametresi Anthropic API'sinin gerektirdiği şekilde otomatik olarak ayarlanmaz (varsayılan olarak 1.0 değerine döner). Diğer modeller için sıcaklık, model yapılandırması aracılığıyla ayarlanabilir.
- **Düşünme/Mantık Yürütme**: Model yapılandırması, düşünmenin etkinleştirilip etkinleştirilmediğini kontrol eden bir `reasoning_effort` ayarı içerir. Etkinleştirildiğinde, düğüm seçilen modele bağlı olarak uygun düşünme modunu (uyarlanabilir veya bütçe tabanlı) otomatik olarak yapılandırır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Claude modelinden oluşturulan metin yanıtı. Hiç metin oluşturulmazsa "Claude modelinden boş yanıt." döndürür. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/tr.md)

---
**Source fingerprint (SHA-256):** `e3bab004535d4d406582aa42f28bb64a2988f8331788d51ec1fa4e943d8d4382`
