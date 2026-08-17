# Temel Rehber

The BasicGuider node creates a simple guidance mechanism for the sampling process. It takes a model and conditioning data as inputs and produces a guider object that can be used to guide the generation process during sampling. This node provides the fundamental guidance functionality needed for controlled generation.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Rehberlik için kullanılacak model | MODEL | Evet | - |
| `conditioning` | Üretim sürecini yönlendiren koşullandırma verileri | CONDITIONING | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `GUIDER` | Örnekleme sürecinde üretimi yönlendirmek için kullanılabilen bir guider nesnesi | GUIDER |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/tr.md)

---
**Source fingerprint (SHA-256):** `8ea6b56be58ae99baaf13a04c4fadbf8ad921801d8f2ce2aecce768cc34a3b20`
