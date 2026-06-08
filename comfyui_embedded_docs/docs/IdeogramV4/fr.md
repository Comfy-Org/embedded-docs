Voici la traduction en français de la documentation du nœud ComfyUI « Ideogram V4 », conforme à vos règles :

# Ideogram V4

Génère des images à l'aide du modèle Ideogram 4.0 à partir d'une invite textuelle. Ce nœud envoie votre description textuelle à l'API Ideogram et retourne l'image générée sous forme de tenseur de sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `invite` | Invite textuelle pour la génération de l'image. | STRING | Oui | Aucune restriction |
| `résolution` | Résolution de l'image générée. Par défaut : "Auto" laisse le modèle choisir la meilleure résolution. | COMBO | Oui | `"Auto"`<br>`"2048x2048 (1:1)"`<br>`"1440x2880 (1:2)"`<br>`"2880x1440 (2:1)"`<br>`"1664x2496 (2:3)"`<br>`"2496x1664 (3:2)"`<br>`"1792x2240 (4:5)"`<br>`"2240x1792 (5:4)"`<br>`"1440x2560 (9:16)"`<br>`"2560x1440 (16:9)"`<br>`"1600x2560 (5:8)"`<br>`"2560x1600 (8:5)"`<br>`"1728x2304 (3:4)"`<br>`"2304x1728 (4:3)"`<br>`"1296x3168 (9:22)"`<br>`"3168x1296 (22:9)"`<br>`"1152x2944 (9:23)"`<br>`"2944x1152 (23:9)"`<br>`"1248x3328 (3:8)"`<br>`"3328x1248 (8:3)"`<br>`"1280x3072 (5:12)"`<br>`"3072x1280 (12:5)"` |
| `vitesse_de_rendu` | Contrôle le compromis entre la vitesse de génération et la qualité. Par défaut : "DEFAULT". | COMBO | Oui | `"DEFAULT"`<br>`"TURBO"`<br>`"QUALITY"` |
| `graine` | Graine pour une génération reproductible. Par défaut : 0. | INT | Oui | Min : 0<br>Max : 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image générée sous forme de tenseur. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV4/fr.md)

---
**Source fingerprint (SHA-256):** `47a486824211d34b9109c5038b0b094d192c4e243c0a6c4ceab13af3bdabe6e4`
