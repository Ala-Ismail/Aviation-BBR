import { copyFile, mkdir, readFile, writeFile } from 'node:fs/promises';
import MarkdownIt from 'markdown-it';

const source = new URL('../', import.meta.url);
const output = new URL('dist/', source);
const pages = {
  'README.md': ['index.html', 'Overview'],
  'Aviation_BBR_technology_assessment.md': ['technology.html', 'Technology assessment'],
  'Aviation_BBR_business_assessment.md': ['business.html', 'Business assessment'],
  'Aviation_BBR_feasibility_study.md': ['feasibility.html', 'Feasibility study'],
};
const assets = [
  'LICENSE',
  'render_aviation_bbr_diagram.py',
  'images/aviation-bbr-top-level.png',
  'images/aviation-bbr-top-level.svg',
];

const markdown = new MarkdownIt();
markdown.core.ruler.push('site_links', ({ tokens }) => {
  for (let index = 0; index < tokens.length; index += 1) {
    const token = tokens[index];
    if (token.type === 'heading_open') {
      const title = tokens[index + 1].content;
      token.attrSet('id', title.toLowerCase().replace(/[^\w -]/g, '').replaceAll(' ', '-'));
    }
    for (const child of token.children ?? []) {
      const href = child.attrGet('href') ?? '';
      const [path, fragment] = href.split('#', 2);
      if (Object.hasOwn(pages, path)) {
        const [page] = pages[path];
        child.attrSet('href', fragment ? `${page}#${fragment}` : page);
      }
    }
  }
});

const renderFence = markdown.renderer.rules.fence;
markdown.renderer.rules.fence = (tokens, index, options, env, renderer) => {
  const code = renderFence(tokens, index, options, env, renderer);
  if (tokens[index].info === 'mermaid') {
    return `<details><summary>Recording-path diagram source</summary>${code}</details>`;
  }
  return code;
};

await mkdir(new URL('images/', output), { recursive: true });
await Promise.all(assets.map((path) => copyFile(new URL(path, source), new URL(path, output))));
await copyFile(new URL('style.css', import.meta.url), new URL('style.css', output));

for (const [path, [filename, label]] of Object.entries(pages)) {
  const content = await readFile(new URL(path, source), 'utf8');
  const links = Object.values(pages).map(([target, title]) => {
    const current = target === filename ? ' aria-current="page"' : '';
    return `<a href="${target}"${current}>${title}</a>`;
  });
  const article = markdown.render(content)
    .replaceAll('<table>', '<div class="table-wrap"><table>')
    .replaceAll('</table>', '</table></div>');
  const html = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${label} | Aviation BBR</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header><div class="site-header">
    <strong>Aviation BBR</strong>
    <nav aria-label="Assessments">${links.join('')}</nav>
  </div></header>
  <main>${article}</main>
</body>
</html>
`;
  await writeFile(new URL(filename, output), html);
}
