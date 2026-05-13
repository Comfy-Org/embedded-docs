> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/tr.md)

Bu düğüm, bir OpenAI modelinden metin yanıtları oluşturur. Metin isteminizi (ve isteğe bağlı olarak görselleri veya dosyaları) bir OpenAI modeline gönderir ve oluşturulan metin yanıtını döndürür.

## Girişler

| Parametre | Veri Türü | Zorunlu | Aralık | Açıklama |
|-----------|-----------|----------|-------|-------------|
| `komut` | STRING | Evet | - | Yanıt oluşturmak için modele gönderilen metin girdileri (varsayılan: boş) |
| `bağlamı_sürdür` | BOOLEAN | Evet | - | Bu parametre kullanımdan kaldırılmıştır ve herhangi bir etkisi yoktur (varsayılan: False) |
| `model` | COMBO | Evet | Birden çok OpenAI modeli mevcut | Yanıtı oluşturmak için kullanılan model |
| `görseller` | IMAGE | Hayır | - | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). Birden çok görsel eklemek için Toplu Görseller düğümünü kullanabilirsiniz |
| `dosyalar` | OPENAI_INPUT_FILES | Hayır | - | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). OpenAI Sohbet Giriş Dosyaları düğümünden girdi kabul eder |
| `gelişmiş_seçenekler` | OPENAI_CHAT_CONFIG | Hayır | - | Model için isteğe bağlı yapılandırma. OpenAI Sohbet Gelişmiş Seçenekler düğümünden girdi kabul eder |

## Çıkışlar

| Çıkış Adı | Veri Türü | Açıklama |
|-----------|-----------|-------------|
| `output_text` | STRING | OpenAI modeli tarafından oluşturulan metin yanıtı |

---
**Source fingerprint (SHA-256):** `ea66b58b23305b0d97bfc76cc39cfdfe8e01b70edcbfd60c2c640a07ad507ee6`
