Bu düğüm, bir OpenAI modelinden metin yanıtları oluşturur. Metin isteminizi (ve isteğe bağlı olarak görselleri veya dosyaları) bir OpenAI modeline gönderir ve oluşturulan metin yanıtını döndürür.

## Girişler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `komut` | Yanıt oluşturmak için modele gönderilen metin girdileri (varsayılan: boş) | STRING | Evet | - |
| `bağlamı_sürdür` | Bu parametre kullanımdan kaldırılmıştır ve herhangi bir etkisi yoktur (varsayılan: False) | BOOLEAN | Evet | - |
| `model` | Yanıtı oluşturmak için kullanılan model | COMBO | Evet | Birden çok OpenAI modeli mevcut |
| `görseller` | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). Birden çok görsel eklemek için Toplu Görseller düğümünü kullanabilirsiniz | IMAGE | Hayır | - |
| `dosyalar` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). OpenAI Sohbet Giriş Dosyaları düğümünden girdi kabul eder | OPENAI_INPUT_FILES | Hayır | - |
| `gelişmiş_seçenekler` | Model için isteğe bağlı yapılandırma. OpenAI Sohbet Gelişmiş Seçenekler düğümünden girdi kabul eder | OPENAI_CHAT_CONFIG | Hayır | - |

## Çıkışlar

| Çıkış Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output_text` | OpenAI modeli tarafından oluşturulan metin yanıtı | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/tr.md)

---
**Source fingerprint (SHA-256):** `ea66b58b23305b0d97bfc76cc39cfdfe8e01b70edcbfd60c2c640a07ad507ee6`
