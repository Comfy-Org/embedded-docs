# PixVerse V6 Texte en vidéo

PixVerse V6 Text to Video génère une vidéo à partir d'une invite textuelle en utilisant le modèle V6 de PixVerse. Le nœud envoie l'invite ainsi que la résolution, la durée, le format d'image et d'autres paramètres choisis à PixVerse, attend la fin de la génération, puis renvoie la vidéo obtenue — y compris une piste audio native lorsque la génération audio est activée.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Paramètres du modèle et de génération. Sélectionnez le modèle et configurez ses options de génération. | DYNAMIC_COMBO | Oui | "PixVerse V6" |

### Entrées PixVerse V6

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite pour la génération vidéo. (défaut : "") | STRING | Oui | 1–5000 caractères |
| `aspect_ratio` | Format d'image de sortie. Sélectionnez l'un des formats d'image pris en charge par PixVerse V6. | COMBO | Oui | Plusieurs options disponibles |
| `quality` | Résolution de sortie. Définit le bord long : 360p correspond à 640px, 540p à 1024px, 720p à 1280px, 1080p à 1920px. (défaut : « 720p ») | COMBO | Oui | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Durée de la vidéo générée en secondes. (défaut : 5) | INT | Oui | 1–15 |
| `generate_audio` | Générer une piste audio native en même temps que la vidéo. (défaut : True) | BOOLEAN | Oui | True<br>False |
| `multi_clip` | Laisse le modèle découper la vidéo en plusieurs plans au lieu d'une seule prise continue. (défaut : False) | BOOLEAN | Oui | True<br>False |
| `seed` | Seed pour la génération vidéo. PixVerse l'enregistre mais ne reproduit pas un tirage à partir de celui-ci. Prend en charge la randomisation après génération. (défaut : 42) | INT | Oui | 0–2147483647 |
| `negative_prompt` | Une description textuelle facultative des éléments indésirables dans la vidéo. (défaut : "") | STRING | Non | 0–2048 caractères |
| `style` | Un style visuel facultatif appliqué à l'ensemble de la vidéo. (défaut : « none ») | COMBO | Non | Plusieurs options disponibles |

**Remarque :** Le paramètre `prompt` est obligatoire et, après suppression des espaces en début et fin de chaîne, ne doit pas être vide ; sa longueur maximale est de 5000 caractères. Le paramètre `negative_prompt` est limité à 2048 caractères. Définir `style` sur « none » (la valeur par défaut) signifie qu'aucun style visuel n'est appliqué. Le paramètre `seed` est enregistré par PixVerse mais ne peut pas être utilisé pour reproduire la même génération. Le nœud attend que PixVerse termine la génération de la vidéo puis la télécharge ; si la requête échoue — par exemple parce que PixVerse a déjà atteint son nombre maximal de générations simultanées, que le compte du fournisseur est à court de crédits ou que la modération du contenu rejette l'invite — le nœud renvoie une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée. Si `generate_audio` est activé, la vidéo inclut la piste audio native. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `4c268be9720a4606e77a9347570ac26b489625fc6b9528b9d3cceb4497d8683b`
