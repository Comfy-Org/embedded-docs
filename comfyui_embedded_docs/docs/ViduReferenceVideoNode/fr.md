> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/fr.md)

Le nœud Vidu Reference Video génère des vidéos à partir de plusieurs images de référence et d'une description textuelle. Il utilise des modèles d'IA pour créer un contenu vidéo cohérent basé sur les images fournies et la description. Le nœud prend en charge divers paramètres vidéo incluant la durée, le format d'image, la résolution et le contrôle du mouvement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | `"vidu_q1"`<br>`"vidu_q2"`<br>`"vidu_q3"`<br>`"vidu_q4"`<br>`"vidu_q5"`<br>`"vidu_q6"`<br>`"vidu_q7"`<br>`"vidu_q8"`<br>`"vidu_q9"`<br>`"vidu_q10"`<br>`"vidu_q11"`<br>`"vidu_q12"`<br>`"vidu_q13"`<br>`"vidu_q14"`<br>`"vidu_q15"`<br>`"vidu_q16"`<br>`"vidu_q17"`<br>`"vidu_q18"`<br>`"vidu_q19"`<br>`"vidu_q20"`<br>`"vidu_q21"`<br>`"vidu_q22"`<br>`"vidu_q23"`<br>`"vidu_q24"`<br>`"vidu_q25"`<br>`"vidu_q26"`<br>`"vidu_q27"`<br>`"vidu_q28"`<br>`"vidu_q29"`<br>`"vidu_q30"`<br>`"vidu_q31"`<br>`"vidu_q32"`<br>`"vidu_q33"`<br>`"vidu_q34"`<br>`"vidu_q35"`<br>`"vidu_q36"`<br>`"vidu_q37"`<br>`"vidu_q38"`<br>`"vidu_q39"`<br>`"vidu_q40"`<br>`"vidu_q41"`<br>`"vidu_q42"`<br>`"vidu_q43"`<br>`"vidu_q44"`<br>`"vidu_q45"`<br>`"vidu_q46"`<br>`"vidu_q47"`<br>`"vidu_q48"`<br>`"vidu_q49"`<br>`"vidu_q50"`<br>`"vidu_q51"`<br>`"vidu_q52"`<br>`"vidu_q53"`<br>`"vidu_q54"`<br>`"vidu_q55"`<br>`"vidu_q56"`<br>`"vidu_q57"`<br>`"vidu_q58"`<br>`"vidu_q59"`<br>`"vidu_q60"`<br>`"vidu_q61"`<br>`"vidu_q62"`<br>`"vidu_q63"`<br>`"vidu_q64"`<br>`"vidu_q65"`<br>`"vidu_q66"`<br>`"vidu_q67"`<br>`"vidu_q68"`<br>`"vidu_q69"`<br>`"vidu_q70"`<br>`"vidu_q71"`<br>`"vidu_q72"`<br>`"vidu_q73"`<br>`"vidu_q74"`<br>`"vidu_q75"`<br>`"vidu_q76"`<br>`"vidu_q77"`<br>`"vidu_q78"`<br>`"vidu_q79"`<br>`"vidu_q80"`<br>`"vidu_q81"`<br>`"vidu_q82"`<br>`"vidu_q83"`<br>`"vidu_q84"`<br>`"vidu_q85"`<br>`"vidu_q86"`<br>`"vidu_q87"`<br>`"vidu_q88"`<br>`"vidu_q89"`<br>`"vidu_q90"`<br>`"vidu_q91"`<br>`"vidu_q92"`<br>`"vidu_q93"`<br>`"vidu_q94"`<br>`"vidu_q95"`<br>`"vidu_q96"`<br>`"vidu_q97"`<br>`"vidu_q98"`<br>`"vidu_q99"`<br>`"vidu_q100"` | Nom du modèle pour la génération vidéo (par défaut : "vidu_q1") |
| `images` | IMAGE | Oui | - | Images à utiliser comme références pour générer une vidéo avec des sujets cohérents (maximum 7 images) |
| `prompt` | STRING | Oui | - | Description textuelle pour la génération vidéo |
| `duration` | INT | Non | 5-5 | Durée de la vidéo de sortie en secondes (par défaut : 5) |
| `seed` | INT | Non | 0-2147483647 | Graine pour la génération vidéo (0 pour aléatoire) (par défaut : 0) |
| `aspect_ratio` | COMBO | Non | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` | Le format d'image de la vidéo de sortie (par défaut : "16:9") |
| `resolution` | COMBO | Non | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"1440p"`<br>`"2160p"` | Les valeurs prises en charge peuvent varier selon le modèle et la durée (par défaut : "1080p") |
| `movement_amplitude` | COMBO | Non | `"auto"`<br>`"low"`<br>`"medium"`<br>`"high"` | L'amplitude du mouvement des objets dans le cadre (par défaut : "auto") |

**Contraintes et limitations :**

- Le champ `prompt` est requis et ne peut pas être vide
- Maximum de 7 images autorisées pour référence
- Chaque image doit avoir un format d'image compris entre 1:4 et 4:1
- Chaque image doit avoir des dimensions minimales de 128x128 pixels
- La durée est fixée à 5 secondes

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée basée sur les images de référence et la description |
