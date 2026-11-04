# ByteDance Texte vers Vidéo

Le nœud ByteDance Text to Video génère une vidéo à l'aide des modèles ByteDance via une API, à partir d'une invite de texte. Vous fournissez une invite et choisissez des paramètres tels que le modèle, la résolution, le format d'image et la durée ; le nœud soumet la demande de génération et renvoie la vidéo générée.

**Remarque:** BytePlus arrête le modèle Seedance 1.5 Pro le 11 novembre 2026 : ce nœud ne le propose donc plus et les workflows enregistrés avec lui cessent de fonctionner. Utilisez plutôt `seedance-1-0-pro-250528`, `seedance-1-0-pro-fast-251015` ou le [nœud partenaire Seedance 2.5](https://docs.comfy.org/fr/tutorials/partner-nodes/bytedance/seedance-2-5).

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle ByteDance utilisé pour générer la vidéo (défaut : `"seedance-1-0-pro-fast-251015"`). | COMBO | Oui | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | L'invite de texte utilisée pour générer la vidéo. | STRING | Oui | - |
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | Le rapport d'aspect de la vidéo de sortie. | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | La durée de la vidéo de sortie en secondes (défaut : 5). | INT | Oui | 3 à 12 |
| `seed` | Graine (seed) à utiliser pour la génération (défaut : 0). | INT | Non | 0 à 2147483647 |
| `camera_fixed` | Spécifie si la caméra doit être fixe. La plateforme ajoute une instruction pour fixer la caméra à votre invite, mais ne garantit pas l'effet réel (défaut : False). | BOOLEAN | Non | - |
| `filigrane` | Indique s'il faut ajouter un filigrane « généré par IA » à la vidéo (défaut : False). | BOOLEAN | Non | - |
| `générer_audio` | Ajoute une piste audio générée par IA. Les modèles restants ignorent cette entrée (défaut : False). | BOOLEAN | Non | - |

**Contraintes des paramètres :**

- Le paramètre `prompt` doit contenir au moins 1 caractère après suppression des espaces blancs.
- Le paramètre `prompt` ne peut pas contenir les paramètres de texte suivants : « resolution », « ratio », « duration », « seed », « camerafixed », « watermark ».
- Le nœud construit l'invite finale en ajoutant les paramètres sélectionnés `resolution`, `aspect_ratio`, `duration`, `seed`, `camera_fixed` et `watermark` au texte de l'invite.
- Le paramètre `duration` est limité à des valeurs comprises entre 3 et 12 secondes.
- Le paramètre `seed` accepte des valeurs de 0 à 2 147 483 647.
- Le paramètre `generate_audio` est conservé pour compatibilité, mais les modèles restants l'ignorent.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `83b805b63e59a76cae378b0407b409e1bfe900677ef1e01fc836fede47283eee`
