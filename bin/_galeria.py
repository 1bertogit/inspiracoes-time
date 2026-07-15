import json, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
insp_dir = os.path.join(ROOT, "inspiracoes")

itens = []
avisos = []

for meta_path in sorted(glob.glob(os.path.join(insp_dir, "*", "meta.json")), reverse=True):
    try:
        m = json.load(open(meta_path))
    except Exception as e:
        avisos.append("meta invalido: " + meta_path + " (" + str(e) + ")")
        continue

    folder = os.path.basename(os.path.dirname(meta_path))
    base = "inspiracoes/" + folder + "/"

    tem_shot = bool(m.get("artefatos", {}).get("screenshot"))
    shot = base + "screenshot.png" if tem_shot else ""

    ep_file = os.path.join(os.path.dirname(meta_path), "_editavel_path.txt")
    if os.path.exists(ep_file):
        editavel = base + open(ep_file).read().strip()
    else:
        editavel = base + "editavel.html"

    site_idx = base + "site/"

    # validacao de referencias (avisa, nao quebra)
    for rotulo, rel in (("screenshot", shot), ("editavel", editavel)):
        if rel and not os.path.exists(os.path.join(ROOT, rel)):
            avisos.append("referencia quebrada [" + rotulo + "]: " + rel)

    itens.append({
        "slug": folder,
        "titulo": m.get("titulo", "") or "",
        "nota": m.get("nota", "") or "",
        "tags": m.get("tags", []) or [],
        "data": m.get("data", "") or "",
        "url": m.get("url", "") or "",
        "screenshot": shot,
        "site": site_idx,
        "editavel": editavel,
    })

dados = {"gerado_em": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
         "total": len(itens),
         "itens": itens}

with open(os.path.join(ROOT, "dados.json"), "w") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)

print("==> dados.json gerado com " + str(len(itens)) + " inspiracao(oes)")
for a in avisos:
    print("   [aviso] " + a)
