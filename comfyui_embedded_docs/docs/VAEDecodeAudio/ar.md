# فك ترميز VAE للصوت

This node converts an audio latent representation back into a playable audio waveform using a Variational Autoencoder (VAE). It takes the encoded samples, decodes them through the selected VAE, and then normalizes the resulting waveform so the overall volume level stays consistent. The output audio uses the VAE's audio sample rate (44100 Hz by default), or the sample rate stored in the input samples when one is present.

## المدخلات

| المعامل | الوصف | نوع البيانات | مطلوب | النطاق |
|-----------|-------------|-----------|----------|-------|
| `samples` | العينات الصوتية المُشفَّرة في الفضاء الكامن والتي سيُعاد فك تشفيرها إلى موجة صوتية. إذا كانت العينات تحمل معدل عينات خاصًا بها، فسيُستخدم هذا القيمة للمخرجات. | LATENT | نعم | - |
| `vae` | نموذج المُشفِّر التلقائي التبايني المستخدم لفك تشفير العينات الكامنة إلى صوت. يحدد معدل عينات خرج الصوت الخاص به (44100 هرتز افتراضيًا) معدل عينات الموجة الناتجة عندما لا تحدد العينات المدخلة معدلًا. | VAE | نعم | - |

## المخرجات

| اسم المخرَج | الوصف | نوع البيانات |
|-------------|-------------|-----------|
| `AUDIO` | موجة الصوت المفكوكة التشفير مع مستوى صوت مُطبَّع، وتُعاد مع معدل العينات الخاص بها (معدل العينات من `samples` المدخلة إن وُجد، وإلا معدل عينات الصوت في VAE، والافتراضي 44100 هرتز). | AUDIO |

> تم إنشاء هذه الوثيقة بواسطة الذكاء الاصطناعي. إذا وجدت أي أخطاء أو لديك اقتراحات للتحسين، فلا تتردد في المساهمة! [تحرير على GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/ar.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`
