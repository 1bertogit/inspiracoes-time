import json, os, glob, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
insp_dir = os.path.join(ROOT, "inspiracoes")
cards = []

for meta_path in sorted(glob.glob(os.path.join(insp_dir, "*", "meta.json")), reverse=True):
    try:
        m = json.load(open(meta_path))
    except Exception:
        continue
    folder = os.path.basename(os.path.dirname(meta_path))
    base = "inspiracoes/" + folder + "/"
    shot = base + "screenshot.png" if m.get("artefatos", {}).get("screenshot") else ""
    ep_file = os.path.join(os.path.dirname(meta_path), "_editavel_path.txt")
    if os.path.exists(ep_file):
        editavel = base + open(ep_file).read().strip()
    else:
        editavel = base + "editavel.html"
    site_idx = base + "site/"
    titulo = html.escape(m.get("titulo", "") or "")
    nota = html.escape(m.get("nota", "") or "")
    url = html.escape(m.get("url", "") or "")
    data = html.escape(m.get("data", "") or "")
    tags = m.get("tags", []) or []
    tags_html = "".join(f'<span class="tag">{html.escape(t)}</span>' for t in tags)
    search = html.escape((titulo + " " + nota + " " + " ".join(tags)).lower())
    if shot:
        img = f'<img src="{shot}" loading="lazy" alt="">'
    else:
        img = '<div class="noshot">sem screenshot</div>'
    cards.append(f'''<div class="card" data-search="{search}">
      <a href="{editavel}" target="_blank">{img}</a>
      <div class="body">
        <h3>{titulo}</h3>
        <p class="nota">{nota}</p>
        <div class="tags">{tags_html}</div>
        <div class="meta"><span>{data}</span></div>
        <div class="links">
          <a href="{site_idx}" target="_blank">site</a>
          <a href="{editavel}" target="_blank">editavel</a>
          <a href="{url}" target="_blank">original</a>
        </div>
      </div>
    </div>''')

html_out = '''<!DOCTYPE html>
<html lang="pt-br"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Acervo de Inspiracoes</title>
<style>
:root{--bg:#0f1115;--card:#1a1d24;--txt:#e8e8ea;--mut:#9aa0aa;--acc:#4a9eff;--tag:#2a2f3a}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--txt);
font-family:-apple-system,Segoe UI,Roboto,sans-serif}
header{padding:24px 28px;position:sticky;top:0;background:var(--bg);border-bottom:1px solid #23262f;z-index:9}
h1{margin:0 0 12px;font-size:20px}
#busca{width:100%;max-width:420px;padding:10px 14px;border-radius:8px;border:1px solid #2a2f3a;
background:#14171d;color:var(--txt);font-size:14px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px;padding:24px 28px}
.card{background:var(--card);border-radius:12px;overflow:hidden;border:1px solid #23262f;transition:.15s}
.card:hover{transform:translateY(-3px);border-color:#39414f}
.card img,.noshot{width:100%;height:190px;object-fit:cover;object-position:top;display:block;background:#0a0c10}
.noshot{display:flex;align-items:center;justify-content:center;color:var(--mut);font-size:13px}
.body{padding:14px 16px}
h3{margin:0 0 6px;font-size:15px;line-height:1.3}
.nota{margin:0 0 10px;color:var(--mut);font-size:13px;line-height:1.4}
.tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px}
.tag{background:var(--tag);color:#c7ccd6;font-size:11px;padding:3px 8px;border-radius:20px}
.meta{color:#6b7280;font-size:11px;margin-bottom:10px}
.links{display:flex;gap:14px}
.links a{color:var(--acc);font-size:13px;text-decoration:none}
.links a:hover{text-decoration:underline}
.empty{padding:60px 28px;color:var(--mut);text-align:center}
</style></head><body>
<header><h1>Acervo de Inspiracoes <span style="color:var(--mut);font-size:14px">(''' + str(len(cards)) + ''')</span></h1>
<input id="busca" placeholder="buscar por titulo, nota ou tag...">
</header>
<div class="grid" id="grid">
''' + ("\n".join(cards) if cards else '<div class="empty">Nenhuma inspiracao ainda. Rode ./bin/capturar</div>') + '''
</div>
<script>
const b=document.getElementById('busca');
b.addEventListener('input',()=>{const q=b.value.toLowerCase();
document.querySelectorAll('.card').forEach(c=>{
c.style.display=c.dataset.search.includes(q)?'':'none';});});
</script>
</body></html>'''

open(os.path.join(ROOT, "galeria.html"), "w").write(html_out)
print(f"==> galeria.html gerada com {len(cards)} inspiracao(oes)")
