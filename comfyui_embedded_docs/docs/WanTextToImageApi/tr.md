# Wan Metinden Görsele

Wan Text to Image düğümü, metin açıklamalarına dayalı görseller üretir. Yazılı istemlerden görsel içerik oluşturmak için yapay zekâ modellerini kullanır ve hem İngilizce hem de Çince metin girişini destekler. Düğüm, çıktı görüntüsünün boyutunu, kalitesini ve stil tercihlerini ayarlamak için çeşitli kontroller sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak model (varsayılan: "wan2.5-t2i-preview") | STRING | Evet | "wan2.5-t2i-preview" |
| `prompt` | Öğeleri ve görsel özellikleri tanımlayan istem. İngilizce ve Çinceyi destekler (varsayılan: boş) | STRING | Evet | - |
| `negative_prompt` | Kaçınılması gerekenleri tanımlayan negatif istem (varsayılan: boş) | STRING | Hayır | - |
| `width` | Piksel cinsinden görüntü genişliği (varsayılan: 1024, adım: 32) | INT | Hayır | 768-1440 |
| `height` | Piksel cinsinden görüntü yüksekliği (varsayılan: 1024, adım: 32) | INT | Hayır | 768-1440 |
| `seed` | Üretim için kullanılacak tohum (varsayılan: 0) | INT | Hayır | 0-2147483647 |
| `prompt_extend` | İstemin yapay zekâ yardımıyla iyileştirilip iyileştirilmeyeceği (varsayılan: True) | BOOLEAN | Hayır | - |
| `watermark` | Sonuca yapay zekâ tarafından oluşturulmuş bir filigran eklenip eklenmeyeceği (varsayılan: False) | BOOLEAN | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Metin istemine dayalı olarak üretilen görüntü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/tr.md)

---
**Source fingerprint (SHA-256):** `208b7c839da45316aeb1a14a3e9d176eeb09b2f931f764fb8a296da15ae3bd4e`
