# QuadrupleClipLoader

הצומת Quadruple CLIP Loader (QuadrupleCLIPLoader) הוא אחד מצמתי הליבה של ComfyUI, שנוסף לראשונה כדי לתמוך במודל HiDream I1. אם הצומת הזה חסר, נסו לעדכן את ComfyUI לגרסה העדכנית ביותר כדי להבטיח תמיכה בצומת.

הוא דורש 4 מודלים של CLIP, המתאימים לפרמטרים `clip_name1`, `clip_name2`, `clip_name3` ו-`clip_name4`, ויספק פלט של מודל CLIP לצמתים עוקבים.

צומת זה יזהה מודלים הממוקמים בתיקייה `ComfyUI/models/text_encoders`,
 וכן יקרא מודלים מנתיבים נוספים המוגדרים בקובץ extra_model_paths.yaml.
 לפעמים, לאחר הוספת מודלים, ייתכן שתצטרכו **לטעון מחדש את ממשק ComfyUI** כדי לאפשר לו לקרוא את קובצי המודל בתיקייה המתאימה.

> מסמך זה נוצר על ידי בינה מלאכותית. אם מצאתם שגיאות או שיש לכם הצעות לשיפור, אתם מוזמנים לתרום! [עריכה ב-GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuadrupleClipLoader/he.md)
