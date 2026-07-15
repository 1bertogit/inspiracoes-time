let ITENS = [];
let tagAtiva = "";
const grid = document.getElementById("grid");
const busca = document.getElementById("busca");
const ordenar = document.getElementById("ordenar");
const filtros = document.getElementById("filtros");
const contador = document.getElementById("contador");

function esc(s){
  return String(s || "").replace(/[&<>"']/g, c =>
    ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
}

function texto(it){
  return (it.titulo + " " + it.nota + " " + (it.tags||[]).join(" ")).toLowerCase();
}

function render(){
  const q = busca.value.toLowerCase().trim();
  let lista = ITENS.filter(it => texto(it).includes(q));
  if (tagAtiva) lista = lista.filter(it => (it.tags||[]).includes(tagAtiva));

  if (ordenar.value === "az")
    lista.sort((a,b)=> (a.titulo||"").localeCompare(b.titulo||""));
  else
    lista.sort((a,b)=> (b.data||"").localeCompare(a.data||""));

  contador.textContent = "(" + lista.length + ")";

  if (!lista.length){
    grid.innerHTML = '<div class="empty">Nenhuma inspiracao encontrada.</div>';
    return;
  }

  grid.innerHTML = lista.map(it => {
    const img = it.screenshot
      ? '<img src="'+esc(it.screenshot)+'" loading="lazy" alt="">'
      : '<div class="noshot">sem screenshot</div>';
    const tags = (it.tags||[]).map(t =>
      '<span class="tag" data-tag="'+esc(t)+'">'+esc(t)+'</span>').join("");
    return '<div class="card">'
      + '<a href="'+esc(it.editavel)+'" target="_blank">'+img+'</a>'
      + '<div class="body">'
      + '<h3>'+esc(it.titulo)+'</h3>'
      + '<p class="nota">'+esc(it.nota)+'</p>'
      + '<div class="tags">'+tags+'</div>'
      + '<div class="meta"><span>'+esc(it.data)+'</span></div>'
      + '<div class="links">'
      + '<a href="'+esc(it.site)+'" target="_blank">site</a>'
      + '<a href="'+esc(it.editavel)+'" target="_blank">editavel</a>'
      + '<a href="'+esc(it.url)+'" target="_blank">original</a>'
      + '</div></div></div>';
  }).join("");
}

function montarFiltros(){
  const todas = [...new Set(ITENS.flatMap(it => it.tags||[]))].sort();
  filtros.innerHTML =
    todas.map(t => '<span class="chip" data-tag="'+esc(t)+'">'+esc(t)+'</span>').join("")
    + '<button id="limpar">limpar filtro</button>';
}

function aplicarTag(t){
  tagAtiva = (tagAtiva === t) ? "" : t;
  document.querySelectorAll("#filtros .chip").forEach(c =>
    c.classList.toggle("on", c.dataset.tag === tagAtiva));
  document.getElementById("limpar").style.display = tagAtiva ? "inline" : "none";
  render();
}

document.addEventListener("click", e => {
  const chip = e.target.closest("[data-tag]");
  if (chip){ aplicarTag(chip.dataset.tag); return; }
  if (e.target.id === "limpar") aplicarTag(tagAtiva);
});

busca.addEventListener("input", render);
ordenar.addEventListener("change", render);

fetch("dados.json")
  .then(r => r.json())
  .then(d => { ITENS = d.itens || []; montarFiltros(); render(); })
  .catch(() => { grid.innerHTML =
    '<div class="empty">Nao consegui carregar dados.json. Rode ./bin/galeria.</div>'; });
