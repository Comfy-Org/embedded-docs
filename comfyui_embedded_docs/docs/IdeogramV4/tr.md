# Ideogram V4

Bir metin isteminden Ideogram 4.0 modelini kullanarak görseller üretir. Bu düğüm, metin açıklamanızı Ideogram API'sine gönderir ve üretilen görseli çıktı tensörü olarak döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|----------|-----------|---------|-------|
| `istem` | Görsel üretimi için metin istemi. | STRING | Evet | Kısıtlama yok |
| `çözünürlük` | Üretilen görselin çözünürlüğü. Varsayılan: "Auto" (modelin en iyi çözünürlüğü seçmesini sağlar). | COMBO | Evet | `"Auto"`<br>`"2048x2048 (1:1)"`<br>`"1440x2880 (1:2)"`<br>`"2880x1440 (2:1)"`<br>`"1664x2496 (2:3)"`<br>`"2496x1664 (3:2)"`<br>`"1792x2240 (4:5)"`<br>`"2240x1792 (5:4)"`<br>`"1440x2560 (9:16)"`<br>`"2560x1440 (16:9)"`<br>`"1600x2560 (5:8)"`<br>`"2560x1600 (8:5)"`<br>`"1728x2304 (3:4)"`<br>`"2304x1728 (4:3)"`<br>`"1296x3168 (9:22)"`<br>`"3168x1296 (22:9)"`<br>`"1152x2944 (9:23)"`<br>`"2944x1152 (23:9)"`<br>`"1248x3328 (3:8)"`<br>`"3328x1248 (8:3)"`<br>`"1280x3072 (5:12)"`<br>`"3072x1280 (12:5)"` |
| `oluşturma_hızı` | Üretim hızı ve kalite arasındaki dengeyi kontrol eder. Varsayılan: "DEFAULT". | COMBO | Evet | `"DEFAULT"`<br>`"TURBO"`<br>`"QUALITY"` |
| `seed` | Tekrarlanabilir üretim için tohum değeri. Varsayılan: 0. | INT | Evet | Min: 0<br>Maks: 2147483647 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `IMAGE` | Tensör olarak üretilen görsel. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV4/tr.md)

---
**Source fingerprint (SHA-256):** `47a486824211d34b9109c5038b0b094d192c4e243c0a6c4ceab13af3bdabe6e4`
