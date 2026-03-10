const fs = require("fs");
const path = require("path");

// Define qué copiar de cada paquete
const vendors = [
  {
    pkg: "@fortawesome/fontawesome-free",
    files: [
      { from: "css/all.min.css",  to: "static/css/vendor/fontawesome.min.css" },
      { from: "js/all.min.js",    to: "static/js/vendor/fontawesome.min.js" },
    ],
    dirs: [
      { from: "webfonts", to: "static/webfonts" },
    ],
  },
  // Agrega aquí nuevas librerías:
  // {
  //   pkg: "htmx.org",
  //   files: [
  //     { from: "dist/htmx.min.js", to: "static/js/vendor/htmx.min.js" },
  //   ],
  // },
];

function copyFile(src, dest) {
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.copyFileSync(src, dest);
  console.log(`  ✔ ${src} → ${dest}`);
}

function copyDir(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  fs.readdirSync(src).forEach((file) => {
    copyFile(path.join(src, file), path.join(dest, file));
  });
}

vendors.forEach(({ pkg, files = [], dirs = [] }) => {
  console.log(`\n📦 ${pkg}`);
  const base = path.join("node_modules", pkg);
  files.forEach(({ from, to }) => copyFile(path.join(base, from), to));
  dirs.forEach(({ from, to }) => copyDir(path.join(base, from), to));
});

console.log("\n✅ vendor listo");